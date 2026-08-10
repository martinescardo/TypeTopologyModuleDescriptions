#!/usr/bin/env python3

"""Recomputes the statistics reported in README.md from a clone of TypeTopology.

This script was written by an LLM. It is included in this repository so that
the computation behind the published figures can be checked rather than taken
on trust.

By default it only reports, comparing what it computes against what README.md
currently says. With --write it updates README.md in place. It never commits,
so the change can be inspected with git diff.

The figures it maintains are marked in README.md itself, invisibly, using the
comment syntax that markdown does not render. A single number inside a
sentence is written

    Of the <!--#dirs-->61<!--/#--> directories,

and only the digits between the markers are replaced, so the sentence around
them can be rewritten freely. A whole table, whose rows come and go, is
fenced instead,

    <!-- ttstats:directories -->
    ... table ...
    <!-- /ttstats:directories -->

and everything between the fences is regenerated, so a table must not be
edited by hand.

Two tables of names have to be maintained by a person, because no computation
can discover them: VARIANTS, which lists the spellings a contributor's name
takes in a file header, and GIT_ALIAS, which lists the identities they commit
under. When a git identity appears that is in neither, this script stops
rather than quietly counting that person's work as somebody else's.

Usage:

    ./ttstats.py                    report only
    ./ttstats.py --write            update README.md
    ./ttstats.py --typetopology DIR  use a TypeTopology clone elsewhere
"""

import argparse
import difflib
import math
import os
import re
import subprocess
import sys
import unicodedata
from collections import defaultdict
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))

# Contributors reaching this share, in either column, are named in the table.
# The test is against the figure as displayed, so somebody at 0.99% is named,
# their share having been rounded up to 1.0%.
THRESHOLD = 1.0

# Anyone within this much of the threshold is reported, since whether to name
# somebody who is a hundredth of a point short is not a decision for a script.
MARGIN = 0.1


# ---------------------------------------------------------------- name tables

# Canonical name -> the spellings it takes in a file header. Accents and case
# are ignored when matching, so only genuinely different spellings are needed.
VARIANTS = {
    "Martin Escardo": ["Martin Escardo", "Martin Hotzel Escardo"],
    "Tom de Jong": ["Tom de Jong"],
    "Ayberk Tosun": ["Ayberk Tosun"],
    "Andrew Sneap": ["Andrew Sneap"],
    "Andrew Swan": ["Andrew Swan"],
    "Chuangjie Xu": ["Chuangjie Xu"],
    "Todd Waugh Ambridge": ["Todd Waugh Ambridge", "Todd Ambridge"],
    "Ian Ray": ["Ian Ray"],
    "Paulo Oliva": ["Paulo Oliva"],
    "Nicolai Kraus": ["Nicolai Kraus"],
    "Jon Sterling": ["Jon Sterling", "Jonathan Sterling"],
    "Fredrik Nordvall Forsberg": ["Fredrik Nordvall Forsberg"],
    "Anna Williams": ["Anna Williams"],
    "Ettore Aldrovandi": ["Ettore Aldrovandi"],
    "Brendan Hart": ["Brendan Hart"],
    "Alice Laroche": ["Alice Laroche"],
    "Bruno Paiva": ["Bruno Paiva", "Bruno da Rocha Paiva"],
    "Carlo Angiuli": ["Carlo Angiuli"],
    "Cory Knapp": ["Cory Knapp"],
    "Evan Cavallo": ["Evan Cavallo"],
    "Fredrik Bakke": ["Fredrik Bakke"],
    "Igor Arrieta": ["Igor Arrieta"],
    "J. A. Carr": ["J. A. Carr", "J.A. Carr", "Jason Carr"],
    "Jakub Oprsal": ["Jakub Oprsal"],
    "Kelton OBrien": ["Kelton OBrien", "Kelton O'Brien"],
    "Keri D'Angelo": ["Keri D'Angelo", "Keri DAngelo"],
    "Lane Biocini": ["Lane Biocini"],
    "Marc Bezem": ["Marc Bezem"],
    "Ohad Kammar": ["Ohad Kammar"],
    "Paul Levy": ["Paul Levy"],
    "Peter Dybjer": ["Peter Dybjer"],
    "Simcha van Collem": ["Simcha van Collem"],
    "Thierry Coquand": ["Thierry Coquand"],
    "Vincent Rahli": ["Vincent Rahli"],
}

