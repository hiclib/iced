---
title: 'iced: fast and memory efficient normalization of contact maps'
tags:
  - Hi-C contact count
  - Normalization
authors:
 - name: Nelle Varoquaux
   orcid: 0000-0002-8748-6546
   affiliation: "1"
 - name: Nicolas Servant
   orcid: 0000-0003-1678-7410
   affiliation: "3, 4, 5"
affiliations:
 - name: University of California, Berkeley
   index: 1
 - name: Institut Curie
   index: 3
 - name: INSERM
   index: 4
 - name: Mines ParisTech
   index: 5

date: 2019, February, 7th
bibliography: paper.bib

---

# Summary

Recent technological advances allow the measurement, in a single Hi-C
experiment, of the frequencies of physical contacts among pairs of genomic
loci at a genome-wide scale.

[**Iced**](https://github.com/hiclib/iced) implements fast and memory
efficient normalization methods, such the ICE normalization strategy or the
SCN algorithm [@varoquaux:iced_osf]. It is included in the HiC-pro pipeline, that processes data
from raw fastq files to normalized contact maps [@servant:hicpro]. iced
eventually grew bigger than just being a normalization packages, and contains
a number of utilities functions that may be useful if you are analyzing and
processing Hi-C data.

Moving from sequencing reads to a normalized contact map is a challenging
task. Hi-C usually requires several millions to billions of paired-end
sequencing reads, depending on genome size and on the desired resolution.
Managing these data thus requires optimized bioinformatic workflows able to
extract the contact frequencies in reasonable computational time and with
reasonable resource and storage requirements. The final step of such pipeline
is typically a normalization step, essential to ensure accurate analysis and
proper interpretation of the results.
  
We propose here fast implementations of the iterative correction method
[@imakaev:iterative] and SCN [@cournac:normalization] in Python. iced
emphasizes ease-of-use, performance, maintainability, and memory-efficiency.
This implementation leverages a memory-efficient data format of Hi-C maps, and
outperforms both in speed and memory usage HiCorrector [@li:hi-corrector], a
parallelized C++ implementation of the same algorithm.

# References
