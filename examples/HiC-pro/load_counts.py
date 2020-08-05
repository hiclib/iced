from __future__ import print_function
from iced import io
import numpy as np

print("Checking the normalized matrix can be re-loaded")

counts = io.load_counts("/tmp/iced_matrix.matrix")

# Load with np.loadtxt and check that the shape makes sense
print("Checking the shape of the written matrix makes sense")
t = np.loadtxt("/tmp/iced_matrix.matrix")
if t.shape[1] != 3:
    raise ValueError("The shape of the written matrix doesn't make sense")
