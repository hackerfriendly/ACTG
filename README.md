ACTG for SublimeText
====================

Nucleotide syntax highlighting and reverse complement support. This is handy for "stare at the screen and squint" DNA analysis.

Features
--------

* Choose 'Nucleotides' syntax highlighting to colorize ACTG and N.
* Automatically associates .fa, .fasta, .fq, .fastq, .sam, and .vcf files.
* Make a selection and hit Control-Shift-R (or Command-Shift-R on Mac) to replace it with the reverse complement.

Bugs
----

* ACTG and N are simply highlighted in place, which can make for some interestingly colored VCF comments and quality strings. A more clever regex would help, if only I could fathom the tmLanguage backreference match syntax.

Patches welcome.

Releases
--------

* 0.0.1: Initial release, 2014-09-29

Thanks
------

Developed at Spiral Genetics, http://www.spiralgenetics.com/
