import numpy as np
from scipy import sparse


def downsample_contact_map(counts, nreads=None, proportion=None,
                           random_state=None):
    """
    Downsample the contact count matrix

    Parameters
    ----------
    counts : ndarray or sparse matrix
        The raw contact count matrix.

    nreads : integer, optional, default : None
        The number of reads of resulting matrix. By default, will downsample
        to 80% of the original matrix.
        `nreads` and `proportion` cannot be both provided.

    proportion : float [0, 1], optional, default: None
        The proportion of reads of the resulting downsampled matrix. By
        default, will downsample to 80% of the matrix.
        `nreads` and `proportion` cannot be both provided.

    random_state : random_state object, optional

    Returns
    -------
    c : downsampled contact count matrix as a COO matrix.
    """
    if counts.dtype != "int":
        if np.abs(counts - np.round(counts)).sum() != 0:
            raise ValueError("Count matrix should be integers")
        counts = counts.astype("int")
    if not sparse.issparse(counts):
        # Convert into COO sparse matrix
        counts = sparse.coo_matrix(np.triu(counts))
    elif not sparse.isspmatrix_coo(counts):
        # Also convert into COO sparse matrix
        counts = sparse.coo_matrix(counts)

    if nreads is None and proportion is None:
        nreads = int(np.round(counts.sum() * 0.8))

    if nreads is not None and proportion is not None:
        raise ValueError(
            "The user provided both the number of reads and "
            "proportion. Provide one or the other")

    if proportion is not None and ((proportion < 0) or (proportion > 1)):
        raise ValueError(
            "`proportion` should be between 0 and 1. %f was provided" %
            proportion)

    if nreads is None:
        nreads = proportion = counts.sum()

    if random_state is None:
        random_state = np.random.RandomState()
    elif isinstance(random_state, int):
        random_state = np.random.RandomState(random_state)

    x, y = np.indices(counts.shape)
    # Create a matrix of indices where each entry corresponds to an
    # interacting pair of loci, and where interacting pairs appear the number
    # of time they interact
    ind = np.repeat(np.arange(len(counts.data)), counts.data, axis=0)

    # Shuffle the indices and select f*nreads number of interaction
    sub_ind = random_state.choice(ind, size=nreads, replace=False)

    # Recreate the interaction counts matrix.
    c = sparse.coo_matrix(
        (np.ones(len(sub_ind)), (counts.row[sub_ind],
                                 counts.col[sub_ind])),
        shape=counts.shape, dtype=float)
    return c


def bootstrap_contact_map(counts, random_state=None):
    """
    Bootstrap the contact count matrix

    Parameters
    ----------
    counts : ndarray or sparse matrix
        The raw contact count matrix.

    random_state : random_state object, optional

    Returns
    -------
    c : downsampled contact count matrix as a COO matrix.
    """
    if counts.dtype != "int":
        if np.abs(counts - np.round(counts)).sum() != 0:
            raise ValueError("Count matrix should be integers")
        counts = counts.astype("int")
    if not sparse.issparse(counts):
        # Convert into COO sparse matrix
        counts = sparse.coo_matrix(np.triu(counts))
    elif not sparse.isspmatrix_coo(counts):
        # Also convert into COO sparse matrix
        counts = sparse.coo_matrix(counts)

    if random_state is None:
        random_state = np.random.RandomState()
    elif isinstance(random_state, int):
        random_state = np.random.RandomState(random_state)

    x, y = np.indices(counts.shape)
    # Create a matrix of indices where each entry corresponds to an
    # interacting pair of loci, and where interacting pairs appear the number
    # of time they interact
    ind = np.repeat(np.arange(len(counts.data)), counts.data, axis=0)

    nreads = counts.sum()
    # Shuffle the indices and select f*nreads number of interaction
    sub_ind = random_state.choice(ind, size=nreads, replace=True)

    # Recreate the interaction counts matrix.
    c = sparse.coo_matrix(
        (np.ones(len(sub_ind)), (counts.row[sub_ind],
                                 counts.col[sub_ind])),
        shape=counts.shape, dtype=float)
    return c
