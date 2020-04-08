# Basic normalization
ice subset.matrix

# More HiC-pro like with the options
ice --results_filename /tmp/iced_matrix.matrix --filter_low_counts_perc 0.02 \
--filter_high_counts_perc 0.02 --max_iter 1000 --eps 0.1 \
--remove-all-zeros-loci --output-bias 1 --verbose 1 subset.matrix 

python load_counts.py