# The identity a commit is authored under -> canonical name. Add a line here
# when the script stops on an identity it does not recognise.
GIT_ALIAS = {
    "mhe": "Martin Escardo",
    "martinescardo": "Martin Escardo",
    "tomdjong": "Tom de Jong",
    "ayberkt": "Ayberk Tosun",
    "adsneap": "Andrew Sneap",
    "tnttodda": "Todd Waugh Ambridge",
    "IanRay11": "Ian Ray",
    "awsloth": "Anna Williams",
    "lane": "Lane Biocini",
    "Jason Carr": "J. A. Carr",
    "Jonathan Sterling": "Jon Sterling",
    "Bruno da Rocha Paiva": "Bruno Paiva",
    "Jakub Opršal": "Jakub Oprsal",
}

# People who have committed a stray fix but are not TypeTopology contributors,
# and are counted under "others" rather than named.
DRIVE_BY = {"Harrison Grodin", "Philip Dorrell", "Ingo Blechschmidt",
            "Scott Fleischman"}


def pct(x):
    """A percentage as the tables show it, rounded up, never understating."""
    return math.ceil(round(x * 10, 6)) / 10


def fold(s):
    """Drop accents and case, so a name matches however it is spelled."""
    return "".join(c for c in unicodedata.normalize("NFD", s.lower())
                   if unicodedata.category(c) != "Mn")


# Canonical names are themselves valid git identities.
for canon in VARIANTS:
    GIT_ALIAS.setdefault(canon, canon)

# Longest first, so "Martin Hotzel Escardo" is preferred to "Martin Escardo".
FOLDED = sorted(((fold(v), canon) for canon, vs in VARIANTS.items() for v in vs),
                key=lambda p: -len(p[0]))

FOLDED_ALIAS = {fold(k): v for k, v in GIT_ALIAS.items()}
FOLDED_DRIVE_BY = {fold(n) for n in DRIVE_BY}


# ------------------------------------------------------------------ the source

def git(tt, *args):
    return subprocess.run(["git", "-C", tt] + list(args),
                          capture_output=True, text=True, check=True).stdout


def ordinal(n):
    if 11 <= n % 100 <= 13:
        return f"{n}th"
    return f"{n}{ {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th') }"


def collect(tt):
    """Every figure the README reports, computed from the TypeTopology clone."""
    files = [f for f in git(tt, "ls-files", "source").splitlines()
             if f.endswith((".lagda", ".agda"))]
    if not files:
        sys.exit(f"no Agda files under source in {tt}")

    text = {}
    for f in files:
        with open(os.path.join(tt, f), encoding="utf-8") as h:
            text[f] = h.read().splitlines()

    total = sum(len(t) for t in text.values())
    nonblank = sum(1 for t in text.values() for line in t if line.strip())

    # A directory is a top-level subdirectory of source holding Agda files.
    dir_files, dir_lines = defaultdict(int), defaultdict(int)
    for f in files:
        parts = f.split("/")
        if len(parts) > 2:
            dir_files[parts[1]] += 1
            dir_lines[parts[1]] += len(text[f])

    indexed = sum(1 for line in
                  open(os.path.join(tt, "source/index.lagda"), encoding="utf-8")
                  if line.startswith("import "))

    # TypeTopology's own roll of contributors, less those it marks as having
    # written no Agda here.
    with open(os.path.join(tt, "README.md"), encoding="utf-8") as h:
        roll = h.read().split("## Current TypeTopology contributors")[1]
    listed = re.findall(r"^\* (.+?)\s*(\(i+\))?$", roll, re.M)
    if not listed:
        sys.exit("cannot find the contributor list in TypeTopology's README.md")

    return dict(files=files, text=text, total=total, nonblank=nonblank,
                dir_files=dir_files, dir_lines=dir_lines, indexed=indexed,
                listed=len(listed),
                contributors=sum(1 for _, mark in listed if not mark))


