.. _tutorial_menu:


================
Iced tutorial
================



.. note:: **Doctest Mode**

   The code-examples in the above tutorials are written in a
   *python-console* format. If you wish to easily execute these examples
   in **IPython**, use::

  %doctest_mode

   in the IPython-console. You can then simply copy and paste the examples
   directly into IPython without having to worry about removing the **>>>**
   manually.


What is iced?
=============

``iced`` is a python package that contains normalization techniques for Hi-C data.
It is included in the HiC-pro pipeline, that processes data from raw fastq
files to normalized contact maps. Eventually, ``iced`` grew bigger than just being a
normalization packages, and contains a number of utilities functions that may
be useful if you are analyzing and processing Hi-C data.

If you use ``iced``, please cite:

HiC-Pro: An optimized and flexible pipeline for Hi-C processing. Servant N.,
Varoquaux N., Lajoie BR., Viara E., Chen CJ., Vert JP., Dekker J., Heard E.,
Barillot E. Genome Biology 2015, 16:259 doi:10.1186/s13059-015-0831-x
http://www.genomebiology.com/2015/16/1/259

Working with Hi-C data in Python
================================

Hi-C data boils down to a matrix of contact counts. Each row and columns
corresponds to a genomic window, and each entry to the number of times these
genomic windows have been observed to interact with one another. Python
happens to be an excellent language to manipulate matrices, and ``iced``
leverages a number of scientific packages that provides nice and easy-to-use
matrix operation. 

.. note::

   If you are not familiar with numpy and python, we strongly encourage to
   follow the short tutorial of the `scipy lecture notes
   <http://www.scipy-lectures.org/>`_

.. _loading_example_dataset

Loading an example dataset
==========================

``iced`` comes with a sample data set that allows you to play a bit with the
package. The sample data set included corresponds to the first 5 chromosomes
of the budding yeast *S. cerevisiae*. In the following, we start a Python or
IPython interpreter from our shell and load this data set. Our notational
convention is that ``$`` denotes the shell prompt while ``>>>`` denotes the
Python interpreter prompt::                                                                                      

  $ python
  >>> from iced import datasets
  >>> counts, lengths = datasets.load_sample_yeast()

A data set in ``iced`` is composed of an N by N numpy.ndarray ``counts`` and a
vector of ``lengths`` that contains the number of bins per chromosomes. For
our sample data, the vector ``lengths`` is an ndarray of length 5, underlying
we have here 5 chromosomes::

  >>> print(len(lengths))
  5

The contact map ``counts`` should be squared and symmetric. The shape should
also match the lengths vector::

  >>> print(counts.shape)
  (350, 350)
  >>> print(lengths.sum())
  350

The ``counts`` matrix is here of size 350 by 350.

You've successfully loaded your first Hi-C data! Let's plot it.



