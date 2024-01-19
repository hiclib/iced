import numpy as np
from scipy import sparse
import pytest

from iced.random import downsample_contact_map
from iced.random import bootstrap_contact_map
from iced import datasets


def test_downsample_contact_map():
    counts, lengths = datasets.load_sample_yeast()
    nreads = int(np.round(0.8 * np.triu(counts).sum()))
    downsampled_counts = downsample_contact_map(counts,
                                                random_state=42)
    assert nreads == downsampled_counts.sum()

    downsampled_counts = downsample_contact_map(counts, nreads=nreads,
                                                random_state=42)
    assert nreads == downsampled_counts.sum()

    downsampled_counts = downsample_contact_map(counts, proportion=0.8,
                                                random_state=42)
    assert nreads == downsampled_counts.sum()

    with pytest.raises(ValueError):
        downsample_contact_map(counts*.3, nreads=nreads,
                               random_state=42)

    with pytest.raises(ValueError):
        downsample_contact_map(counts, nreads=nreads,
                               proportion=0.5,
                               random_state=42)

    # Test that it works with COO matrices
    counts = sparse.coo_matrix(np.triu(counts))
    downsampled_counts = downsample_contact_map(counts, nreads=nreads,
                                                random_state=42)
    assert nreads == downsampled_counts.sum()

    # Test that it works with CSR matrices
    counts = sparse.csr_matrix(counts)
    downsampled_counts = downsample_contact_map(counts, nreads=nreads,
                                                random_state=42)
    assert nreads == downsampled_counts.sum()

    with pytest.raises(ValueError):
        downsample_contact_map(counts, proportion=-0.1)

    with pytest.raises(ValueError):
        downsample_contact_map(counts, proportion=1.5)

    downsample_contact_map(counts)


def test_bootstrap_contact_map():
    counts, lengths = datasets.load_sample_yeast()
    bootstrap_contact_map(counts,
                          random_state=42)
    with pytest.raises(ValueError):
        bootstrap_contact_map(counts*.3,
                              random_state=42)

    # Test that it works with COO matrices
    counts = sparse.coo_matrix(np.triu(counts))
    bootstrap_contact_map(counts,
                          random_state=42)

    # Test that it works with CSR matrices
    counts = sparse.csr_matrix(counts)
    bootstrap_contact_map(counts,
                          random_state=42)

    bootstrap_contact_map(counts)