def header_names(lines):
    """The contributors named in a file's header, before the code begins."""
    head = []
    for line in lines[:25]:
        if line.startswith("\\begin{code}"):
            break
        head.append(line)
    blob = fold("\n".join(head))
    found = []
    for folded, canon in FOLDED:
        if folded in blob and canon not in found:
            found.append(canon)
            blob = blob.replace(folded, " ")   # a name is not counted twice
    return found


def attribute(tt, data):
    """Share of the lines due to each contributor, counted in the two ways."""
    by_header = defaultdict(float)
    headerless = []
    for f in data["files"]:
        names = header_names(data["text"][f])
        if names:
            for n in names:
                by_header[n] += len(data["text"][f]) / len(names)
        else:
            headerless.append(f)

    # A file with no name in its header goes to whoever first committed it.
    unknown = defaultdict(int)
    for f in headerless:
        log = git(tt, "log", "--follow", "--diff-filter=A", "--format=%an",
                  "--", f).splitlines()
        who = fold(log[-1].strip()) if log else ""
        if who in FOLDED_ALIAS:
            by_header[FOLDED_ALIAS[who]] += len(data["text"][f])
        else:
            by_header["others"] += len(data["text"][f])
            if who and who not in FOLDED_DRIVE_BY:
                unknown[log[-1].strip()] += 1

    by_blame = defaultdict(int)
    for f in data["files"]:
        for line in git(tt, "blame", "--line-porcelain", "--", f).splitlines():
            if line.startswith("author "):
                who = line[7:].strip()
                folded = fold(who)
                if folded in FOLDED_ALIAS:
                    by_blame[FOLDED_ALIAS[folded]] += 1
                else:
                    by_blame["others"] += 1
                    if folded not in FOLDED_DRIVE_BY:
                        unknown[who] += 1

    if unknown:
        print("This script does not recognise the following, and so cannot say",
              file=sys.stderr)
        print("whose work it is:\n", file=sys.stderr)
        for who, n in sorted(unknown.items(), key=lambda kv: -kv[1]):
            print(f"    {who}   ({n} lines or files)", file=sys.stderr)
        print("\nAdd each of them to GIT_ALIAS in this script, against the name"
              "\nthey are known by, or to DRIVE_BY if they are not a"
              "\nTypeTopology contributor. Nothing has been written.",
              file=sys.stderr)
        sys.exit(1)

    return by_header, by_blame, len(headerless)


# -------------------------------------------------------------- the two tables

def directories_table(data):
    ranked = sorted(data["dir_lines"].items(), key=lambda kv: -kv[1])
    top, rest = ranked[:12], ranked[12:]
    loose = len(data["files"]) - sum(data["dir_files"].values())
    rows = ["| directory | files | lines | share |",
            "| --- | ---: | ---: | ---: |"]
    for d, n in top:
        rows.append(f"| [{d}](#{d.lower()}) | {data['dir_files'][d]} | {n:,} |"
                    f" {pct(100 * n / data['total']):.1f}% |")
    # Everything not in the twelve, including the two loose files at the root
    # of source, so that the column still sums to the total.
    others = data["total"] - sum(n for _, n in top)
    rows.append(f"| others | {sum(data['dir_files'][d] for d, _ in rest) + loose}"
                f" | {others:,} | {pct(100 * others / data['total']):.1f}% |")
    return "\n".join(rows)


def contributors_table(by_header, by_blame):
    ht, bt = sum(by_header.values()), sum(by_blame.values())
    # Exact shares. Rounding up happens only where they are shown, and the
    # others row is computed from the exact remainder rather than by adding
    # up figures that have each already been rounded up.
    share = {n: (100 * by_header[n] / ht, 100 * by_blame[n] / bt)
             for n in set(by_header) | set(by_blame)}
    named = sorted((n for n in share if n != "others"
                    and max(pct(share[n][0]), pct(share[n][1])) >= THRESHOLD),
                   key=lambda n: -share[n][0])
    rows = ["| | by header | by blame |", "| --- | ---: | ---: |"]
    for n in named:
        rows.append(f"| {n} | {pct(share[n][0]):.1f}% | {pct(share[n][1]):.1f}% |")
    oh = sum(share[n][0] for n in share if n not in named)
    ob = sum(share[n][1] for n in share if n not in named)
    rows.append(f"| others | {pct(oh):.1f}% | {pct(ob):.1f}% |")

    borderline = [n for n in share if n != "others" and n not in named
                  and max(share[n]) >= THRESHOLD - MARGIN]
    return "\n".join(rows), borderline, share


