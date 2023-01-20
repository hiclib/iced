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
    if not np.issubdtype(counts.dtype, np.integer):
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
        nreads = int(np.round(proportion * counts.sum()))

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
    if not np.issubdtype(counts.dtype, np.integer):
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


def permute_contact_map(counts, random_state=None, circular=False):
    """
    Randomize matrix preserving the distribution of elements per diagonal

    Arguments
    ---------
    matrix : ndarray (n, n)
        The ndarray to shuffle

    circular : boolean, optional, default: False
        Whether the chromosome is circular.

    Returns
    -------
    Randomized matrix that preserves the contact law P(s)
    """
    if random_state is None:
        random_state = np.random.RandomState()
    elif isinstance(random_state, int):
        random_state = np.random.RandomState(random_state)

    if circular:
        return _permute_contact_map_circular(
            counts,
            random_state=random_state)
    else:
        randomized_counts = np.zeros(counts.shape)

        N = len(counts)

        for s in range(0, N):
            indices = random_state.shuffle(np.arange(N - s))
            random_elements = np.diag(counts, k=s)[indices]
            np.fill_diag(randomized_counts.T[s:], random_elements)
        return randomized_counts


def _permute_contact_map_circular(counts, random_state=None):
    N = len(counts)
    randomized_counts = np.zeros(counts.shape)

    # Draw random samples directly from the data
    indices = np.arange(N)
    np.random.shuffle(indices)
    np.fill_diagonal(randomized_counts, np.diag(counts)[indices])

    for s in range(1, int(np.ceil(N / 2))):
        # Start by upper diagonals
        sub_diag = np.concatenate(
            [np.diag(counts, k=s),
             np.diag(counts, k=s-N)])
        np.random.shuffle(indices)
        random_elements = sub_diag[indices]
        np.fill_diagonal(
            randomized_counts.T[s:],
            random_elements[:N-s])
        np.fill_diagonal(
            randomized_counts[N-s:],
            random_elements[N-s:N])

        # And now lower diagonals
        sub_diag = np.concatenate(
            [np.diag(counts, k=-s),
             np.diag(counts, k=N-s)])
        np.random.shuffle(indices)
        random_elements = sub_diag[indices]
        np.fill_diagonal(
            randomized_counts[s:],
            random_elements[:N-s])
        np.fill_diagonal(
            randomized_counts.T[N-s:],
            random_elements[N-s:N])

    return randomized_counts
