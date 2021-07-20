from iced import io
import numpy as np

counts = io.load_counts("/tmp/iced_matrix.matrix")

# Load with np.loadtxt and check that the shape makes sense
print("Checking the shape of the written matrix makes sense")
t = np.loadtxt("/tmp/iced_matrix.matrix")
if t.shape[1] != 3:
    raise ValueError("The shape of the written matrix doesn't make sense")

# Checking that the base seems fine (ie, is one)
if t[0, 0] < 1 or t[0, 1] < 1:
    raise ValueError("The output should be 1-based, not 0 based")