# -------------------------------------------------------------- README surgery

INLINE = r"<!--#{name}-->(.*?)<!--/#-->"
FENCE = r"(<!-- ttstats:{name} -->\n)(.*?)(\n<!-- /ttstats:{name} -->)"


def read_inline(doc, name):
    return [m.group(1) for m in re.finditer(INLINE.format(name=name), doc)]


def read_fence(doc, name):
    m = re.search(FENCE.format(name=name), doc, re.S)
    return m.group(2) if m else None


def write_inline(doc, name, value):
    return re.sub(INLINE.format(name=name),
                  lambda m: f"<!--#{name}-->{value}<!--/#-->", doc)


def write_fence(doc, name, value):
    return re.sub(FENCE.format(name=name),
                  lambda m: m.group(1) + value + m.group(3), doc, flags=re.S)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--typetopology", default=os.path.join(HERE, "..", "TypeTopology"),
                    help="the TypeTopology clone to measure")
    ap.add_argument("--readme", default=os.path.join(HERE, "README.md"))
    ap.add_argument("--write", action="store_true",
                    help="update README.md instead of only reporting")
    args = ap.parse_args()

    tt = os.path.abspath(args.typetopology)
    if not os.path.isdir(os.path.join(tt, "source")):
        sys.exit(f"{tt} does not look like a TypeTopology clone")

    data = collect(tt)
    by_header, by_blame, headerless = attribute(tt, data)
    dirs = directories_table(data)
    contribs, borderline, share = contributors_table(by_header, by_blame)

    today = date.today()
    fresh = {
        "date": f"{ordinal(today.day)} {today:%B %Y}",
        "files": f"{len(data['files']):,}",
        "lines": f"{data['total']:,}",
        "nonblank": f"{data['nonblank']:,}",
        "dirs": f"{len(data['dir_files']):,}",
        "indexed": f"{data['indexed']:,}",
        "contributors": f"{data['contributors']:,}",
    }

    with open(args.readme, encoding="utf-8") as h:
        doc = h.read()

    stale = []
    for name, value in fresh.items():
        found = read_inline(doc, name)
        if not found:
            sys.exit(f"README.md has no marker for {name}. Nothing written.")
        if any(v != value for v in found):
            stale.append((name, found[0], value))
    for name, value in (("directories", dirs), ("contributors", contribs)):
        current = read_fence(doc, name)
        if current is None:
            sys.exit(f"README.md has no fence for {name}. Nothing written.")
        if current != value:
            stale.append((name, "table", value))

    print(f"measured {len(data['files']):,} Agda files at "
          f"{git(tt, 'rev-parse', '--short', 'HEAD').strip()}, "
          f"{headerless} of them with no name in the header")

    if not stale:
        print("README.md is up to date.")
    else:
        for name, was, now in stale:
            if was == "table":
                print(f"\n  the {name} table would change:")
                for line in difflib.unified_diff(
                        read_fence(doc, name).split("\n"), now.split("\n"),
                        "README.md", "computed now", lineterm="", n=0):
                    if not line.startswith(("---", "+++", "@@")):
                        print(f"    {line}")
            else:
                print(f"  {name:<12} {was:>16}  ->  {now}")

    if borderline:
        print(f"\nWithin {MARGIN}% of the {THRESHOLD}% threshold for being named,"
              " so worth a look:")
        for n in borderline:
            print(f"    {n}   {share[n][0]:.2f}% by header,"
                  f" {share[n][1]:.2f}% by blame")

    print(f"\nTypeTopology lists {data['listed']} contributors, of whom"
          f" {data['contributors']} have written Agda, which is the figure"
          "\nreported as Contributors.")

    if args.write:
        for name, value in fresh.items():
            doc = write_inline(doc, name, value)
        doc = write_fence(doc, "directories", dirs)
        doc = write_fence(doc, "contributors", contribs)
        with open(args.readme, "w", encoding="utf-8") as h:
            h.write(doc)
        print(f"\n{args.readme} written. Inspect it with git diff.")
    elif stale:
        print("\nRun again with --write to update README.md.")


if __name__ == "__main__":
    main()
