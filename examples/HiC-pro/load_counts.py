from __future__ import print_function
from iced import io
import numpy as np

print("Checking the normalized matrix can be re-loaded")

counts = io.load_counts("/tmp/iced_matrix.matrix", base=1)

# Load with np.loadtxt and check that the shape makes sense
print("Checking the shape of the written matrix makes sense...")
t = np.loadtxt("/tmp/iced_matrix.matrix")
if t.shape[1] != 3:
    raise ValueError("The shape of the written matrix doesn't make sense")

print("Checking the shape of the bias makes sense...")
bias = np.loadtxt("/tmp/iced_matrix.matrix.biases")

if counts.shape[0] != bias.shape[0]:
    raise ValueError(
        "The shape of the count matrix doesn't match the bias")
