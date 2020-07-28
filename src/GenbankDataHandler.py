# GENBANKDATAHANDLER.PY
# AUTHOR: Erika Parayno
# DATE: 07/22/2020
# LAST EDITED: 07/28/2020
# DESCRIPTION:  Takes GenBank data in forms of fasta and csv and stores it in Sequence object, which will be stored
#               in list structure. Allows for encapsulation of data.
# ASSUMPTIONS:  - Requirement #1: fasta file located in subdirectory source: containing at least accession name
#               - Requirement #2: csv file with the following attributes: accession, species, length, completeness,
#                 geo location, US state, isolation source and collection date
import csv
from Sequence import Sequence

# pre-condition: sequences_path and attributes_path are valid paths, containing files that conform to requirements
# post-condition: Each GenBank result is stored into a new Sequence object, which is stored inside a sequence list
# return: orig_seq_storage
def read_files(sequences_path, attributes_path):
    # initialize structure to store sequence object
    orig_seq_storage = []

    # append ">END" flag to fasta file
    with open(sequences_path, 'a') as f:
        f.write("\n>END")

    # open fasta file to read
    seq_file = open(sequences_path, "r")

    # read each sequence from csv and fasta files
    with open(attributes_path, "r") as attributesFile:
        reader = csv.reader(attributesFile, delimiter=",")
        for i, line in enumerate(reader):

            # create new sequence
            new_sequence = Sequence()

            # define sequence variables
            new_sequence.accession = line[0]
            new_sequence.species = line[1]
            new_sequence.length = line[2]
            new_sequence.nuc_completeness = line[3]
            new_sequence.geo_location = line[4]
            new_sequence.us_state = line[5]
            new_sequence.isolation_source = line[6]
            new_sequence.collection_date = line[7]

            # extract DNA sequence
            curr_dna_seq = []
            iterator = True
            seq_line = seq_file.readline()

            while iterator:
                seq_line = seq_file.readline()
                if seq_line[0] == ">":
                    iterator = False
                else:
                    # store sequence from fasta file into object variable, stripping whitespace
                    curr_dna_seq.append(seq_line.strip())

            # join curr_dna_seq and store to object DNASeq
            new_sequence.dna_seq = ''.join(curr_dna_seq)
            curr_dna_seq.clear()

            # append sequence to sequence storage
            orig_seq_storage.append(new_sequence)

            # print data
            new_sequence.to_string()

    return orig_seq_storage
