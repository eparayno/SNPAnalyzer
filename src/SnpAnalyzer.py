# SNPANALYZER.PY
# AUTHOR: Erika Parayno
# DATE: 07/22/2020
# LAST EDITED: 07/28/2020
# DESCRIPTION:  Takes a fasta file with corresponding csv file of genome to identify and analyze SNPs.
#               Including SNP's upstream and downstream buffer nucleotides, the program then performs blast operations
#               to find matching genomes of other organisms.
# ASSUMPTIONS:  - fasta file located in subdirectory source: containing at least accession name
#               - csv file with the following attributes: accession, species, length, completeness,
#                 geo location, US state, isolation source and collection date
#               - paths edited appropriately in the code (see line 20-21)
import GenbankDataHandler
from BufferGenerator import create_buffer
from SequenceBlaster import blast_sequence
from CommonLengthAligner import align
from SnpFinder import snp_finder


class SnpAnalyzer:
    # file paths, EDIT THIS AS NEEDED FOR YOUR RESPECTIVE GENES / FILES
    sequences_path = "data/SeqDNA.fasta"
    attributes_path = "data/SeqAttributes.csv"

    # handle fasta and csv files and store each item into Sequence object list
    origSeqStorage = GenbankDataHandler.read_files(sequences_path, attributes_path)

    # align sequences in list based on common length
    trimmedSeqStorage = align(origSeqStorage)

    # get locations of SNPs with respective frequencies and get location with most mutations
    mutationLocMode = snp_finder(trimmedSeqStorage)

    # create buffer sequence near location with most frequencies
    buffer_length = 30
    areaOfInterest = create_buffer(trimmedSeqStorage[0], mutationLocMode, buffer_length)

    # get buffer sequence organism match using BLAST
    blast_sequence(areaOfInterest)

    print("\nEnd of program.")

