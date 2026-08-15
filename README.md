# [TypeTopology](https://github.com/martinescardo/TypeTopology) module descriptions

This file describes what each directory of
[TypeTopology](https://github.com/martinescardo/TypeTopology) does.

It was automatically generated using various command-line tools and
generative AI, and then manually curated by Martin Escardo,
July–August 2026, over a period of six weeks. Tom de Jong suggested
and contributed further revisions over the span of two weeks. However,
significant errors and omissions may still remain, given the
[magnitude of the repository](#repository-statistics).

From now on, anybody contributing to TypeTopology should update this
file whenever appropriate, manually, although the statistics below
should be updated automatically by the repository maintainers.

## Table of contents

1. [Organization](#organization)
1. [Searching TypeTopology](#searching-typetopology)
1. [Repository statistics](#repository-statistics)
1. [Contributors](#contributors)
1. [Authors](#authors)
1. [Philosophy of the repository](#philosophy-of-the-repository)

<details>
<summary>7. <a href="#description-of-safe-modules">Description of safe modules</a></summary>

1. [AlgebraicStructuresForcingSethood](#algebraicstructuresforcingsethood)
1. [Apartness](#apartness)
1. [BinarySystems](#binarysystems)
1. [CantorSchroederBernstein](#cantorschroederbernstein)
1. [Cardinals](#cardinals)
1. [Categories](#categories)
1. [CoNaturals](#conaturals)
1. [ContinuityAxiom](#continuityaxiom)
1. [Coslice](#coslice)
1. [CrossedModules](#crossedmodules)
1. [C-Spaces](#c-spaces)
1. [DedekindReals](#dedekindreals)
1. [DiscreteGraphicMonoids](#discretegraphicmonoids)
1. [DomainTheory](#domaintheory)
1. [Dominance](#dominance)
1. [Duploids](#duploids)
1. [Dyadics](#dyadics)
1. [DyadicsInductive](#dyadicsinductive)
1. [EffectfulForcing](#effectfulforcing)
1. [EGroups](#egroups)
1. [Factorial](#factorial)
1. [Field](#field)
1. [Fin](#fin)
1. [Games](#games)
1. [Groups](#groups)
1. [Higgs](#higgs)
1. [InjectiveTypes](#injectivetypes)
1. [Integers](#integers)
1. [Iterative](#iterative)
1. [Lifting](#lifting)
1. [Locales](#locales)
1. [MetricSpaces](#metricspaces)
1. [MGS](#mgs)
1. [MLTT](#mltt)
1. [Modal](#modal)
1. [MonadOnTypes](#monadontypes)
1. [Naturals](#naturals)
1. [Notation](#notation)
1. [NotionsOfDecidability](#notionsofdecidability)
1. [OrderedTypes](#orderedtypes)
1. [Ordinals](#ordinals)
1. [PathSequences](#pathsequences)
1. [PCF](#pcf)
1. [Quotient](#quotient)
1. [Rationals](#rationals)
1. [ReflexiveGraphs](#reflexivegraphs)
1. [Relations](#relations)
1. [RelativeMonadOnStructuredTypes](#relativemonadonstructuredtypes)
1. [Slice](#slice)
1. [SyntheticHomotopyTheory](#synthetichomotopytheory)
1. [Taboos](#taboos)
1. [TWA](#twa)
1. [TypeTopology](#typetopology)
1. [UF](#uf)
1. [W](#w)
1. [WildCategories](#wildcategories)
1. [deprecated](#deprecated)
1. [Various](#various)
   1. [CantorTheoremForEmbeddings](#variouscantortheoremforembeddings)
   1. [Dedekind](#variousdedekind)
   1. [DedekindNonAxiomatic](#variousdedekindnonaxiomatic)
   1. [DummettDisjunction](#variousdummettdisjunction)
   1. [LawvereFPT](#variouslawverefpt)
   1. [LawvereFPT-Generalized](#variouslawverefpt-generalized)
   1. [Lumsdaine](#variouslumsdaine)
   1. [NatIsSetWithoutUniverse](#variousnatissetwithoutuniverse)
   1. [NonCollapsibleFamily](#variousnoncollapsiblefamily)
   1. [Pataraia](#variouspataraia)
   1. [Pataraia-Taylor](#variouspataraia-taylor)
   1. [RootsOfBooleanFunctions](#variousrootsofbooleanfunctions)
   1. [Types2019](#varioustypes2019)
   1. [UnivalenceFromScratch](#variousunivalencefromscratch)
1. [gist](#gist)
   1. [2-injective-types](#gist2-injective-types)
   1. [Ackermann](#gistackermann)
   1. [DependentlyTypedTensors](#gistdependentlytypedtensors)
   1. [Hydra](#gisthydra)
   1. [InjectivesVersusAlgebras](#gistinjectivesversusalgebras)
   1. [IntervalObject](#gistintervalobject)
   1. [multiset-addendum-question](#gistmultiset-addendum-question)
   1. [not-an-apartness](#gistnot-an-apartness)
   1. [remove-swap](#gistremove-swap)
   1. [TotallySeparatedReflectionOfOmega](#gisttotallyseparatedreflectionofomega)
   1. [transport-discussion](#gisttransport-discussion)
   1. [wrong-proofs](#gistwrong-proofs)
   1. [MajoritiesOnlyActOnSets](#gistmajoritiesonlyactonsets)

</details>

<details>
<summary>8. <a href="#description-of-unsafe-modules">Description of unsafe modules</a></summary>

1. [Unsafe](#unsafe)
   1. [Games.Main](#gamesmain)
   1. [SyntheticHomotopyTheory.Circle.FundamentalGroup](#synthetichomotopytheorycirclefundamentalgroup)
   1. [SyntheticHomotopyTheory.Circle.WithRewriting](#synthetichomotopytheorycirclewithrewriting)
   1. [TWA.Thesis.Chapter6.Main](#twathesischapter6main)
   1. [CantorCompact](#unsafecantorcompact)
   1. [CoNat-Equiv](#unsafeconat-equiv)
   1. [CountableTychonoff](#unsafecountabletychonoff)
   1. [Haskell](#unsafehaskell)
   1. [Type-in-Type-False](#unsafetype-in-type-false)
1. [InfinitePigeon](#infinitepigeon)
   1. [J-Shift-BBC](#infinitepigeonj-shift-bbc)
   1. [J-Shift-Selection](#infinitepigeonj-shift-selection)
   1. [K-Shift-MBR](#infinitepigeonk-shift-mbr)

</details>

9. [List of people mentioned in the files](#list-of-people-mentioned-in-the-files)

## Organization

There is one entry for each of the directories imported by the module
[index](https://www.cs.bham.ac.uk/~mhe/TypeTopology/index.html), a
paragraph or a few for each, in alphabetical order, except for
[Various](#various) and [gist](#gist), which collect miscellaneous material
and come at the end. A final section describes the modules that are not
`--safe`, which are those imported by
[Unsafe.index](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Unsafe.index.html)
and three of those of [InfinitePigeon](#infinitepigeon), saying in each case
which Agda option is responsible.

The names of the directories and modules link to their html rendering, which
lives at <https://www.cs.bham.ac.uk/~mhe/TypeTopology/>.

Many directories collect the work of several people and span several
years, and so the descriptions are deliberately brief, with the
individual files and their own index modules giving the fuller
details, references and precise attributions. The attributions are taken
from the file headers, and for the larger directories they may be
incomplete (please add yourself if you notice that you are missing, or
anybody else you notice is missing).

Where the files record a publication that resulted from the development,
meaning an article, thesis or abstract by its authors reporting this work,
or the unformalized counterpart that this formalizes, it is listed after the
authors. The
[README](https://github.com/martinescardo/TypeTopology/blob/master/README.md)
of the repository has the same
[publications](https://github.com/martinescardo/TypeTopology/blob/master/README.md#academic-publications-and-preprints-resulting-from-typetopology)
in a single chronological list, and what the entries below add is the
directory that each of them concerns. A number of the files are new research
that haven't been written up as papers or submitted for publication yet,
although they are intended to eventually be.

[Table of contents](#table-of-contents)

## Searching TypeTopology

The repository can be searched for a name, a concept or a contributor at
<https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html>, which is also
what the links in the [contributors](#contributors) list below use. The
same searches are
[available from Emacs](https://github.com/martinescardo/TypeTopologySearch/blob/main/README.md).

[Table of contents](#table-of-contents)

## Repository statistics

The counts below were taken on <!--#date-->14th August 2026<!--/#-->, over
the Agda files tracked by git in the directory source.

| what is counted | count |
| --- | ---: |
| Agda files | <!--#files-->990<!--/#--> |
| Lines, including comments and blank lines | <!--#lines-->287,833<!--/#--> |
| Lines that are not blank | <!--#nonblank-->223,253<!--/#--> |
| Directories | <!--#dirs-->61<!--/#--> |
| Contributors | <!--#contributors-->35<!--/#--> |

Of the <!--#dirs-->61<!--/#--> directories, <!--#indexed-->59<!--/#--> are
imported by [index](https://www.cs.bham.ac.uk/~mhe/TypeTopology/index.html)
and are described below, and the remaining two,
[InfinitePigeon](#infinitepigeon) and [Unsafe](#unsafe), are reached only
through
[AllModulesIndex](https://www.cs.bham.ac.uk/~mhe/TypeTopology/AllModulesIndex.html).
Besides the directories, the [root of
source](https://github.com/martinescardo/TypeTopology/tree/master/source)
holds those two index files themselves.

The twelve largest directories account for about two thirds of the lines.
One of them, `TypeTopology`, bears the same name as the repository; it is the
directory that is meant here and throughout.

<!-- ttstats:directories -->
| directory | files | lines | share |
| --- | ---: | ---: | ---: |
| [Ordinals](#ordinals) | 67 | 29,825 | 10.4% |
| [Locales](#locales) | 85 | 29,553 | 10.3% |
| [UF](#uf) | 80 | 27,213 | 9.5% |
| [DomainTheory](#domaintheory) | 44 | 19,260 | 6.7% |
| [TypeTopology](#typetopology) | 35 | 14,611 | 5.1% |
| [TWA](#twa) | 33 | 10,972 | 3.9% |
| [InjectiveTypes](#injectivetypes) | 19 | 10,913 | 3.8% |
| [MGS](#mgs) | 30 | 9,298 | 3.3% |
| [Groups](#groups) | 27 | 7,681 | 2.7% |
| [C-Spaces](#c-spaces) | 38 | 7,377 | 2.6% |
| [EffectfulForcing](#effectfulforcing) | 27 | 7,360 | 2.6% |
| [Various](#various) | 15 | 6,945 | 2.5% |
| others | 490 | 106,825 | 37.2% |
<!-- /ttstats:directories -->

[Table of contents](#table-of-contents)

## Contributors

[TypeTopology](https://github.com/martinescardo/TypeTopology)
was started by [Martin Escardo](https://www.cs.bham.ac.uk/~mhe)
at around 2010, and by now there are many contributors, including
former and current students, collaborators, and people doing their own
work.

To put numbers on this, the table below gives the share of
the <!--#files-->990<!--/#--> Agda files of the repository that is due to
each of us, counted in two ways. The first column attributes each file to
the authors named in its header, splitting a file equally when it names
several, and resolves the few files with no name in the header by the git
history. The second column is what git blame reports, after merging the
aliases under which some of us commit, and so it counts the author of the
last change to each line.

<!-- ttstats:contributors -->
| | by header | by blame |
| --- | ---: | ---: |
| Martin Escardo | 45.3% | 53.4% |
| Tom de Jong | 12.3% | 14.8% |
| Ayberk Tosun | 11.6% | 11.5% |
| Andrew Sneap | 5.5% | 4.3% |
| Chuangjie Xu | 4.1% | 2.7% |
| Todd Waugh Ambridge | 3.7% | 2.8% |
| Ian Ray | 3.0% | 3.3% |
| Paulo Oliva | 2.4% | 0.0% |
| Nicolai Kraus | 1.7% | 0.3% |
| Jon Sterling | 1.5% | 1.2% |
| Fredrik Nordvall Forsberg | 1.4% | 0.0% |
| Anna Williams | 1.1% | 1.2% |
| Ettore Aldrovandi | 1.1% | 1.6% |
| Brendan Hart | 1.0% | 0.0% |
| others | 5.0% | 3.5% |
<!-- /ttstats:contributors -->

The table was last updated on <!--#date-->14th August 2026<!--/#-->. It
names only those of us who reach 1% in at least one of the two columns, and
so it is not a list of contributors. The [full
list](https://github.com/martinescardo/TypeTopology/blob/master/README.md#current-contributors-in-alphabetical-order-of-first-name)
is in the
[README](https://github.com/martinescardo/TypeTopology/blob/master/README.md)
of the repository, which also records two contributors who wrote no Agda
here, having contributed to constructions, theorems and proofs through the
hands of others.

Both counts include comments and blank lines. They differ where a file was
later edited, refactored or renamed by someone other than its author, which
moves lines to whoever did the editing, and they differ more sharply where
one of us committed a file written by someone else, which is why some
contributors have no lines at all in the second column. Neither count
measures the ideas, the questions posed or the supervision that lie behind
the files.

[Table of contents](#table-of-contents)

## Authors

Where an entry below names several authors, they are listed in order of
the amount contributed, without saying by how much, since the boundary
between one person's contribution and another's is usually too blurred
for a number to mean much.

[Table of contents](#table-of-contents)

## Philosophy of the repository

Most modules of the repository are developed in a Spartan intensional
Martin-Löf type theory, with the univalent point of view adopted
throughout. A few modules rely on more advanced MLTT concepts, such as
induction-recursion, and a number of them use the universe 𝓤ω. Nothing
is postulated. Univalence, function extensionality, propositional
truncation, propositional resizing, excluded middle and choice are
explicit assumptions of the theorems and modules that need them, so
that each result records what it depends on. See the main
[index file of the repository](https://www.cs.bham.ac.uk/~mhe/TypeTopology/index.html)
for further details. A few modules that significantly depart from this
philosophy are discussed in
[Description of unsafe modules](#description-of-unsafe-modules).

[Table of contents](#table-of-contents)

## Description of safe modules

### [AlgebraicStructuresForcingSethood](https://www.cs.bham.ac.uk/~mhe/TypeTopology/AlgebraicStructuresForcingSethood.index.html)

We study algebraic structures whose mere existence on a type forces
the type to be a set, that is, to have propositional identity
types. What is striking is that the equations are ordinary ones,
imposed on points only, with no higher coherences, and yet
they collapse the higher structure. Any type with a binary operation
that is associative, commutative and idempotent is a set, so that
there are no higher semilattices, and the same holds for a type with a
ternary majority operation and for one with ternary operations
satisfying Willard's equations. Weaker hypotheses give weaker
conclusions: a commutative idempotent operation makes the loop spaces
commutative, and an operation satisfying a non-trivial idempotent
Maltsev condition makes the fundamental group abelian. The proofs go
through the loop spaces, and the streamlined versions factor the
original ones through a single criterion for their triviality. The
ancestry is in universal algebra, in results of Taylor from 1977 about
topological algebras being homotopy equivalent to discrete spaces.

By Jakub Opršal, Tom de Jong and Martin Escardo, the semilattice part
following David Wärn.

[Table of contents](#table-of-contents)

### [Apartness](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Apartness.index.html)

Apartness relations, including tight apartness, are treated together with
their basic theory. An apartness is the positive, constructive counterpart
of the negation of equality. Rather than saying that two points are not
equal, one gives positive information witnessing that they are apart.
Besides the definition and the general properties, there are morphisms of
apartness types and the tight reflection, which universally forces an
apartness to be tight. A strong version of the notion is also considered,
whose cotransitivity is untruncated. Elements that are not not equal are
never apart, and it follows that a type with a tight apartness is a set. The
negation of an apartness has a positive characterization, two elements
failing to be apart precisely when the same elements are apart from both,
which as far as we know is new.

An apartness is nontrivial when it does tell two points apart. Weak excluded
middle gives a nontrivial apartness on any type with two distinct points.
Classically the negation of equality is the only tight apartness a type can
have, but this uniqueness is a constructive taboo. For the Cantor type it
implies that WLPO gives LPO, and for ℕ, or any discrete type with two
distinct points, it gives double negation elimination.

By Martin Escardo and Tom de Jong.

[Table of contents](#table-of-contents)

### [BinarySystems](https://www.cs.bham.ac.uk/~mhe/TypeTopology/BinarySystems.index.html)

The initial binary system is constructed. A binary system is a type with two
distinguished points a and b and two endofunctions f and g, subject to the
equations a = f a, f b = g a and b = g b, which make it the algebra
underlying binary subdivision, so that it is closely related to the interval
and to signed binary notation for dyadic numbers. The initial one is the
closed interval of dyadic rationals, and it is built in Spartan Martin-Löf
type theory without higher inductive types, quotients or extensionality
axioms, because the quotient that is needed happens to be available.

Two constructions are given, the first working with a subtype of normal
elements and the second avoiding it, which is simpler. The second does not
require the underlying type of a binary system to be a set, and sethood of
the initial one follows rather than being assumed. A third construction, in
cubical type theory, defines the initial binary system both as a higher
inductive type and in pure Martin-Löf type theory and shows the two
definitions equivalent, from which sethood also follows. It is not imported
by the index, because it needs Agda 2.6.2 together with the Cubical Library
and currently breaks the build, so it is linked directly:
[CubicalBinarySystem](https://github.com/martinescardo/TypeTopology/blob/master/source/BinarySystems/CubicalBinarySystem.lagda).

By Martin Escardo and Alex Rice.

[Table of contents](#table-of-contents)

### [CantorSchroederBernstein](https://www.cs.bham.ac.uk/~mhe/TypeTopology/CantorSchroederBernstein.index.html)

Here the Cantor–Schröder–Bernstein theorem is generalized from sets to
arbitrary (homotopy) types, so that if there are embeddings between
two types in both directions, then the types are equivalent. This is
proved under the assumption of excluded middle, and holds in any
boolean ∞-topos. A later variation, by Fredrik Bakke, weakens excluded
middle to WLPO, at the cost of stronger hypotheses on the two
embeddings, which is necessary because the theorem for sets already
implies excluded middle.

By Martin Escardo.

**Publications.**

1. M.H. Escardó, "The Cantor–Schröder–Bernstein Theorem for ∞-groupoids",
   Journal of Homotopy and Related Structures 16(3), 2021, 363–366, [doi:10.1007/s40062-021-00284-6](https://doi.org/10.1007/s40062-021-00284-6),
   which is the unformalized version of part of this development.

1. F. Bakke, "The Cantor–Schröder–Bernstein theorem in ∞-Topoi", slides,
   2025, <https://hott-uf.github.io/2025/slides/Bakke.pdf>, for the WLPO variation.

[Table of contents](#table-of-contents)

### [Cardinals](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Cardinals.index.html)

Cardinals are studied in univalent foundations. The HoTT book obtains
weak successor cardinals from excluded middle, and what is shown here
is that suitable propositional resizing assumptions give them
constructively instead.

By Jon Sterling.

[Table of contents](#table-of-contents)

### [Categories](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Categories.index.html)

Here some 1-category theory is developed in univalent foundations. Wild
categories, precategories, univalent categories, functors and natural
transformations are all treated, with the distinctions between these levels
of coherence taken seriously. There are also adjoints, displayed categories
and a range of examples, with one module corresponding to the author's MSci
project.

By Anna Williams.

**Publication.**

1. A. Williams, "Formalising Displayed Categories with Univalent
   Foundations", MSci project,
   <https://anna-maths.xyz/assets/papers/disp-categories.pdf>.

[Table of contents](#table-of-contents)

### [CoNaturals](https://www.cs.bham.ac.uk/~mhe/TypeTopology/CoNaturals.index.html)

The type of conatural numbers is presented as decreasing binary sequences,
also called the *generic convergent sequence* in the repository, where the
terminology comes from its connection with topology. It includes its
universal property as a final coalgebra, an equivalent copy and a comparison
between the two presentations, and its arithmetic. A sharpness relation and
further properties are also developed.

By Martin Escardo and Chuangjie Xu.

[Table of contents](#table-of-contents)

### [ContinuityAxiom](https://www.cs.bham.ac.uk/~mhe/TypeTopology/ContinuityAxiom.index.html)

Here we show that a Brouwerian continuity principle is inconsistent with the
Curry–Howard interpretation. Formulating "all functions are continuous" as a
type inhabited by an explicit modulus-of-continuity functional leads to a
contradiction, in contrast with the consistent propositionally-truncated
formulations used elsewhere. The contradiction is derived in more than one
way, including a version that avoids identity types, with related material
on uniform continuity.

By Martin Escardo and Chuangjie Xu.

**Publication.**

1. M.H. Escardó and C. Xu, "The Inconsistency of a Brouwerian Continuity
   Principle with the Curry–Howard Interpretation", TLCA 2015, LIPIcs, [doi:10.4230/LIPIcs.TLCA.2015.153](https://doi.org/10.4230/LIPIcs.TLCA.2015.153).

[Table of contents](#table-of-contents)

### [Coslice](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Coslice.index.html)

The coslice (∞,1)-category of a universe under a given type is studied.
While this concept cannot be formalized in its entirety in current univalent
foundations, one can nonetheless carry out concrete constructions, such as
defining the coslice objects and their homomorphisms and characterizing its
path spaces.

By Jon Sterling.

[Table of contents](#table-of-contents)

### [CrossedModules](https://www.cs.bham.ac.uk/~mhe/TypeTopology/CrossedModules.index.html)

Here we have crossed modules, a two-dimensional algebraic structure
equivalent to internal categories in groups. A single module sets up the
definition and its basic theory.

By Ettore Aldrovandi and Keri D'Angelo.

[Table of contents](#table-of-contents)

### [C-Spaces](https://www.cs.bham.ac.uk/~mhe/TypeTopology/C-Spaces.index.html)

C-spaces are developed, following the PhD thesis of Chuangjie Xu, which
gives a continuous computational interpretation of type theory. A C-space is
a set equipped with a notion of continuity given by probes from the Cantor
space, and the category of C-spaces is cartesian closed, indeed locally
cartesian closed, with a natural numbers object, so that it models type
theory. A central outcome is a fan functional that continuously computes
least moduli of uniform continuity for maps from the Cantor space to the
natural numbers. The modules are arranged to mirror the main mathematical
stages of the thesis and can be read as a guide to where the corresponding
arguments appear in Agda. They include a coverage and the associated notion
of uniform continuity, the syntax of system T and of HAω, and the structure
of a category with families. The main development assumes function
extensionality. A second and less direct one strengthens the probe axioms so
that only the double negation of function extensionality is needed, which
carries no computational content and so does not obstruct normalization, with
the effect that the moduli extracted there normalize to numerals, as they
need not do in the first. The note by Coquand, Danielsson, Escardó, Norell
and Xu cited below justifies this, showing that negative consistent axioms
can be postulated without loss of canonicity.

By Chuangjie Xu and Martin Escardo.

**Publications.**

1. C. Xu, "A Continuous Computational Interpretation of Type
   Theories", PhD thesis, University of Birmingham, 2015,
   <https://cj-xu.github.io/ContinuityType/xu-thesis.pdf>, which this
   formalizes.

1. C. Xu and M.H. Escardó, "A constructive model of uniform continuity",
   TLCA 2013, [doi:10.1007/978-3-642-38946-7_18](https://doi.org/10.1007/978-3-642-38946-7_18).

1. M.H. Escardó and C. Xu, "A constructive manifestation of the
   Kleene-Kreisel continuous functionals", Annals of Pure and Applied Logic
   167(9), 2016, [doi:10.1016/j.apal.2016.04.011](https://doi.org/10.1016/j.apal.2016.04.011).

1. T. Coquand, N.A. Danielsson, M.H. Escardó, U. Norell and C. Xu.
   "Negative consistent axioms can be postulated without loss of
   canonicity". [3-page unpublished note](https://www.cs.bham.ac.uk/~mhe/papers/negative-axioms.pdf), 19th October 2013, updated 25th October 2017.

   [Formalized in
   Agda](https://github.com/andreasabel/logrel-mltt/tree/master/Application/NegativeAxioms)
   by Andreas Abel, 2022.

[Table of contents](#table-of-contents)

### [DedekindReals](https://www.cs.bham.ac.uk/~mhe/TypeTopology/DedekindReals.index.html)

The Dedekind real numbers are constructed as two-sided Dedekind cuts,
together with their arithmetic and order. A real is a pair of a lower and an
upper cut, and the library develops addition, multiplication, order and
their properties, with a mechanism for extending functions to the reals.
This is the proper library of Dedekind reals, whereas
[Various.Dedekind](#variousdedekind) is separate, being exploratory notes
rather than a library.

By Andrew Sneap.

[Table of contents](#table-of-contents)

### [DiscreteGraphicMonoids](https://www.cs.bham.ac.uk/~mhe/TypeTopology/DiscreteGraphicMonoids.index.html)

Following Lawvere, lists without repetitions over a discrete type are shown
to form the free discrete graphic monoid, a monoid being called graphic when
it satisfies the identity xyx = xy. From this it follows, in a standard way,
that such lists form a monad, and moreover an affine one, which is the whole
point of the exercise, for applications to game theory in [Games](#games).

By Martin Escardo and Paulo Oliva.

[Table of contents](#table-of-contents)

### [DomainTheory](https://www.cs.bham.ac.uk/~mhe/TypeTopology/DomainTheory.index.html)

Domain theory is developed in constructive and predicative univalent
foundations. Much of the code accompanies Tom de Jong's PhD thesis "Domain
Theory in Constructive and Predicative Univalent Foundations" and the index file
provides an overview of the full development.

We give a brief summary here and highlight the additions outside the
aforementioned PhD thesis after. The code defines directed complete posets
(dcpos) and their basic theory. It also develops the theory of continuous and
algebraic dcpos, with small bases playing an important role in the predicative
setting where dcpos are large structures. The classical construction of flat
domains is shown to be constructively inadequate: if the flat poset with carrier
𝟙 + ℕ is ω-complete/directed complete, then the constructive taboo LPO
holds. Instead, the Escardó–Knapp lifting (the type of partial elements) is used
to construct the free pointed dcpo on a set (and with a refined order relation,
on a dcpo as well). Formalized examples of dcpos include (large) powersets, the
type of propositions, the poset of ordinals, the type of extended partial
Dedekind reals, and the ideal completion of the dyadics. Finally, Scott's D∞,
which is isomorphic to its own function space, is constructed via general
directed bilimits, and the Scott model of the combinatory version of PCF is also
defined.

Martin Escardo ported code by Brendan Hart that formalizes the Scott model for
the λ-calculus version of PCF and the proof of its computational adequacy.
The Scott topology of a dcpo and the notion of a Scott domain are formalized by
Ayberk Tosun. The point-free counterpart is in [Locales](#locales), where the
Scott locale of a Scott domain is proved spectral.
Finally, Simcha van Collem showed that for small dcpos (which exist in the
presence of propositional resizing), canonical continuity and algebraicity data
can be defined from their respective truncated existence.

By Tom de Jong, Brendan Hart, Ayberk Tosun, Simcha van Collem and Martin
Escardo.

**Publications.**

1. T. de Jong and M.H. Escardó, "Domain Theory in Constructive and
   Predicative Univalent Foundations", CSL 2021, LIPIcs 183, [doi:10.4230/LIPIcs.CSL.2021.28](https://doi.org/10.4230/LIPIcs.CSL.2021.28).

1. T. de Jong, "The Scott model of PCF in univalent type theory",
   Mathematical Structures in Computer Science 31(10), 2021, [doi:10.1017/S0960129521000153](https://doi.org/10.1017/S0960129521000153),
   also listed under [PCF](#pcf).

1. T. de Jong, "Domain Theory in Constructive and Predicative Univalent
   Foundations", PhD thesis, University of Birmingham, 2023, <https://etheses.bham.ac.uk/id/eprint/13401/>, [arXiv:2301.12405](https://arxiv.org/abs/2301.12405).

1. T. de Jong, "Domain theory in univalent foundations I: Directed complete
   posets and Scott's D∞", 2024, [doi:10.48550/arXiv.2407.06952](https://doi.org/10.48550/arXiv.2407.06952).

1. T. de Jong and M.H. Escardó, "Continuous and algebraic domains in
   univalent foundations", which is part II, Journal of Pure and Applied
   Algebra 229(10), 2025, [doi:10.1016/j.jpaa.2025.108072](https://doi.org/10.1016/j.jpaa.2025.108072), [arXiv:2407.06956](https://arxiv.org/abs/2407.06956).

[Table of contents](#table-of-contents)

### [Dominance](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Dominance.index.html)

Dominances in the sense of Rosolini are studied, that is, classes of
propositions closed under the operations needed to serve as a notion of
semidecidability, together with their relationship to decidability, the
initial dominance, and the connection with the lifting monad.

By Martin Escardo and Jon Sterling.

**Publication.**

1. M.H. Escardó and C. Knapp, "Partial Elements and Recursion via Dominances
   in Univalent Type Theory", CSL 2017, LIPIcs, [doi:10.4230/LIPIcs.CSL.2017.21](https://doi.org/10.4230/LIPIcs.CSL.2017.21).

[Table of contents](#table-of-contents)

### [Duploids](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Duploids.index.html)

Here we have duploids, a categorical semantics due to Munch-Maccagnoni that
unifies polarized sequent calculus, call-by-push-value and abstract
machines. A duploid generalizes a category by relaxing associativity in a
way compatible with viewing morphisms as effectful programs. The
formalization builds duploids from a deductive system, via preduploids, and
includes the depolarization construction.

By Jon Sterling.

[Table of contents](#table-of-contents)

### [Dyadics](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Dyadics.index.html)

The dyadic rational numbers, that is, the rationals with power-of-two
denominators, are developed with their type, addition, multiplication,
negation and order.

By Andrew Sneap.

[Table of contents](#table-of-contents)

### [DyadicsInductive](https://www.cs.bham.ac.uk/~mhe/TypeTopology/DyadicsInductive.index.html)

Here the dyadic rationals are defined inductively, as suggested by Martin
Escardo and formalized by Tom de Jong, giving an alternative to the
construction in the [Dyadics](#dyadics) directory. Those of the open
interval from −1 to 1 are generated from its midpoint by the two maps that
send x to (x−1)/2 and to (x+1)/2, an order on them is defined inductively
and shown to be transitive and linear, and density and the absence of
endpoints are proved.

By Tom de Jong.

[Table of contents](#table-of-contents)

### [EffectfulForcing](https://www.cs.bham.ac.uk/~mhe/TypeTopology/EffectfulForcing.index.html)

Dialogue trees and effectful forcing give a semantics of Gödel's system T in
a monad of dialogue trees. From the dialogue tree of a definable functional
one reads off its continuity on the Baire type and the uniform continuity of
its restriction to the Cantor type, both externally and via an internal
version of the argument. The external development includes the MFPS paper
and several variations, among them an oracle-free proof and a translation of
dialogue trees to Brouwer trees, while the internal one produces, for every
closed system T term of type (ι → ι) → ι, a system T term that
Church-encodes a dialogue tree of its standard interpretation, together with
proofs of correctness. From these terms one obtains further system T terms
that compute moduli of continuity and of uniform continuity, again proved
correct.

By Martin Escardo, Ayberk Tosun, Bruno da Rocha Paiva, Vincent Rahli,
Chuangjie Xu and Paulo Oliva.

**Publications.**

1. M.H. Escardó, "Continuity of Gödel's system T definable functionals via
   effectful forcing", MFPS XXIX, Electronic Notes in Theoretical Computer
   Science 298, 2013, 119–141, [doi:10.1016/j.entcs.2013.09.010](https://doi.org/10.1016/j.entcs.2013.09.010).

1. M.H. Escardó, B. da Rocha Paiva, V. Rahli and A. Tosun, "Internal
   Effectful Forcing in System T", FSCD 2025, [doi:10.48550/arXiv.2505.11055](https://doi.org/10.48550/arXiv.2505.11055).

[Table of contents](#table-of-contents)

### [EGroups](https://www.cs.bham.ac.uk/~mhe/TypeTopology/EGroups.index.html)

Free groups are constructed here in pure Martin-Löf type theory using
setoids. A setoid is a type with an equivalence relation given as data, and
an egroup, which is what we call a group over a setoid, has its group laws
holding up to that relation. This makes it possible to construct free groups
without function extensionality, propositional truncation, quotients or
univalence, in contrast with the construction in [Groups](#groups).

The free egroup on a setoid has the words on the generators as its
underlying type and convertibility as its equivalence relation. Two adjacent
letters cancel when the second is the inverse of the first up to the
relation of the generators, rather than only when they are equal, so that
two reducts of a word agree only up to that relation. Confluence has to be
proved modulo an equivalence relation, which is done for an abstract
reduction and then applied to words, and on this rests the universal
property, that a setoid map from the generators into an egroup extends along
the insertion of generators to a homomorphism, uniquely up to the
equivalence relation of that egroup.

Size is measured by the relation of a setoid rather than by its identity
type. As in
[Groups.Large](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Groups.Large.html),
the free egroup on a large setoid whose relation is small-valued is itself
large, in the sense that no egroup whose underlying type and relation are
both small is isomorphic to it. The example is the universe taken with type
equivalence as its relation, which has a small-valued relation with no
assumptions, since X ≃ Y already lives in the universe of X and Y, whereas
the identity type X ＝ Y is not small without something such as univalence.
That it is large follows from the generalization of Coquand's paradox of
trees in [Various.LawvereFPT](#variouslawverefpt), which uses Lawvere's
fixed point theorem and W-types to rule out a type of the universe that is
equivalent to the universe itself, and so, for any universe 𝓤, there is an
egroup in the next universe 𝓤⁺ that is isomorphic to no egroup in 𝓤.

By Martin Escardo.

[Table of contents](#table-of-contents)

### [Factorial](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Factorial.index.html)

The factorial of a type and its combinatorics are studied. The main result
is that, for an arbitrary type X,

co-derived-set (X + 𝟙) × Aut X ≃ Aut (X + 𝟙),

where Aut X is the type X ≃ X of automorphisms of X, and the co-derived set
of a type is its subtype of isolated points. When X is discrete, so that all
its points are isolated, this specializes to the factorial equivalence

(X + 𝟙) × Aut X ≃ Aut (X + 𝟙),

which is what gives the directory its name. When instead X is perfect,
having no isolated points, as the circle S¹ is, we get Aut X ≃ Aut (X + 𝟙).
A key ingredient is the left-cancellability of adding a single point, that
X + 𝟙 ≃ Y + 𝟙 gives X ≃ Y, which is proved constructively and without
function extensionality, together with the swap automorphism that exchanges
two isolated points. The main equivalence itself does assume function
extensionality, but neither propositional extensionality nor univalence.

By Martin Escardo.

[Table of contents](#table-of-contents)

### [Field](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Field.index.html)

Here the axioms for a field are given, in a formulation suitable for
constructive mathematics, and then those for an ordered field on top of
them. The axioms require the two identity elements to be apart rather than
merely different, with the apartness relation given as part of the
structure, being the negation of equality for the rationals and the
disjunction of the two strict inequalities for the Dedekind reals. The two
requirements agree classically, but it is apartness that one can reason with
constructively. The rationals are shown to satisfy the axioms, and the
intended verification for the Dedekind reals is begun but left unfinished.

By Andrew Sneap.

[Table of contents](#table-of-contents)

### [Fin](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Fin.index.html)

The standard finite types Fin n and their properties are developed,
including their role as the canonical types with exactly n elements. Three
notions of finiteness for arbitrary types are compared, namely those of
Bishop, Kuratowski and Dedekind. Whether every Kuratowski finite discrete
type can be linearly ordered is a question of Steve Vickers, asked for the
internal language of a 1-topos, and answered here in a different way. There
are also the pigeonhole principle,
choice for finite types, the discreteness and compactness of the types Fin
n, and a proof that addition and multiplication of natural numbers are
commutative which constructs equivalences of finite types instead of arguing
by induction. A finite type is shown to embed into the type of propositions
only if it has at most two elements, and such an embedding is an equivalence
precisely when it has exactly two and excluded middle holds.

By Martin Escardo.

[Table of contents](#table-of-contents)

### [Games](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Games.index.html)

The theory of finite, history-dependent games of perfect information is
developed using selection functions and quantifiers. A game is given by a
dependent type tree of moves, a type of outcomes, and a quantifier at each
node, and optimal strategies and subgame-perfect equilibria are computed by
products of selection functions, which is what connects game theory with
dependently-typed programming.

The dependent type trees the games are built on are closely related to
Aczel's W-type of constructive set theory, and are studied briefly in their
own right. There is a constructor for building games conveniently, an
alternative equivalent definition not yet used, notions of optimal move and
optimal play, and a computation of the list of all optimal plays of a game
in two ways.

Two reworkings generalize the theory by a monad parameter, applying the
selection monad transformer to it and requiring the outcomes to carry an
algebra, so that the definition of game is unchanged and the original
development is recovered when the parameter is the identity monad. The
monads in view are the powerset monad for the Herbrand functional
interpretation, probability distributions for mixed strategies, and the
reader monad for alpha-beta pruning, and a further aim is to consider
rational players playing against irrational ones. This needs affine monads,
which are available only on certain structured types, such as those with
decidable equality in the case of non-empty lists without repetitions, and
so the second reworking uses relative monads on structured types instead.
Both are experimental, and the authors record that they are not yet sure the
algebras model the intended notions.

Efficiency is a running concern. Tic-tac-toe appears in three variants, the
second built with the game constructor and the third more efficient but less
elegant, as the test case. Alpha-beta pruning is developed for minimax
games, those with alternating min and max quantifiers, in three stages. The
selection functions are pruned first, with the correctness of the resulting
optimal play left to be formulated. A game is then transformed so that its
optimal plays can be read off from the optimal outcomes of the transformed
game, and this is proved correct. Finally the transformation is itself
pruned, and here the correctness statement is written down but its proof is
left open. No efficiency theorems are proved either, although the tests
report the pruned version running eight times faster. A separate speed-up
computes a product of selection functions as a product of quantifiers, which
is also what the proof of the second stage rests on.

By Martin Escardo and Paulo Oliva.

**Publications.**

1. M.H. Escardó and P. Oliva, "Higher-order games with dependent types",
   Theoretical Computer Science 974, 2023, 114111, [doi:10.1016/j.tcs.2023.114111](https://doi.org/10.1016/j.tcs.2023.114111), [arXiv:2212.07735](https://arxiv.org/abs/2212.07735).

1. M.H. Escardó and P. Oliva, "Sequential games and optimal strategies",
   Proceedings of the Royal Society A 467, 2011, 1519–1545, [doi:10.1098/rspa.2010.0471](https://doi.org/10.1098/rspa.2010.0471).

[Table of contents](#table-of-contents)

### [Groups](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Groups.index.html)

Group theory is developed, with the type of groups and its basic properties,
subgroups, homomorphisms, kernels and images, quotients and cokernels, free
groups, and specific examples such as the symmetric groups and the modular
group. There are also group actions and torsors, automorphism groups, the
opposite group, and a development of large groups.

By Martin Escardo, Lane Biocini, Ettore Aldrovandi, Keri D'Angelo, Marc
Bezem, Thierry Coquand and Peter Dybjer.

[Table of contents](#table-of-contents)

### [Higgs](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Higgs.index.html)

Denis Higgs' involution theorem, that every monomorphism from the type Ω of
truth values to itself is an involution, is adapted to univalent
mathematics, together with a number of its consequences.

An automorphism of Ω is determined by its value at ⊤, in the sense that it
sends p to p ⇔ 𝕗 ⊤, and the type of automorphisms is equivalent to
[Johnstone](https://doi.org/10.1007/BF02488012)'s Higgs object ℍ, whose
elements are the widespread truth values, those r for which
((p ⇔ r) ⇔ r) ＝ p for every p. The main results of Johnstone and
[Freyd](https://doi.org/10.1016/0168-0072%2887%2990060-1) about
automorphisms of Ω are proved in this form. In particular ℍ, and hence Aut
Ω, has at most two elements, which seems to be due to Freyd, although the
proof given here is not his. Both a truncated and an untruncated form of the
at-most-two statement are given, the untruncated one being equivalent to
saying that Aut Ω has exactly one or two elements, so that every
automorphism is either the identity or negation. There is also a variant
showing that Aut Ω satisfies a form of weak excluded middle, in that an
automorphism is either equal to negation, in which case full excluded middle
holds, or not equal to it, and hence not not equal to the identity.

The second is that a group structure on Ω gives excluded middle, which
doesn't seem to be known in the topos theory community, and is the subject
of a [blog
post](https://homotopytypetheory.org/2021/01/23/can-the-type-of-truth-values-be-given-the-structure-of-a-group/).
Such a structure is necessarily abelian, and indeed any left-cancellable
monoid structure on Ω is an abelian group structure in which every element
is its own inverse.

The third concerns rigidity. A type is rigid when its only automorphism is
the identity, or, as one says in univalent mathematics, when its type of
automorphisms is contractible. The type Ω is not rigid in a boolean topos,
where it has exactly the identity and negation, and conversely, if there is
an automorphism of Ω other than the identity, then the topos is boolean.

By Martin Escardo and J. A. Carr.

[Table of contents](#table-of-contents)

### [InjectiveTypes](https://www.cs.bham.ac.uk/~mhe/TypeTopology/InjectiveTypes.index.html)

Injective types and their theory are developed in univalent foundations,
accompanying two papers, with a blackboard module in which the material was
worked out and an article module that follows the published account.

The central notions are algebraic injectivity and algebraic flabbiness, the
second being the working tool for establishing the first. Injective types
are closed under retracts, and are themselves the retracts of the
exponential powers of universes. A sufficient condition is given for
Σ x ꞉ X , A x to be algebraically flabby when X is, which subsumes an
earlier condition for types of mathematical structures and gives the
injectivity of the types of pointed types, ∞-magmas, pointed ∞-magmas and
monoids. The other examples found since the first paper are obtained
separately, the type of ordinals directly and also as a pointed dcpo, the
type of iterative multisets from prop-indexed sums and also from
prop-indexed products, the type of iterative sets as a retract of the
multisets, the type of non-empty types as a retract of the universe, and the
type of iterative ordinals from its equivalence with the ordinals.
Injectivity also plays a major role in the construction of compact, or
searchable, types.

Counterexamples are necessarily indirect. Excluded middle holds if and only
if every pointed type is algebraically injective, so no type other than the
empty one can be shown not to be injective, and what one does instead is
derive a constructive taboo from the injectivity of a type of interest. The
Dedekind reals are such a type, their injectivity giving weak excluded
middle. In the same vein, injective types have a non-trivial decidable
property if and only if weak excluded middle holds, which is where the
decomposability results of [Taboos](#taboos) come from.

Further strands are the characterization of the algebraically injective
types as the retracts of the algebras of the partial-map classifier monad,
injectivity over small maps, injectivity of subtypes and of pointed dcpos, a
proof that this notion of flabbiness agrees, for types that are sets, with
the one Blechschmidt gives for toposes, and resizing results showing that
the earlier theorems are tight in the universe levels and that no small type
with two distinct points is injective without Ω¬¬-resizing. Any map is also
factored as an embedding followed by one whose fibers are all algebraically
injective, with diagonal fillers for embeddings against such maps, though
the conclusion that these give a weak factorization system is so far argued
only in prose.

By Martin Escardo and Tom de Jong.

**Publications.**

1. M.H. Escardó, "Injective types in univalent mathematics", Mathematical
   Structures in Computer Science 31(1), 2021, 89–111, [doi:10.1017/S0960129520000225](https://doi.org/10.1017/S0960129520000225).

1. T. de Jong and M.H. Escardó, "Examples and counterexamples of injective
   types", 2026, [doi:10.48550/arXiv.2601.12536](https://doi.org/10.48550/arXiv.2601.12536).

[Table of contents](#table-of-contents)

### [Integers](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Integers.index.html)

The integers are constructed from the natural numbers, together with their
arithmetic and order, and further operations such as absolute value,
division, highest common factors, parity and exponentiation.

By Andrew Sneap and Lane Biocini.

[Table of contents](#table-of-contents)

### [Iterative](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Iterative.index.html)

Here iterative multisets, iterative sets and iterative ordinals are defined
using W-types, giving models of set theory and of the ordinals inside
univalent foundations. For the iterative sets the extensionality axiom holds
as a consequence of univalence, and the empty set, singletons, separation
and unions of small families are constructed, the unions requiring
propositional truncation and set replacement. The three layers are built one
on top of another, using Gylterud's construction of the cumulative hierarchy
𝕍, with the identifications between them worked out in detail.

By Martin Escardo, Tom de Jong and Alice Laroche.

**Publication.**

1. T. de Jong, N. Kraus, F. Nordvall Forsberg and C. Xu, "Set-Theoretic and
   Type-Theoretic Ordinals Coincide", LICS 2023, [doi:10.1109/LICS56636.2023.10175762](https://doi.org/10.1109/LICS56636.2023.10175762), [arXiv:2301.10696](https://arxiv.org/abs/2301.10696).

[Table of contents](#table-of-contents)

### [Lifting](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Lifting.index.html)

The lifting monad, also known as the partial-map classifier monad, is
developed, its value at a type X being the type of partial elements of X,
each given by a proposition together with a map from it into X. The
propositions are all those of a chosen universe, the variant that restricts
them by a dominance being in [Dominance](#dominance), and the sense in which
the lifting is free, as the free pointed dcpo on a set, belonging to
[DomainTheory](#domaintheory). Its algebras are studied, its identity types
are characterized both directly and via the structure identity principle,
size issues are addressed, and it is organized as a univalent wild category,
with several results on free algebras.

By Martin Escardo and Tom de Jong.

[Table of contents](#table-of-contents)

### [Locales](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Locales.index.html)

This is a constructive and predicative development of point-free topology in
univalent foundations, accompanying the PhD thesis of Ayberk Tosun. Alongside a
general theory of locales in UF, it develops the theory of spectral and Stone
locales as well as the point-free topology of Scott domains. The development
uses function extensionality, propositional truncation, and set replacement
whilst avoiding both excluded middle and propositional resizing. Due to the
predicative nature of the foundational setting, the category of locales
considered is that of large, locally small, and small-complete locales. This
requires suitable reformulations of many established definitions of locale
theory, which is a key contribution of this development.

The project began with the goal of constructing the patch locale of a spectral
locale in univalent foundations, building on Escardó’s characterization of it as
the frame of Scott-continuous nuclei. Achieving this required a substantial
development of general point-free topology and the work has thus expanded into a
broader study of locale theory in univalent foundations. Salient topological
notions developed include compactness, the way-below relation, clopens, the
well-inside relation, regularity, zero-dimensionality, bases (especially small
bases), sublocales, the patch topology (in localic form), and Stone duality.
Salient examples of locales studied in this development include the terminal
locale, the Sierpiński locale, the discrete locale, and the Scott locale of an
algebraic DCPO.

A further strand of work is on the point-free topology of domains. This uses Tom
de Jong's development of domain theory and connects the two TypeTopology
developments via the Scott topology. Key constructions and theorems include the
Scott locale of an algebraic DCPO, the spectrality of the Scott locale of a
Scott domain (involving nontrivial base constructions in the predicative
setting), and the points of the patch of the Scott locale of a Scott domain. The
Sierpiński locale is also constructed as the Scott locale of the Sierpiński
DCPO.

By Ayberk Tosun.

**Publications.**

1. A. Tosun, "Constructive and Predicative Locale Theory in Univalent
   Foundations", PhD thesis, University of Birmingham, 2025, <https://etheses.bham.ac.uk/id/eprint/16416/>, [arXiv:2603.01308](https://arxiv.org/abs/2603.01308).

1. A. Tosun and M.H. Escardó, "Patch Locale of a Spectral Locale in Univalent
   Type Theory", MFPS XXXVIII, Electronic Notes in Theoretical Informatics
   and Computer Science 1, 2023, [doi:10.46298/entics.10808](https://doi.org/10.46298/entics.10808).

1. I. Arrieta, M.H. Escardó and A. Tosun, "The Patch Topology in Univalent
   Foundations", Mathematical Structures in Computer Science 35, 2025, [doi:10.1017/S0960129525000088](https://doi.org/10.1017/S0960129525000088).

[Table of contents](#table-of-contents)

### [MetricSpaces](https://www.cs.bham.ac.uk/~mhe/TypeTopology/MetricSpaces.index.html)

Metric spaces are developed in constructive univalent foundations without
mentioning the real numbers. Instead of a distance function taking values in
the reals, a metric space is given here by a relation saying that two points
are within ε of each other for a positive rational ε, subject to the
requirements that points within every ε are equal, that the relation is
reflexive, symmetric and monotone in ε, and that being within ε₁ and then
within ε₂ gives being within ε₁ + ε₂. Cauchy sequences, convergent sequences
and completeness are defined in these terms, and the rationals and the
Dedekind reals are shown to be instances. The standard definition using the
reals is given separately, for comparison with this one.

By Andrew Sneap and Tom de Jong.

[Table of contents](#table-of-contents)

### [MGS](https://www.cs.bham.ac.uk/~mhe/TypeTopology/MGS.index.html)

This is a modular version of the HoTT/UF in Agda lecture notes, providing a
more principled and self-contained introduction to the univalent foundations
used in the rest of the repository. It covers the standard toolkit, namely
MLTT, h-levels, equivalences, univalence and its consequences, embeddings,
the powerset, quotients, the SIP and the Yoneda lemma, together with
exercises and their solutions.

By Martin Escardo.

**Publication.**

1. M.H. Escardó, "Introduction to Univalent Foundations of Mathematics with
   Agda", 2019, [doi:10.48550/arXiv.1911.00580](https://doi.org/10.48550/arXiv.1911.00580), <https://github.com/martinescardo/HoTT-UF-Agda-Lecture-Notes>.

[Table of contents](#table-of-contents)

### [MLTT](https://www.cs.bham.ac.uk/~mhe/TypeTopology/MLTT.index.html)

Here is the Spartan Martin-Löf type theory that is the foundation of the
whole development, with universes, the empty and unit types, sums, Σ-types
and Π-types, the identity type, the natural numbers, and the basic notation
built on them. The Spartan module gathers the core, with further modules for
lists, vectors and finite types and a slightly larger Athenian selection.

By Martin Escardo, Ayberk Tosun, Tom de Jong, Fredrik Nordvall Forsberg and
Carlo Angiuli.

[Table of contents](#table-of-contents)

### [Modal](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Modal.index.html)

Reflective subuniverses and modalities in homotopy type theory are treated,
roughly following [Rijke, Shulman and
Spitters](https://doi.org/10.23638/LMCS-16%281:2%292020) on modalities and
[Rijke's thesis](https://arxiv.org/abs/1906.09435), on whose proofs much of
the treatment of reflective subuniverses is based. Subuniverses, reflective
subuniverses and their Σ-closed, or modal, versions are developed, with the
truncation and open modalities as examples, and with the closure of the
modal types under pullbacks and identity types.

By Jon Sterling and Andrew Swan.

[Table of contents](#table-of-contents)

### [MonadOnTypes](https://www.cs.bham.ac.uk/~mhe/TypeTopology/MonadOnTypes.index.html)

Wild monads on types are developed, carrying a universe-level transformer so
that the value of a monad may live in a higher universe than its argument, as
for the powerset monad, whose value on a type in 𝓤 lands in 𝓤⁺. The monad
laws are imposed, as identifications, and the monads are wild in that no
coherence conditions in the sense of HoTT/UF or higher category theory are
imposed on these identifications. The general definition is instantiated at
the selection monad J, the continuation monad K and their interaction, the
list and non-empty-list monads, and the reader monad, and there is a
selection-monad transformer, in a basic and a more general variant.

Every monad in this sense is automatically strong, with a tensor
operation constructed from the monad structure rather than given as
additional data.

Some results need the extension operation to send a constant function
to the constant function with the same value, and Ohad Kammar pointed
out that this amounts to the affineness of the monad, in the sense
that its unit at the type 𝟙 is an equivalence, and a proof of this is
included.

By Martin Escardo and Paulo Oliva.

[Table of contents](#table-of-contents)

### [Naturals](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Naturals.index.html)

The natural numbers and their elementary number theory are built up, with
addition, multiplication and exponentiation, order, division and highest
common factors, parity, a binary representation, and truncation principles
for finding roots and least elements, together with the universal property
of ℕ.

By Martin Escardo, Andrew Sneap, Lane Biocini, Tom de Jong, Chuangjie Xu and
Fredrik Nordvall Forsberg.

[Table of contents](#table-of-contents)

### [Notation](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Notation.index.html)

The general notation and conventions used throughout the development are
collected, so that the same symbols and naming schemes are available
uniformly across the other directories. It has general and order notation,
canonical maps between types, underlying-type projections, and decimal
literals.

By Martin Escardo, Ian Ray and Lane Biocini.

[Table of contents](#table-of-contents)

### [NotionsOfDecidability](https://www.cs.bham.ac.uk/~mhe/TypeTopology/NotionsOfDecidability.index.html)

Various (closure) properties of decidable types are discussed. The
type 𝟚 of booleans is shown to classify complemented subsets.

In addition, semidecidable and quasidecidable propositions are studied.
A proposition P is semidecidable if there exists a binary sequence such that P is
equivalent to the statement that the sequence has a 1 somewhere. The
constructive taboos LPO, Markov's Principle and strong Brouwer-Kripke-Schema are
related to closure and embedding properties of the type of semidecidable
propositions. Closure under Σ and countable joins are related to (weak) choice
axioms, partly following Escardó–Knapp.
Motivated by the lack of countable joins (in general) for semidecidable
propositions, the quasidecidable propositions are defined as the least
collection of types (which happen to be propositions) closed under the empty
type, the unit type and ℕ-indexed existential quantification. It seems this
collection is not definable without higher inductive types or propositional
resizing. It is shown that the quasidecidable propositions form a dominance. The
existence of the type of quasidecidable propositions is related to the existence
of the initial σ-frame and the free σ-sup-lattice on one generator.

By Martin Escardo and Tom de Jong.

[Table of contents](#table-of-contents)

### [OrderedTypes](https://www.cs.bham.ac.uk/~mhe/TypeTopology/OrderedTypes.index.html)

Various ordered structures are defined, such as posets, frames, σ-frames,
σ-sup-lattices, join-semilattices, and sup- and inf-lattices. There are also
related constructions, such as the poset reflection of a preorder, the powerset
as the free sup-lattice, and the Kuratowski finite subsets as the free
join-semilattice.

The main theorems of Ch. 6 of Tom de Jong's thesis involving propositional
resizing and the technical notion of δ-complete poset can be found here too.
A type-theoretic account of work by Giovanni Curi, due to Ian Ray and
accompanying his paper referenced below, is part of the development. This
account is instantiated in the presence of propositional resizing to obtain a
generalization of Tarski's least fixed point theorem, namely one for endomaps on
a large sup-lattice with a small basis.
Finally, the proof that the axiom of choice implies Zorn's lemma is included.

By Ian Ray, Tom de Jong, Martin Escardo and Kelton OBrien.

**Publications.**

1. T. de Jong and M.H. Escardó, "Predicative Aspects of Order Theory in
   Univalent Foundations", FSCD 2021, LIPIcs 195, [doi:10.4230/LIPIcs.FSCD.2021.8](https://doi.org/10.4230/LIPIcs.FSCD.2021.8).

1. T. de Jong and M.H. Escardó, "On Small Types in Univalent Foundations",
   Logical Methods in Computer Science 19(2), 2023,
   [doi:10.46298/lmcs-19(2:8)2023](https://doi.org/10.46298/lmcs-19%282:8%292023), [arXiv:2111.00482](https://arxiv.org/abs/2111.00482), which is the revised and expanded
   version of the above.

1. I. Ray, "Tarski's least fixed point theorem: A predicative type theoretic
   formulation", 2024, [doi:10.48550/arXiv.2401.00841](https://doi.org/10.48550/arXiv.2401.00841).

1. The free join- and sup-lattice constructions also accompany T. de Jong's
   PhD thesis, cited under [DomainTheory](#domaintheory) above.

[Table of contents](#table-of-contents)

### [Ordinals](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Ordinals.index.html)

The theory of ordinals is developed in univalent foundations, where an
ordinal is a type equipped with a well-founded, extensional and transitive
order. By univalence, the ordinals of a universe themselves form an ordinal
in the next universe, which is large but locally small, and it is
algebraically injective.

The arithmetic comprises addition, multiplication and exponentiation and
their properties, together with bounded operations, suprema and sums, and
variants of these for the topped and the trichotomous ordinals. It is
noteworthy that the infimum of a merely inhabited family of ordinals is
constructed using propositional truncation and univalence alone, the
construction staying small by an observation of Christian Sattler, whereas
the known constructions of suprema need set quotients or, equivalently, set
replacement.

Exponentiation has a subdirectory of its own. It is specified first, then
constructed abstractly using suprema and concretely using decreasing lists,
and the two constructions are shown to agree when the base has a
trichotomous least element, which happens exactly when the base is of the
form 𝟙 + α for some ordinal α. Robin Grayson's variant of the decreasing
list construction is implemented and shown not to give an ordinal in
general. Alongside this is the abstract cancellation arithmetic of de Jong,
Kraus, Nordvall Forsberg and Xu, in which the maps α + −, α × − and exp α −
are proved to reflect the order and the identity.

Several classically true statements about ordinals are taboos here, in that
each of them implies excluded middle. Shulman observed that this is so if
every subset of an ordinal is an ordinal. Following Swan, it is so if every
set can be inductively well-ordered, and again if every discrete ordinal is
trichotomous. Trichotomy and total separatedness both fail in general. The
inductive well-ordering principle is in fact equivalent to the axiom of
choice, which gives that every set can be well-ordered, and conversely. The
Burali-Forti argument is used to show that the embedding of a universe into
its successor is not an equivalence, and likewise for the types of sets,
magmas, monoids and groups.

Sums of ordinal-indexed families are constructed with the lexicographic
order for families indexed by an ordinal with a top element, and it is
Shulman's taboo that justifies restricting to the topped ordinals, the
obstruction in general being the extensionality of the lexicographic order
on the sum.

The set-theoretic reading is developed alongside. Inside the cumulative
hierarchy 𝕍 the set-theoretic ordinals are the transitive sets of transitive
sets, and this subtype is shown to coincide with the type-theoretic
ordinals.

Ordinals are also presented syntactically, by Brouwer codes and by other
notation systems, each with its interpretation. Among the concrete ordinals
there are the ordinal of truth values, the ordinals below ω given by Fin, a
Church encoding, and the conatural numbers ℕ∞. A supremum of a
compact-indexed family of compact ordinals is compact, and the lexicographic
order gives further compactness results. There is also machinery for
transporting and extending well-orders and for identifying equivalent
ordinals.

By Martin Escardo, Tom de Jong, Fredrik Nordvall Forsberg, Nicolai Kraus,
Chuangjie Xu, Andrew Swan, Alice Laroche, Ohad Kammar, Marc Bezem, Thierry
Coquand and Peter Dybjer.

**Publications.**

1. M.H. Escardó, "Compact, totally separated and well-ordered types in
   univalent mathematics", abstract, TYPES 2019, Oslo, <https://eutypes.cs.ru.nl/pmwiki/uploads/Main/books-of-abstracts-TYPES2019.pdf>, for the notation
   systems for discrete and compact ordinals and their interpretations.

1. T. de Jong, N. Kraus, F. Nordvall Forsberg and C. Xu, "Set-Theoretic and
   Type-Theoretic Ordinals Coincide", LICS 2023, [doi:10.1109/LICS56636.2023.10175762](https://doi.org/10.1109/LICS56636.2023.10175762), [arXiv:2301.10696](https://arxiv.org/abs/2301.10696).

1. T. de Jong, N. Kraus, F. Nordvall Forsberg and C. Xu, "Ordinal
   Exponentiation in Homotopy Type Theory", LICS 2025, [doi:10.1109/LICS65433.2025.00027](https://doi.org/10.1109/LICS65433.2025.00027).

1. T. de Jong, N. Kraus, F. Nordvall Forsberg and C. Xu, "Constructive
   Ordinal Exponentiation", [arXiv:2501.14542](https://arxiv.org/abs/2501.14542), the journal version of the
   above.

[Table of contents](#table-of-contents)

### [PathSequences](https://www.cs.bham.ac.uk/~mhe/TypeTopology/PathSequences.index.html)

This is a library for manipulating sequences of paths, providing a calculus
for reassociating and reversing concatenations, ported from the [HoTT-Agda
library](https://github.com/HoTT/HoTT-Agda). The operations include
concatenation, application of functions, cancellation, inversion, rotation
and splitting, with an equational-reasoning interface.

By Ettore Aldrovandi.

[Table of contents](#table-of-contents)

### [PCF](https://www.cs.bham.ac.uk/~mhe/TypeTopology/PCF.index.html)

The programming language PCF is developed in two presentations, one
combinatory and the other based on the lambda calculus, each with its
operational and denotational Scott semantics. For the lambda-calculus
presentation the Scott model is proved computationally adequate. For the
combinatory presentation adequacy is not formalized here, having been proved
by Tom de Jong in UniMath instead. Each presentation has its own
subdirectory and index.

By Brendan Hart, Tom de Jong and Martin Escardo.

**Publications.**

1. T. de Jong, "The Scott model of PCF in univalent type theory",
   Mathematical Structures in Computer Science 31(10), 2021,
   [doi:10.1017/S0960129521000153](https://doi.org/10.1017/S0960129521000153).
   The Scott model it reports is the one in
   [DomainTheory](#domaintheory), under which this paper is also listed.

1. B. Hart, "Investigating Properties of PCF in Agda", MSci dissertation,
   University of Birmingham, 2020, <https://github.com/BrendanHart/Investigating-Properties-of-PCF>.

[Table of contents](#table-of-contents)

### [Quotient](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Quotient.index.html)

Set quotients are studied, starting from an axiomatization of them.
Effectivity is not required as part of that axiomatization but is derived
from it, in the presence of function extensionality and propositional
extensionality. The existence of set quotients is interderivable with set
replacement, and, given function extensionality, set quotients give
propositional truncations, while conversely propositional truncations
together with function and propositional extensionality give quotients that
are large, living in a higher universe than the type quotiented and needing
no resizing. A variation of that construction controls the universe in which
the assumed truncations live.

By Martin Escardo and Tom de Jong.

[Table of contents](#table-of-contents)

### [Rationals](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Rationals.index.html)

The rational numbers are constructed from the integers via fractions,
together with their arithmetic, order, absolute value, min and max,
positivity, and a notion of limit.

By Andrew Sneap.

[Table of contents](#table-of-contents)

### [ReflexiveGraphs](https://www.cs.bham.ac.uk/~mhe/TypeTopology/ReflexiveGraphs.index.html)

Reflexive graphs and reflexive graph lenses are developed, following
Sterling, as a modular approach to the structure identity principle. Lenses
provide a generic notion of transport, giving reusable characterizations of
identity, illustrated by several examples. Reflexive graphs, their displayed
and univalent versions, biased and unbiased lenses, and univalent closure
properties are developed in turn.

The primary source is J. Sterling, "Reflexive graph lenses in univalent
foundations", Mathematical Structures in Computer Science 36, 2026, article
e21, [doi:10.1017/S0960129526100565](https://doi.org/10.1017/S0960129526100565).

By Ian Ray.

[Table of contents](#table-of-contents)

### [Relations](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Relations.index.html)

The basic theory of relations is set out, including their standard
properties and constructions such as closures, used throughout the
development. It provides the symmetric-reflexive-transitive closure of a
relation and an abstract Church–Rosser property, which is reused, for
instance, in the free-group construction.

By Martin Escardo.

[Table of contents](#table-of-contents)

### [RelativeMonadOnStructuredTypes](https://www.cs.bham.ac.uk/~mhe/TypeTopology/RelativeMonadOnStructuredTypes.index.html)

Relative monads on structured types are developed, motivated by applications
to combinatorial game theory, which need monads that are affine, in the
sense that the unit 𝟙 → T 𝟙 is an isomorphism. The list monad is not affine,
but the non-empty lists without repetitions are, and to work with those one
needs decidable equality on the type of entries. This is what makes the
monad relative. Decidable equality on X is needed in order to form T X, but
T X is not required to have decidable equality in turn, so T is not an
endofunctor, and the monad is given instead by a unit and an extension
operator, following Altenkirch, Chapman and Uustalu. The structure
considered is required to be closed under 𝟙 and Σ, and the definition
carries a universe-level transformer, so that examples such as the non-empty
powerset, which raise the universe level, are covered as well. There is also
a monad transformer sending T to JT X = (X → T R) → T X.

By Martin Escardo and Paulo Oliva.

[Table of contents](#table-of-contents)

### [Slice](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Slice.index.html)

The slice of a universe over a type is presented as families, together with
its monad structure, the corresponding algebras, an embedding into the
universe, and a characterization of its identity types via the structure
identity principle. This is the family fibration presentation, closely
related to the lifting monad.

By Martin Escardo, Ayberk Tosun, Ian Ray and Tom de Jong.

[Table of contents](#table-of-contents)

### [SyntheticHomotopyTheory](https://www.cs.bham.ac.uk/~mhe/TypeTopology/SyntheticHomotopyTheory.index.html)

Two types of interest for homotopy theory are defined. The first is the infinite
dimensional real projective space ℝP∞. Justified by a paper by Ulrik Buchholtz
and Egbert Rijke, the simple definition as the connected component of the
booleans is adopted.
The second is the (homotopy) circle S¹. Following a paper by Marc Bezem, Ulrik
Buchholtz, Dan Grayson and Mike Shulman, it is constructed as the type of
ℤ-torsors.

See also
[SyntheticHomotopyTheory.Circle.FundamentalGroup](#synthetichomotopytheorycirclefundamentalgroup)
and
[SyntheticHomotopyTheory.Circle.WithRewriting](#synthetichomotopytheorycirclewithrewriting).

By Tom de Jong.

[Table of contents](#table-of-contents)

### [Taboos](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Taboos.index.html)

The non-constructive principles that mark the boundary of constructive
reasoning are collected here, chiefly excluded middle and the
omniscience principles of Bishop, together with statements that are
shown to be constructive taboos in the sense of Aczel by reducing them
to such principles.

The omniscience principles come first. LPO is the compactness of ℕ,
that is, for every binary sequence either some term is 0 or all of
them are 1, and it is treated both in this form, which is not a
proposition because there may be many such terms, and in its truncated
form. WLPO is stated here as saying that every element of the type ℕ∞
of conatural numbers is ∞ or not, and this is proved equivalent to the
traditional formulation, that it is decidable whether a binary
sequence is constantly 1. Markov's principle is here too, with the
fact that it and WLPO together give LPO. LPO and WLPO are independent,
holding in the model of classical sets and failing in recursive
models. LLPO is stated with disjunction, and its untruncated version,
with + in place of disjunction ∨, implies WLPO and is an instance of
De Morgan's Law, whereas the truncated one is known not to imply it.

Then come taboos of a more topological flavour. A function ℕ∞ → 𝟚 that takes
the value 0 at every finite element and the value 1 at ∞ gives WLPO.
Equivalently, it is a taboo that the constant sequence 0 converges to the
number 1 in the binary numbers, which a Brouwerian continuity axiom, not
postulated here, would rule out by requiring every convergent sequence of
binary numbers to be eventually constant. The type of ordinals is
decomposable as a disjoint union of two pointed types if and only if weak
excluded middle holds, so that it has no non-trivial decidable property
unless the taboo holds, and the same is later shown for injective types,
which subsumes it since the type of ordinals is injective. There are three
versions of the drinker paradox, one of which is equivalent to excluded
middle, a taboo about Kuratowski-finite subsets, namely that if every subset
of a Kuratowski-finite subset of a set is again Kuratowski-finite then the
set is discrete, and a study of when the constant map 𝟚 → (X → 𝟚) is an
equivalence, a property called thin inhabitedness which is stronger than
nonemptiness precisely because weak excluded middle is not decided.

By Martin Escardo, Ayberk Tosun and Tom de Jong.

The decomposability development draws on the two papers of T. de Jong and
M.H. Escardó listed under [OrderedTypes](#orderedtypes) above.

[Table of contents](#table-of-contents)

### [TWA](https://www.cs.bham.ac.uk/~mhe/TypeTopology/TWA.index.html)

Todd Waugh Ambridge's thesis and related work are kept here. The thesis
subdirectory is organized by chapter, and each chapter of the index links to
the corresponding part of the thesis itself.

The two notions it turns on are searchability and uniform continuity. Both
are formulated on closeness spaces, a convenient version of ultrametric
spaces in which the closeness of two points is a conatural number, maximal
exactly when the points are equal, and satisfying an ultrametric condition
relating the closeness of x and z to those of x and y and of y and z. A map
is uniformly continuous when for every precision ϵ there is a precision δ
such that δ-close points are sent to ϵ-close points, and it is this δ,
available explicitly rather than merely existing, that makes search
possible. There are also pseudocloseness spaces, which drop the requirement
that indistinguishable points be equal, and a version of the totally bounded
property. Building on earlier work of Escardo, certain infinite types are
then searched by exploiting the modulus explicitly, and the key technical
result is that uniformly continuously searchable types are closed under
countable products.

On top of this, global optimization and parametric regression are stated and
proved to converge for a wide class of types. What makes this possible is
the notion of an approximate linear preorder, which orders the elements of a
closeness space only up to a given precision, so that the optimization and
regression statements become type-theoretic and their proofs follow from the
framework rather than from further analysis.

Two representations of the real numbers are then given, ternary signed
digits and ternary Boehm encodings. For the first, negation, binary and
infinitary midpoint, and multiplication are verified against the
Escardo-Simpson axiomatization of the closed interval, which is itself
formalized here, along with a structure identity principle for midpoint
algebras, convex bodies and interval objects. For the second, the type is
defined and its structure proved correct, and it is shown to represent
compact intervals that can then be searched. The framework is finally
instantiated on both, and the resulting algorithms are run on examples.

Outside the thesis there are the closeness function on the Baire, Cantor and
conatural types, and a Banach fixed-point theorem for ultracloseness
spaces. The dyadic rationals and dyadic reals that the thesis uses are
contributed by Andrew Sneap, and are marked in his files as incomplete.

By Todd Waugh Ambridge, Andrew Sneap and Martin Escardo.

**Publications.**

1. T. Waugh Ambridge, "Exact Real Search: Formalised Optimisation and
   Regression in Constructive Univalent Mathematics", PhD thesis, University
   of Birmingham, 2024, [doi:10.48550/arXiv.2401.09270](https://doi.org/10.48550/arXiv.2401.09270).

1. D.R. Ghica and T. Waugh Ambridge, "Global Optimisation with Constructive
   Reals", LICS 2021, [doi:10.1109/LICS52264.2021.9470549](https://doi.org/10.1109/LICS52264.2021.9470549).

1. M.H. Escardó and A. Simpson, "A universal characterization of the closed
   Euclidean interval", LICS 2001, pp. 115–125, [doi:10.1109/LICS.2001.932488](https://doi.org/10.1109/LICS.2001.932488), formalized by the
   interval-object module.

[Table of contents](#table-of-contents)

### [TypeTopology](https://www.cs.bham.ac.uk/~mhe/TypeTopology/TypeTopology.index.html)

Here we have the topological view of types after which the repository is
named. The two should not be confused. TypeTopology is the repository, of
which this is one directory among 61, and it is the one where the
topological view itself is developed. Types are treated as though they
carried an intrinsic topology, so that notions such as compactness, in the
sense of exhaustive searchability, discreteness, total separatedness,
disconnectedness, sequential Hausdorffness and the structure of the Cantor
type can be studied, along with the ways in which they interact. Concretely
this includes compact, or exhaustively searchable, types and their closure
properties, the generic convergent sequence and the Cantor type, total
separatedness, weakly compact types, squashed sums, Rice's theorem for the
universe, and the indiscreteness of the universe.

Not only is the generic convergent sequence compact, but minimal witnesses
can be found. The totally separated reflection is constructed in two ways,
as the image of the evaluation map into ((X → 𝟚) → 𝟚) and as a set quotient.
The Cantor type is searchable for uniformly continuous decidable predicates,
and more generally so is ℕ → X for any compact X. For any function ℕ∞ → ℕ it
is decidable whether it fails to be continuous, and for any function ℕ∞ → 𝟚
it is decidable whether it takes the value 1 at every finite element. The
simple types, generated from ℕ by function types, all have ℕ as a retract,
so none of them is 𝟚-compact unless WLPO holds. A product of pointed compact
types indexed by a proposition is compact, whereas assuming this for compact
types that are not pointed gives weak excluded middle. Compactness is
upwards absolute for modalities, a type compact in the internal logic of a
reflective subuniverse being compact as a type, though not conversely. Sums
do not preserve total separatedness, and the compact ordinals are
nevertheless shown to be totally separated by exhibiting them as retracts of
the Cantor type, which suffices because total separatedness is inherited by
retracts. The decreasing sequences of natural numbers bounded by a fixed
number form a Stone type, being both compact and totally separated. The
Cantor type with a point removed, in the sense of the subtype of points
apart from it, is isomorphic to ℕ × (ℕ → 𝟚). A point is a limit point when
its being isolated would imply WLPO, a formulation chosen to stay agnostic
about classical principles, since under excluded middle every point of a set
is isolated. Crucially, we don't assume continuity axioms so that all
results hold in all toposes.

By Martin Escardo, Andrew Swan, Fredrik Bakke, Chuangjie Xu and Ayberk
Tosun.

**Publications.**

1. M.H. Escardó, "Infinite sets that admit fast exhaustive search", LICS
   2007, 443–452, [doi:10.1109/LICS.2007.25](https://doi.org/10.1109/LICS.2007.25).

1. M.H. Escardó, "Exhaustible sets in higher-type computation", Logical
   Methods in Computer Science 4(3:3), 2008,
   [doi:10.2168/LMCS-4(3:3)2008](https://doi.org/10.2168/LMCS-4%283:3%292008).

1. M.H. Escardó, "Infinite sets that satisfy the principle of omniscience in
   any variety of constructive mathematics", Journal of Symbolic Logic 78(3),
   2013, 764–784, [doi:10.2178/jsl.7803040](https://doi.org/10.2178/jsl.7803040).

1. M.H. Escardó, "Constructive decidability of classical continuity",
   Mathematical Structures in Computer Science 25(7), 2015, 1578–1589, [doi:10.1017/S096012951300042X](https://doi.org/10.1017/S096012951300042X).

1. M.H. Escardó and T. Streicher, "The intrinsic topology of Martin-Löf
   universes", Annals of Pure and Applied Logic 167(9), 2016, 794–805, [doi:10.1016/j.apal.2016.04.010](https://doi.org/10.1016/j.apal.2016.04.010).

1. M.H. Escardó, "Compact, totally separated and well-ordered types in
   univalent mathematics", abstract, TYPES 2019, Oslo, <https://eutypes.cs.ru.nl/pmwiki/uploads/Main/books-of-abstracts-TYPES2019.pdf>.

[Table of contents](#table-of-contents)

### [UF](https://www.cs.bham.ac.uk/~mhe/TypeTopology/UF.index.html)

Here is the core HoTT/UF library on which the rest of the development rests,
developed on demand over many years. Of the other 59 directories, all but
Notation and InfinitePigeon import it, and only MLTT, which every one of
them imports, is more widely used.

The axioms are defined here as types rather than postulated, namely function
extensionality in several equivalent forms, propositional extensionality,
the existence of propositional truncations, univalence, propositional
resizing, excluded middle and choice, and they are taken as explicit
assumptions wherever they are used, so that each theorem elsewhere names
exactly what it needs. Several equivalent formulations of the axiom of
choice are given, one of which seems to be new, along with its relation to
the double-negation shift, a pre-univalence axiom due to Cavallo and
Lumsdaine, and a derivation of function extensionality from a generalization
of univalence taken from Cory Knapp's thesis.

On this rest equivalences and embeddings, subsingletons, sets and h-levels,
Hedberg's theorem, discrete and ¬¬-separated types, the structure identity
principle with its examples, identity systems, the subtype and other
classifiers, the powerset in variants differing in how they treat universes
and resizing, together with its Kuratowski-finite subsets, image and
surjection, size and resizing, the Yoneda machinery with the embedding
Id : X → (X → 𝓤), the cumulative hierarchy, and a semistrict identity type
whose composition is definitionally associative and unital. There are also
general truncations defined by records, homotopy pullbacks, pushouts,
sequential colimits, connected types and the axiom of replacement.

A type is collapsible when it has a weakly constant endomap. Kraus's lemma,
that the fixed points of such an endomap form a proposition, holds in pure
Martin-Löf type theory, and gives a propositional truncation of any
collapsible type that one can exit, obtaining a point of the type. A family
indexed by a proposition has its product and its sum equivalent to the fibre
over any point of the index, while over an empty index the product is the
unit type and the sum is the empty type. Groupoids are defined directly
rather than as the types of h-level two, which keeps their basic theory free
of univalence, and the two definitions are proved to agree when univalence is
assumed. Univalence transports a structure along an equivalence, and this
transport is characterised by acting as the identity at the identity
equivalence, so any explicitly defined operation with that property agrees
with it and is easier to compute with.

Under univalence any universe embeds into any larger one, which has to be
proved because the type theory used here has no cumulativity. Local smallness
has a version graded by truncation level, which is closed under truncation
and strong enough that requiring it of all truncated types gives
propositional resizing. Smallness is closed under equivalence and under Σ,
and under Π given function extensionality. Small maps are closed under
composition, and a decidable embedding is small with respect to every
universe, as is the embedding Id : X → (X → 𝓤) under univalence, although its
codomain lies in a larger universe.

By Martin Escardo, Ian Ray, Tom de Jong, Cory Knapp, Jon Sterling, Ayberk
Tosun, Nicolai Kraus, Fredrik Nordvall Forsberg, Chuangjie Xu, Anna Williams,
Fredrik Bakke, Carlo Angiuli, Ettore Aldrovandi, Marc Bezem, Thierry Coquand
and Peter Dybjer.

**Publications.**

1. N. Kraus, M.H. Escardó, T. Coquand and T. Altenkirch, "Generalizations of
   Hedberg's Theorem", TLCA 2013, Lecture Notes in Computer Science 7941,
   Springer, [doi:10.1007/978-3-642-38946-7_14](https://doi.org/10.1007/978-3-642-38946-7_14).

1. N. Kraus, M.H. Escardó, T. Coquand and T. Altenkirch, "Notions of
   Anonymous Existence in Martin-Löf Type Theory", Logical Methods in
   Computer Science 13(1), 2017, [doi:10.23638/LMCS-13(1:15)2017](https://doi.org/10.23638/LMCS-13%281:15%292017).

1. T. de Jong and M.H. Escardó, "On Small Types in Univalent Foundations",
   Logical Methods in Computer Science 19(2), 2023,
   [doi:10.46298/lmcs-19(2:8)2023](https://doi.org/10.46298/lmcs-19%282:8%292023), for the material on size and resizing.

[Table of contents](#table-of-contents)

### [W](https://www.cs.bham.ac.uk/~mhe/TypeTopology/W.index.html)

W-types are the types of well-founded trees, which serve as a general scheme
of inductive types and underlie several other developments, such as the
iterative sets. The type is given with its properties, a characterization of
its identity types, and an encoding of the natural numbers as a W-type.

By Martin Escardo.

[Table of contents](#table-of-contents)

### [WildCategories](https://www.cs.bham.ac.uk/~mhe/TypeTopology/WildCategories.index.html)

Wild higher categories, that is, categories without imposed coherence
conditions, are developed, with the arguments due to Mike Shulman and typed
into Agda by Jon Sterling. The current material sets up the basic notions,
cones, and the splitting of idempotents.

By Jon Sterling and Mike Shulman.

[Table of contents](#table-of-contents)

### [deprecated](https://www.cs.bham.ac.uk/~mhe/TypeTopology/deprecated.index.html)

Modules kept for reference or historical interest live here, superseded by
material elsewhere but retained so that older results and links remain
available. It currently holds earlier accounts of categories and of the structure
identity principle, and a first construction of free groups over setoids,
superseded by [EGroups](#egroups).

By Martin Escardo and Jon Sterling.

[Table of contents](#table-of-contents)

### [Various](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Various.index.html)

Miscellaneous results of interest that do not belong naturally to any
of the other directories are collected here.

By Martin Escardo, Tom de Jong, Alice Laroche, Evan Cavallo, Jon Sterling
and Ingo Blechschmidt.

[Table of contents](#table-of-contents)

#### [Various.CantorTheoremForEmbeddings](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Various.CantorTheoremForEmbeddings.html)

Cantor's theorem is proved for embeddings of the powerset of a type into the
type itself, following Taylor's Practical Foundations of Mathematics by way
of [the nLab](https://ncatlab.org/nlab/show/Cantor%27s+theorem). It applies
Cantor's theorem for surjections, proved in
[Various.LawvereFPT](#variouslawverefpt), and uses function extensionality,
propositional extensionality and propositional resizing.

By Jon Sterling.

[Table of contents](#table-of-contents)

#### [Various.Dedekind](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Various.Dedekind.html)

These are exploratory notes on the Dedekind reals, written to try out ideas
rather than to build a library, the library proper being
[DedekindReals](#dedekindreals).

What is explored is how the Dedekind reals can be defined, there being
several candidate definitions, and the notes set them out and compare them,
keeping track throughout of what is data and what is mere property.

The usual definition is a triple consisting of a lower cut, an upper cut and
a proof that the pair is a cut, in which both cuts are data. But a lower
real has at most one upper cut completing it to a Dedekind real, so that the
upper cut and the axioms relating the two are property of the lower real
rather than further data. The reals can therefore be defined instead as a
subtype of the lower reals, whose inclusion is an embedding, making them a
set.

A further candidate, due to Troelstra, asks of a lower cut only that it be
bounded above and located, and this is proved equivalent to the Dedekind
condition once the order is further assumed dense, upper open, and to
satisfy the criterion that p < q whenever q is not below p and the two are
distinct, which the rationals do satisfy. Under excluded middle the
candidates collapse into one: the Dedekind reals are then equivalent to the
bounded lower reals, and every bounded lower real is Dedekind.

Throughout, the rationals are not constructed but assumed, as an abstract
type with a proposition-valued irreflexive order. This avoids having to
define them, it allows the dyadic rationals or any dense countable subset to
be used instead, and it shows that nothing beyond such an order is needed
for the discussion. Univalence is not used anywhere, although it is
mentioned in the discussions.

[Table of contents](#table-of-contents)

#### [Various.DedekindNonAxiomatic](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Various.DedekindNonAxiomatic.html)

The constructions of the module above are re-exported, with their
assumptions on ℚ and its strict order discharged by Andrew Sneap's rational
numbers.

By Tom de Jong.

[Table of contents](#table-of-contents)

#### [Various.DummettDisjunction](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Various.DummettDisjunction.html)

Dummett disjunction of two propositions P and Q, defined as ((P → Q) → Q) ×
((Q → P) → P), is weaker than intuitionistic disjunction and stronger than
classical disjunction, agreeing with intuitionistic disjunction under
Dummett's linearity axiom (P → Q) + (Q → P) or whenever one of the
propositions is decidable. Many more things in this direction are discussed.

By Martin Escardo.

[Table of contents](#table-of-contents)

#### [Various.LawvereFPT](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Various.LawvereFPT.html)

Lawvere's fixed point theorem is proved, together with a range of its
consequences. In our type theoretic form, the theorem says that if a type A
admits a map onto the functions from A to X, then every endomap of X has a
fixed point, so that a type carrying a fixed-point-free endomap admits no
such map. Underlying it is what is called here Lawvere's fixed-point
combinator, which Lawvere did not consider. It is definable from maps r : A
→ (A → X) and s : (A → X) → A under no assumptions at all, and is a typed
relative of the Y combinator of the untyped lambda calculus; the assumption
that r and s form a section-retraction pair is needed only to show that
what the combinator produces is indeed a fixed point.

The theorem is proved first for retractions, which can be formulated
in a Spartan MLTT, and in fact for a pointwise weakening of retraction
which is enough for the proof and lets the applications avoid function
extensionality. The original form, with surjections, has the weaker
hypothesis but needs a stronger language including propositional
truncation, taken here as an assumption; and for that version the
pointwise weakening no longer suffices.

The intuitionistic proof that no type is equivalent to its own
negation is the case X = 𝟘 with the identity as the endomap. Negation
itself has no fixed points, an observation made here and added to the
[nLab](https://ncatlab.org/nlab/show/Lawvere%27s+fixed+point+theorem)
afterwards.

For universes, two applications of the theorem in succession give that
a universe does not map onto its own function space: the first yields
a type B with B ＝ (B → X) for any X, and the second, applied to the
resulting retraction, yields a fixed point of every endomap of X,
which is absurd for X = 𝟘. For powersets, in the original form, the
maps go into the subtype classifier Ω, and function extensionality is
needed to define negation on it. Using both versions of the theorem
together, the Cantor type and the Baire type are uncountable. A
treatment for embeddings rather than surjections is in
[Various.CantorTheoremForEmbeddings](#variouscantortheoremforembeddings).

The universe is then shown uncountable, and more generally regular
against families indexed by a discrete type, in proofs due to Ingo
Blechschmidt after a problem posed to the students, Ingo in particular, at
the Fischbachau autumn school of 2018, reworked jointly to go through the
fixed point theorem, with a variant trading discreteness for sethood at
the cost of raising a universe level.

Adapting Coquand's paradox of trees, which shows type-in-type
inconsistent for a universe closed under W-types, as formalized in
[Unsafe.Type-in-Type-False](#unsafetype-in-type-false), no type of a
universe is equivalent to that universe, and this needs neither
extensionality nor univalence, being a theorem of a Spartan
MLTT. Hence a universe is a retract of no type of its own, and in
particular the successor universe is neither a retract of nor
equivalent to the original universe. Whether the diagonal construction
there could be replaced by a second application of the fixed point
theorem was left as a question, and is answered in
[Various.LawvereFPT-Generalized](#variouslawverefpt-generalized).

By Martin Escardo and Ingo Blechschmidt.

[Table of contents](#table-of-contents)

#### [Various.LawvereFPT-Generalized](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Various.LawvereFPT-Generalized.html)

A question left open in the module above is answered here, namely whether a
certain diagonalization can be replaced by a second application of the fixed
point theorem. It cannot, at least not directly, but it can once the theorem
is generalized.

By Martin Escardo.

[Table of contents](#table-of-contents)

#### [Various.Lumsdaine](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Various.Lumsdaine.html)

Here is an improvement method learned from Peter Lumsdaine, adapted from an
Agda rendering by Andy Pitts of his Coq code. From an identity system whose
eliminator J has no computation rule, it produces one with a propositional
computation rule.

By Martin Escardo.

[Table of contents](#table-of-contents)

#### [Various.NatIsSetWithoutUniverse](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Various.NatIsSetWithoutUniverse.html)

The natural numbers form a set, proved without using a universe, in answer
to [a question of Naïm Favier](https://types.pl/@ncf/114779291760324789).
The usual route through Hedberg's theorem is not available, because 0 ≠ 1 is
not provable without universes or large elimination from ℕ, by a theorem of
Jan M. Smith. Several proofs are given, the first original and the others
simplifications, and at the end that the type of lists over a set is a set.

By Evan Cavallo.

[Table of contents](#table-of-contents)

#### [Various.NonCollapsibleFamily](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Various.NonCollapsibleFamily.html)

A type is collapsible when it has a weakly constant endomap. If every type
were collapsible, then every type would have decidable equality and hence be
a set by Hedberg's theorem, and global choice would hold, because
collapsible types have split support. A criterion for decidable equality
from the collapsibility of the fibers of a map out of 𝟚 is given here.

By Martin Escardo.

[Table of contents](#table-of-contents)

#### [Various.Pataraia](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Various.Pataraia.html)

Every monotone endomap of a directed complete poset with a least element has
a least fixed point, in topos logic. Pataraia was the first to prove this
constructively, and a version of his proof was published by Escardo with his
permission, which is the impredicative proof followed here. An earlier and
less general theorem, for bounded complete dcpos, is due to Coquand.

By Martin Escardo.

[Table of contents](#table-of-contents)

#### [Various.Pataraia-Taylor](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Various.Pataraia-Taylor.html)

A predicative version of Pataraia's fixed point theorem is proved here:
every monotone endomap of a directed complete poset with a least element
has a least fixed point, now in a setting with function extensionality and
propositional truncations but no resizing axioms. Pataraia's own proof, as
formalized in Various.Pataraia, has an impredicative second step forming
the intersection of all subsets of the dcpo that contain the least element
and are closed under both the endomap and directed suprema. That step is
replaced here by an explicit predicative construction due to Paul Taylor,
which is why the theorem is named after both of them. There is a catch,
though: this predicative version applies only to dcpos whose carrier,
order and index types for directed families all live in the same universe,
and no non-trivial example of such a dcpo exists without assuming
propositional resizing, so producing one to apply the theorem to still
requires such axioms.

By Martin Escardo and Tom de Jong.

[Table of contents](#table-of-contents)

#### [Various.RootsOfBooleanFunctions](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Various.RootsOfBooleanFunctions.html)

A formula is given for a putative root of any boolean function f : 𝟚ⁿ → 𝟚,
written using only the function f and the constant 0, together
with a proof of its correctness. A putative root is one which is a
root provided the function has any root at all. This is based on
Section 8.1 of "Exhaustible sets in higher-type computation", cited
under [TypeTopology](#typetopology) above.

By Martin Escardo and Alice Laroche.

[Table of contents](#table-of-contents)

#### [Various.Types2019](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Various.Types2019.html)

Here are links to the modules that implement the ideas of the TYPES 2019
abstract on compact, totally separated and well-ordered types, cited under
[TypeTopology](#typetopology) above. This module is linked from the
published abstract, and for that reason it is not to be moved.

By Martin Escardo.

[Table of contents](#table-of-contents)

#### [Various.UnivalenceFromScratch](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Various.UnivalenceFromScratch.html)

The univalence axiom is formulated in a self-contained way, first in
mathematical English and then in Agda. The reason for it is that the axiom
is usually explained to general audiences by handwaving, which gives rise to
misconceptions that cannot be addressed in the absence of a precise
definition.

By Martin Escardo.

[Table of contents](#table-of-contents)

### [gist](https://www.cs.bham.ac.uk/~mhe/TypeTopology/gist.index.html)

Examples used for discussion or illustration are kept here, together with
blackboard-style experiments which, if successful, are eventually moved to
the main directories.

By Martin Escardo, Alice Laroche, Ayberk Tosun, Stefano Gogioso, Marc Bezem,
Thierry Coquand, Peter Dybjer, Jakub Opršal and Tom de Jong.

[Table of contents](#table-of-contents)

#### [gist.2-injective-types](https://www.cs.bham.ac.uk/~mhe/TypeTopology/gist.2-injective-types.html)

𝟚-injecting maps and 𝟚-injective types are introduced here. The motivation
is that injective types have no non-trivial decidable properties in general,
and that totally separated types, which have plenty of them by definition,
fail badly to be injective. The question is whether the totally separated
types are the injective types with respect to some class of maps.

By Martin Escardo.

[Table of contents](#table-of-contents)

#### [gist.Ackermann](https://www.cs.bham.ac.uk/~mhe/TypeTopology/gist.Ackermann.html)

The Ackermann function is defined by induction on the ordinal ω², regarding
[this discussion
thread](https://mathstodon.xyz/deck/@cxandru@types.pl/115984233527105134).

By Martin Escardo.

[Table of contents](#table-of-contents)

#### [gist.DependentlyTypedTensors](https://www.cs.bham.ac.uk/~mhe/TypeTopology/gist.DependentlyTypedTensors.html)

Tensors are encoded using dependent types. This summarizes a discussion with
Stefano Gogioso, in which the observation was made independently by both
authors.

By Stefano Gogioso and Ayberk Tosun.

[Table of contents](#table-of-contents)

#### [gist.Hydra](https://www.cs.bham.ac.uk/~mhe/TypeTopology/gist.Hydra.html)

The [Kirby-Paris hydra game](https://en.wikipedia.org/wiki/Hydra_game) is
defined, with a proof that every battle eventually ends, and used to compute
the first terms of the function Hydra.

By Alice Laroche, using ideas and notations from Ayberk Tosun.

[Table of contents](#table-of-contents)

#### [gist.InjectivesVersusAlgebras](https://www.cs.bham.ac.uk/~mhe/TypeTopology/gist.InjectivesVersusAlgebras.html)

These are blackboard thoughts on injective types as algebras of the
partial-map classifier monad, superseded by
[InjectiveTypes.Algebra](https://www.cs.bham.ac.uk/~mhe/TypeTopology/InjectiveTypes.Algebra.html)
apart from a few speculative ideas towards the end.

By Martin Escardo.

[Table of contents](#table-of-contents)

#### [gist.IntervalObject](https://www.cs.bham.ac.uk/~mhe/TypeTopology/gist.IntervalObject.html)

Convex bodies, that is, cancellative iterative midpoint objects, are
considered in the ∞-topos of types. These are experimental thoughts written
while finishing the journal version of the interval-object paper with Alex
Simpson.

By Martin Escardo.

[Table of contents](#table-of-contents)

#### [gist.multiset-addendum-question](https://www.cs.bham.ac.uk/~mhe/TypeTopology/gist.multiset-addendum-question.html)

This answers the question asked in
[Iterative.Multisets-Addendum](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Iterative.Multisets-Addendum.html).

By Alice Laroche.

[Table of contents](#table-of-contents)

#### [gist.not-an-apartness](https://www.cs.bham.ac.uk/~mhe/TypeTopology/gist.not-an-apartness.html)

A failed attempt at a tight apartness on the type ℕ∞₂ is given for
illustration, satisfying every condition except cotransitivity.

By Martin Escardo.

[Table of contents](#table-of-contents)

#### [gist.remove-swap](https://www.cs.bham.ac.uk/~mhe/TypeTopology/gist.remove-swap.html)

The functions remove and remove-swap are defined without Agda's with,
regarding [this mastodon
discussion](https://mathstodon.xyz/deck/@MartinEscardo/112214064298894127).

By Martin Escardo.

[Table of contents](#table-of-contents)

#### [gist.TotallySeparatedReflectionOfOmega](https://www.cs.bham.ac.uk/~mhe/TypeTopology/gist.TotallySeparatedReflectionOfOmega.html)

This is about the totally separated reflection of the type Ω of
propositions. Every type X has one, given by the image of its evaluation map
into ((X → 𝟚) → 𝟚), and the question here is whether that of Ω has a more
direct description. Assuming propositional resizing, the type of maps from
weak excluded middle to 𝟚 has its universal property.

By Martin Escardo.

[Table of contents](#table-of-contents)

#### [gist.transport-discussion](https://www.cs.bham.ac.uk/~mhe/TypeTopology/gist.transport-discussion.html)

The question is whether a certain transport can be performed more easily
using univalence than by hand, and whether cumulativity helps. The
discussion is inconclusive for the moment.

By Marc Bezem, Thierry Coquand, Peter Dybjer and Martin Escardo.

[Table of contents](#table-of-contents)

#### [gist.wrong-proofs](https://www.cs.bham.ac.uk/~mhe/TypeTopology/gist.wrong-proofs.html)

These proofs are kept as they were so that [this mathstodon
discussion](https://mathstodon.xyz/deck/@MartinEscardo/115751523590095370)
can be understood in its original context. The conclusion of that discussion
is that they are not wrong after all, translating to the known proofs by the
encode-decode method, but, crucially relying on having a universe.

By Martin Escardo.

[Table of contents](#table-of-contents)

#### [gist.MajoritiesOnlyActOnSets](https://www.cs.bham.ac.uk/~mhe/TypeTopology/gist.MajoritiesOnlyActOnSets.html)

This, together with
[gist.ThereAreNoHigherSemilattices](https://www.cs.bham.ac.uk/~mhe/TypeTopology/gist.ThereAreNoHigherSemilattices.html)
and
[gist.ThereAreNoHigherSemilattices2](https://www.cs.bham.ac.uk/~mhe/TypeTopology/gist.ThereAreNoHigherSemilattices2.html),
is what remains of experiments that were moved to
[AlgebraicStructuresForcingSethood](#algebraicstructuresforcingsethood) in
April 2026. The three modules now do nothing but import the material in its
new place. The only reason to keep them here is that links to these gists
had been given publicly on mathstodon before the move, and deleting the
modules would break those links.

By Jakub Opršal, by Martin Escardo following a result of David Wärn,
and by Tom de Jong, respectively.

[Table of contents](#table-of-contents)

## Description of unsafe modules

Besides index, the module
[AllModulesIndex](https://www.cs.bham.ac.uk/~mhe/TypeTopology/AllModulesIndex.html)
imports
[Unsafe.index](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Unsafe.index.html)
and
[InfinitePigeon.index](https://www.cs.bham.ac.uk/~mhe/TypeTopology/InfinitePigeon.index.html).
Everything imported by the first, and three of the modules of the second, is
what Agda cannot certify as
[`--safe`](https://agda.readthedocs.io/en/latest/language/safe-agda.html).
All of them are `--without-K`, like the rest of the development.

### [Unsafe](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Unsafe.index.html)

The following are the modules imported by
[Unsafe.index](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Unsafe.index.html).
Some of them live in other directories, and are described here rather than
there because it is here that they are collected.

[Table of contents](#table-of-contents)

#### [Games.Main](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Games.Main.html)

This compiles, through Haskell, to a program that plays tic-tac-toe by the
alpha-beta pruning of the directory [Games](#games), and prints an optimal
play. It is not `--safe` because it prints, using the postulates of
[Unsafe.Haskell](#unsafehaskell).

By Martin Escardo and Paulo Oliva.

[Table of contents](#table-of-contents)

#### [SyntheticHomotopyTheory.Circle.FundamentalGroup](https://www.cs.bham.ac.uk/~mhe/TypeTopology/SyntheticHomotopyTheory.Circle.FundamentalGroup.html)

The loop space of the circle is equivalent to the integers, by the map that
sends an integer k to the k-th power of the loop. It is not `--safe` because
it rests on the postulated circle of the [module
below](#synthetichomotopytheorycirclewithrewriting), and hence also uses
`--rewriting`.

By Tom de Jong.

[Table of contents](#table-of-contents)

#### [SyntheticHomotopyTheory.Circle.WithRewriting](https://www.cs.bham.ac.uk/~mhe/TypeTopology/SyntheticHomotopyTheory.Circle.WithRewriting.html)

The circle is postulated, with a definitional computation rule at the point,
and its dependent universal property is derived. It is not `--safe` because
the circle is given by postulates and the computation rule is implemented by
Agda's rewriting mechanism, which needs the option `--rewriting`.

By Tom de Jong.

[Table of contents](#table-of-contents)

#### [TWA.Thesis.Chapter6.Main](https://www.cs.bham.ac.uk/~mhe/TypeTopology/TWA.Thesis.Chapter6.Main.html)

This compiles, through Haskell, to a program that runs the exact-real search
and regression algorithms of [Todd Waugh Ambridge's thesis](#twa) and prints
a prefix of the answer to a requested precision. Like
[Games.Main](#gamesmain), it is not `--safe` because it prints.

By Todd Waugh Ambridge.

[Table of contents](#table-of-contents)

#### [Unsafe.CantorCompact](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Unsafe.CantorCompact.html)

The Cantor type ℕ → 𝟚 is compact, as a corollary of the [countable Tychonoff
theorem below](#unsafecountabletychonoff), together with further
consequences of that theorem. It is not `--safe` because it depends on it.

By Martin Escardo.

[Table of contents](#table-of-contents)

#### [Unsafe.CoNat-Equiv](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Unsafe.CoNat-Equiv.html)

The conatural numbers defined by coinduction are equivalent to the conatural
numbers defined as the generic convergent sequence, assuming function
extensionality and that bisimilarity is equality. It is not `--safe` because
coinductive records need the option `--guardedness`.

By Alice Laroche.

[Table of contents](#table-of-contents)

#### [Unsafe.CountableTychonoff](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Unsafe.CountableTychonoff.html)

Countable products of compact types are compact, obtained by iterating the
fact that binary products preserve compactness. It is not `--safe` because
Agda does not see that the iteration terminates, and so termination has to
be indicated explicitly.

By Martin Escardo.

[Table of contents](#table-of-contents)

#### [Unsafe.Haskell](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Unsafe.Haskell.html)

Haskell primitives are postulated here, adapted from the [Agda standard
library](https://github.com/agda/agda-stdlib) and given as postulates, so
that programs can be compiled through Haskell and print their output. It is
not `--safe` because of the postulates.

By Martin Escardo.

[Table of contents](#table-of-contents)

#### [Unsafe.Type-in-Type-False](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Unsafe.Type-in-Type-False.html)

Type-in-type is inconsistent, shown in two ways. The first is [Coquand's
paradox of
trees](https://pdfs.semanticscholar.org/f2f3/30b27f1d7ca99c2550f96581a4400c209ef8.pdf),
phrased in terms of Lawvere's fixed point theorem, and the second follows an
argument of Ingo Blechschmidt. It is not `--safe` because it assumes
`--type-in-type`, which is the very hypothesis being refuted. The module
[Various.LawvereFPT](#variouslawverefpt) has formulations that don't assume
it.

By Martin Escardo.

[Table of contents](#table-of-contents)

### [InfinitePigeon](https://www.cs.bham.ac.uk/~mhe/TypeTopology/InfinitePigeon.index.html)

The material of the tutorial "Programs from proofs" is implemented here, as
given by Ulrich Berger, Monika Seisenberger, Martin Escardo and Paulo Oliva
at MFPS XXVII in Pittsburgh in 2011. A classical proof of the infinite
pigeonhole principle, that an infinite binary sequence has an infinite
constant subsequence, is used to prove the finite pigeonhole principle, and
that proof is then run as a program which, given a binary sequence and a
number m, returns a bit and a list of m+1 increasing positions at which the
sequence takes that bit as its value. Classical countable choice is obtained
from the double-negation shift, which is realized in three ways, and it is
these three realizers, and only they, that are not `--safe`. In each case
the reason is the same. The recursion defining the realizer is not seen to
terminate by Agda, and so the module uses the option
`--no-termination-check`. The recursions should nevertheless terminate, but
this has to be checked by the mathematician rather than by Agda.

[Table of contents](#table-of-contents)

#### [InfinitePigeon.J-Shift-BBC](https://www.cs.bham.ac.uk/~mhe/TypeTopology/InfinitePigeon.J-Shift-BBC.html)

The Berardi-Bezem-Coquand functional realizes the shift for the selection
monad J, and hence, in another module, that for the continuation monad K.

[Table of contents](#table-of-contents)

#### [InfinitePigeon.J-Shift-Selection](https://www.cs.bham.ac.uk/~mhe/TypeTopology/InfinitePigeon.J-Shift-Selection.html)

The shift for the selection monad J is realized by infinite iteration of the
finite shift. Termination is proved externally, by bar induction and
continuity.

[Table of contents](#table-of-contents)

#### [InfinitePigeon.K-Shift-MBR](https://www.cs.bham.ac.uk/~mhe/TypeTopology/InfinitePigeon.K-Shift-MBR.html)

Berger's modified bar recursion realizes the shift for the continuation
monad K.

This Agda formalization, like the rest of the directory, is by Martin
Escardo and Paulo Oliva, but of the three realizers only the selection one
is originally theirs: the BBC realizer is due to Berardi, Bezem and
Coquand, and the modified bar recursion realizer here is due to Berger.

**Publications.**

1. M.H. Escardó and P. Oliva, "Selection functions, bar recursion and
   backward induction", Mathematical Structures in Computer Science 20(2),
   2010, 127–168,
   [doi:10.1017/S0960129509990351](https://doi.org/10.1017/S0960129509990351),
   which gives the definition realized by the selection-function shift above
   and the external termination proof by bar induction and continuity.

1. The slides of the tutorial,
   <http://www.cs.bham.ac.uk/~mhe/.talks/mfps2011/mfps2011.pdf>, and its web
   page, <https://www.cs.bham.ac.uk/~mhe/pigeon/>.

[Table of contents](#table-of-contents)

## List of people mentioned in the files

Everybody named anywhere in the Agda files is listed here, whether they
wrote code, supplied an idea, asked a question, or gave their name to a
notion. Those who wrote Agda are marked as contributors, and their entry
links to a search for the files they contributed to. The others link to the
file that mentions them, or, when there are several, to a search of the
repository.

* [Andreas Abel](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Abel&c=1)
* [Samson Abramsky](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Abramsky&c=1)
* [Wilhelm Ackermann](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Ackermann&c=1)
* [Peter Aczel](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Aczel&c=1)
* [Ettore Aldrovandi](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Ettore%20Aldrovandi) (contributor)
* [Cass Alexandru](https://www.cs.bham.ac.uk/~mhe/TypeTopology/PCF.Combinatory.ScottModelOfPCF.html)
* [Thorsten Altenkirch](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Altenkirch&c=1)
* [Carlo Angiuli](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Carlo%20Angiuli) (contributor)
* [Igor Arrieta](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Igor%20Arrieta) (contributor)
* [Jeremy Avigad](https://www.cs.bham.ac.uk/~mhe/TypeTopology/UF.Pullback.html)
* [Fredrik Bakke](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Fredrik%20Bakke) (contributor)
* [Stefan Banach](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Banach&c=1)
* [Reid Barton](https://www.cs.bham.ac.uk/~mhe/TypeTopology/UF.Replacement.html)
* [Andrej Bauer](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Bauer&c=1)
* [Ulrich Berger](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Berger&c=1)
* [Felix Bernstein](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Bernstein&c=1)
* [Marc Bezem](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Marc%20Bezem) (contributor)
* [Lane Biocini](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Lane%20Biocini) (contributor)
* [Errett Bishop](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Bishop&c=1)
* [Ingo Blechschmidt](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Blechschmidt&c=1)
* [Elisabeth Bonnevier](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Bonnevier&c=1)
* [Auke Booij](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Various.Dedekind.html)
* [John Bourke](https://www.cs.bham.ac.uk/~mhe/TypeTopology/InjectiveTypes.Article.html)
* [L. E. J. Brouwer](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Brouwer&c=1)
* [Ulrik Buchholtz](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Ulrik%20Buchholtz) (contributor)
* [Cesare Burali-Forti](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Burali-Forti&c=1)
* [Pierre Cagne](https://www.cs.bham.ac.uk/~mhe/TypeTopology/UF.Size.html)
* [Georg Cantor](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Cantor&c=1)
* [J. A. Carr](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=J.%20A.%20Carr) (contributor)
* [Augustin-Louis Cauchy](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Cauchy&c=1)
* [Evan Cavallo](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Evan%20Cavallo) (contributor)
* [Arthur Cayley](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Cayley&c=1)
* [James Chapman](https://www.cs.bham.ac.uk/~mhe/TypeTopology/RelativeMonadOnStructuredTypes.index.html)
* [Alonzo Church](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Church&c=1)
* [John Conway](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Games.Discussion.html)
* [Thierry Coquand](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Thierry%20Coquand) (contributor)
* [Giovanni Curi](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Curi&c=1)
* [Haskell Curry](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Curry&c=1)
* [Keri D'Angelo](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Keri%20D%27Angelo) (contributor)
* [Nils Anders Danielsson](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Danielsson&c=1)
* [Tom de Jong](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Tom%20de%20Jong) (contributor)
* [Augustus De Morgan](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=De%20Morgan&c=1)
* [Richard Dedekind](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Dedekind&c=1)
* [Michael Dummett](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Dummett&c=1)
* [Peter Dybjer](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Peter%20Dybjer) (contributor)
* [Beno Eckmann](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Eckmann&c=1)
* [Martin Escardo](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Martin%20Escardo) (contributor)
* [Naïm Favier](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Various.NatIsSetWithoutUniverse.html)
* [Michael Fourman](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Fourman&c=1)
* [Jonas Frey](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Frey&c=1)
* [Peter Freyd](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Freyd&c=1)
* [Harvey Friedman](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Friedman&c=1)
* [Kurt Gödel](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=G%C3%B6del&c=1)
* [Stefano Gogioso](https://www.cs.bham.ac.uk/~mhe/TypeTopology/gist.DependentlyTypedTensors.html)
* [Daniel Gratzer](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Gratzer&c=1)
* [Dan Grayson](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Dan%20Grayson&c=1)
* [Robin Grayson](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Robin%20Grayson&c=1)
* [Chris Groassack](https://www.cs.bham.ac.uk/~mhe/TypeTopology/TypeTopology.index.html)
* [Alexander Grothendieck](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Grothendieck&c=1)
* [Håkon Robbestad Gylterud](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Gylterud&c=1)
* [Peter Hancock](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Hancock&c=1)
* [Brendan Hart](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Brendan%20Hart) (contributor)
* [Felix Hausdorff](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Hausdorff&c=1)
* [Michael Hedberg](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Hedberg&c=1)
* [Arend Heyting](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Heyting&c=1)
* [Denis Higgs](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Higgs&c=1)
* [Peter Hilton](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Hilton&c=1)
* [Martin Hofmann](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Hofmann&c=1)
* [William Alvin Howard](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Howard&c=1)
* [John Isbell](https://www.cs.bham.ac.uk/~mhe/TypeTopology/NotionsOfDecidability.QuasiDecidable.html)
* [Bart Jacobs](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Jacobs&c=1)
* [Peter Johnstone](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Johnstone&c=1)
* [André Joyal](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Joyal&c=1)
* [Achim Jung](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Jung&c=1)
* [Ohad Kammar](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Ohad%20Kammar) (contributor)
* [Kan](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Kan&c=1)
* [Chris Kapulkin](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Kapulkin&c=1)
* [Klaus Keimel](https://www.cs.bham.ac.uk/~mhe/TypeTopology/TypeTopology.TotallySeparated.html)
* [Laurie Kirby](https://www.cs.bham.ac.uk/~mhe/TypeTopology/gist.Hydra.html)
* [Dominik Kirst](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Ordinals.WellOrderingTaboo.html)
* [Stephen Kleene](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Kleene&c=1)
* [Heinrich Kleisli](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Kleisli&c=1)
* [Cory Knapp](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Cory%20Knapp) (contributor)
* [König](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=K%C3%B6nig&c=1)
* [Nicolai Kraus](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Nicolai%20Kraus) (contributor)
* [Georg Kreisel](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Kreisel&c=1)
* [Kazimierz Kuratowski](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Kuratowski&c=1)
* [Joachim Lambek](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Lambek&c=1)
* [Alice Laroche](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Alice%20Laroche) (contributor)
* [F. William Lawvere](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Lawvere&c=1)
* [Gerald Leversha](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Leversha&c=1)
* [Paul Levy](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Paul%20Levy) (contributor)
* [Peter Lumsdaine](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Lumsdaine&c=1)
* [Anatoly Maltsev](https://www.cs.bham.ac.uk/~mhe/TypeTopology/AlgebraicStructuresForcingSethood.WeakNearUnanimity.html)
* [Graham Manuell](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Locales.Compactness.CharacterizationOfCompactLocales.html)
* [Markov](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Markov&c=1)
* [Per Martin-Löf](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Martin-L%C3%B6f&c=1)
* [Sebastian Meyer](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Meyer&c=1)
* [Anders Mörtberg](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=M%C3%B6rtberg&c=1)
* [Joan Moschovakis](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Moschovakis&c=1)
* [Guillaume Munch-Maccagnoni](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Munch-Maccagnoni&c=1)
* [Fredrik Nordvall Forsberg](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Fredrik%20Nordvall%20Forsberg) (contributor)
* [Ulf Norell](https://www.cs.bham.ac.uk/~mhe/TypeTopology/TypeTopology.DecidabilityOfNonContinuity.html)
* [Kelton OBrien](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Kelton%20OBrien) (contributor)
* [Paulo Oliva](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Paulo%20Oliva) (contributor)
* [Jakub Opršal](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Jakub%20Oprsal) (contributor)
* [Bruno Paiva](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Bruno%20Paiva) (contributor)
* [Dito Pataraia](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Pataraia&c=1)
* [Giuseppe Peano](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Peano&c=1)
* [Charles Sanders Peirce](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Peirce&c=1)
* [Andy Pitts](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Pitts&c=1)
* [William C. Powell](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Powell&c=1)
* [Cécilia Pradic](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Pradic&c=1)
* [Vincent Rahli](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Vincent%20Rahli) (contributor)
* [Ian Ray](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Ian%20Ray) (contributor)
* [Alex Rice](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Alex%20Rice) (contributor)
* [Egbert Rijke](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Rijke&c=1)
* [Giuseppe Rosolini](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Rosolini&c=1)
* [J. Barkley Rosser](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Rosser&c=1)
* [Bertrand Russell](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Russell&c=1)
* [Christian Sattler](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Ordinals.OrdinalOfOrdinalsInfima.html)
* [Ernst Schröder](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Schr%C3%B6der&c=1)
* [Dana Scott](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Scott&c=1)
* [Phil Scott](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Phil%20Scott&c=1)
* [Monika Seisenberger](https://www.cs.bham.ac.uk/~mhe/TypeTopology/InfinitePigeon.index.html)
* [Anton Setzer](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Setzer&c=1)
* [Mike Shulman](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Mike%20Shulman) (contributor)
* [Wacław Sierpiński](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Sierpi%C5%84ski&c=1)
* [Alex Simpson](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Simpson&c=1)
* [Jan M. Smith](https://www.cs.bham.ac.uk/~mhe/TypeTopology/Various.NatIsSetWithoutUniverse.html)
* [Andrew Sneap](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Andrew%20Sneap) (contributor)
* [Kristina Sojakova](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Sojakova&c=1)
* [Bas Spitters](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Spitters&c=1)
* [Jon Sterling](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Jon%20Sterling) (contributor)
* [Marshall Stone](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Stone&c=1)
* [Thomas Streicher](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Streicher&c=1)
* [Andrew Swan](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Andrew%20Swan) (contributor)
* [Alfred Tarski](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Tarski&c=1)
* [Paul Taylor](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Paul%20Taylor&c=1)
* [Walter Taylor](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Walter%20Taylor&c=1)
* [Linus Torvalds](https://www.cs.bham.ac.uk/~mhe/TypeTopology/index.html)
* [Ayberk Tosun](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Ayberk%20Tosun) (contributor)
* [Anne Sjerp Troelstra](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Troelstra&c=1)
* [Alan Turing](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Turing&c=1)
* [Andrey Tychonoff](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Tychonoff&c=1)
* [Tarmo Uustalu](https://www.cs.bham.ac.uk/~mhe/TypeTopology/RelativeMonadOnStructuredTypes.index.html)
* [Simcha van Collem](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Simcha%20van%20Collem) (contributor)
* [Andrea Vezzosi](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Vezzosi&c=1)
* [Steve Vickers](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Vickers&c=1)
* [Vladimir Voevodsky](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Voevodsky&c=1)
* [David Wärn](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=W%C3%A4rn&c=1)
* [Todd Waugh Ambridge](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Todd%20Waugh%20Ambridge) (contributor)
* [Ross Willard](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Willard&c=1)
* [Anna Williams](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Anna%20Williams) (contributor)
* [Gavin Wraith](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Wraith&c=1)
* [Chuangjie Xu](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Chuangjie%20Xu) (contributor)
* [Nobuo Yoneda](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Yoneda&c=1)
* [Ernst Zermelo](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Zermelo&c=1)
* [Max Zorn](https://www.cs.bham.ac.uk/~mhe/TypeTopologySearch.html#q=Zorn&c=1)

[Table of contents](#table-of-contents)
