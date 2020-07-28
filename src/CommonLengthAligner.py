# COMMONLENGTHALIGNER.PY
# AUTHOR: Erika Parayno
# DATE: 07/22/2020
# LAST EDITED: 07/28/2020
# DESCRIPTION:  Basic common alignment tool that finds most common sequence length within a list of sequences.
#               It chooses the most common length to allow for the largest size of sequences for analysis.
#               Then, creates a new list of sequences using the original sequence list, containing sequences that are of
#               length of most common sequence length.
# ASSUMPTIONS:  - Sequences in list have sequence that are complete and accurate.
from statistics import mode


# pre-condition: orig_seq_storage contains objects with complete sequence
# post-condition: created a new list containing only sequences with common, most frequent length
# return: trimmed-seq_storage
def align(orig_seq_storage):
    # get the different lengths of each Sequence object and store onto list
    lengths = []
    for i in orig_seq_storage:
        lengths.append(i.length)

    # get most common length
    mode_length = mode(lengths)
    print("\nMost common length: " + mode_length)

    # trim original sequence storage, containing only sequences with common length
    trimmed_seq_storage = []
    for i in orig_seq_storage:
        if i.length == mode_length:
            trimmed_seq_storage.append(i)
            i.to_string()

    return trimmed_seq_storage
