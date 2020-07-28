# SNPFINDER.PY
# AUTHOR: Erika Parayno
# DATE: 07/22/2020
# LAST EDITED: 07/28/2020
# DESCRIPTION:  Takes set of sequences and finds most frequently occurring mutation.
# ASSUMPTIONS:  - Sequences in list are of equal length
from collections import Counter
from statistics import mode


# pre-condition: trimmed_seq_storage is a list that contains sequences of equal length
# post-condition: calculated location with most mutation
# return: mutation_loc_mode
def snp_finder(trimmed_seq_storage):
    # traverse through two sequences at a time, find mismatches, and store location onto list
    mutation_indexes = []
    counter = 0

    while counter < len(trimmed_seq_storage) - 1:
        a = trimmed_seq_storage[counter].dna_seq
        b = trimmed_seq_storage[counter + 1].dna_seq

        str_index = 0
        for aNuc, bNuc in zip(a, b):
            if aNuc != bNuc:
                mutation_indexes.append(str_index)
            str_index = str_index + 1

        counter = counter + 1

    # generate frequency dictionary (key: mutation location, value: respective mutation frequencies)
    counts = Counter(mutation_indexes)

    # print counts
    print("\nNucleotide location relative to start with mutation frequencies: \n", counts)

    # get location with the most frequencies
    mutation_loc_mode = mode(mutation_indexes)

    return mutation_loc_mode
