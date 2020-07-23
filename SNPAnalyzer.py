# SNPANALYZER.PY
# AUTHOR: ERIKA PARAYNO
# DATE: 07/22/2020
# DESCRIPTION:  Takes a fasta file with corresponding csv file of genome to identify and analyze SNPs.
#               Including SNP's upstream and downstream buffer nucleotides, the program then performs blast operations
#               to find matching genomes of other organisms.
# ASSUMPTIONS:  - fasta file located in subdirectory source: containing at least accession name & ending in >END
#               - csv file with the following attributes: acccession, species, length, completeness,
#                 geo location, US state, isolation source and collection date
#               - paths edited appropriately in the code (see line 35-36)

# class storing DNA attributes
class Sequence:
    accession = ""
    species = ""
    length = ""
    nuc_completeness = ""
    geo_location = ""
    us_state = ""
    isolation_source = ""
    collection_date = ""
    DNAseq = ""

    def toString(self):
        print(f'Accession[{self.accession}] = {self.species}, {self.length}, {self.nuc_completeness}, {self.geo_location}, {self.us_state}, {self.isolation_source}, {self.collection_date}')
        #print(''.join(self.DNAseq))

import csv
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from collections import Counter
from statistics import mode
class analyzeSNPs:
    # file paths, EDIT THIS AS NEEDED FOR YOUR RESPECTIVE GENES / FILES
    sequencesPath = "sources/SeqDNA.fasta"
    attributesPath = "sources/SeqAttributes.csv"

    # initialize structure to store sequence object
    origSeqStorage = []

    # open files
    seqFile = open(sequencesPath, "r")

    # read each sequence from csv and fasta files
    with open(attributesPath, "r") as attributesFile:
        reader = csv.reader(attributesFile, delimiter=",")
        for i, line in enumerate(reader):

            # create new sequence
            newSequence = Sequence()

            # define sequence variables
            newSequence.accession = line[0]
            newSequence.species = line[1]
            newSequence.length = line[2]
            newSequence.nuc_completeness = line[3]
            newSequence.geo_location = line[4]
            newSequence.us_state = line[5]
            newSequence.isolation_source = line[6]
            newSequence.collection_date = line[7]

            currDNASeq = []
            iterator = True
            seqLine = seqFile.readline()

            while iterator:
                seqLine = seqFile.readline()
                if seqLine[0] == ">":
                    iterator = False
                else:
                    # store sequence from fasta file into object variable, stripping whitespace
                    currDNASeq.append(seqLine.strip())

            # join currDNASeq and store to object DNASeq
            newSequence.DNAseq = ''.join(currDNASeq)
            currDNASeq.clear()

            # append sequence to sequence storage
            origSeqStorage.append(newSequence)

            # print data
            newSequence.toString()

    # because we are looking for SNPs, get most common nuc length
    lengths = []
    for i in origSeqStorage:
        lengths.append(i.length)
    modeLength = mode(lengths)
    print("\nMost common length: " + modeLength)
    lengths.clear()

    # only use sequences with most common nuc length
    trimmedSeqStorage = []
    for i in origSeqStorage:
        if i.length == modeLength:
            trimmedSeqStorage.append(i)
            i.toString()

    # find mismatches
    mutationIndexes = []
    counter = 0

    while counter < len(trimmedSeqStorage) - 1:
        a = trimmedSeqStorage[counter].DNAseq
        b = trimmedSeqStorage[counter+1].DNAseq

        strIndex = 0
        for aNuc, bNuc in zip(a, b):
            if aNuc != bNuc:
                mutationIndexes.append(strIndex)
            strIndex = strIndex + 1

        counter = counter + 1

    # generate mutation location with respective mutation frequencies
    counts = Counter(mutationIndexes)

    # print counter
    print("\nNucleotide location relative to start with mutation frequencies: \n", counts)

    bufferSize = 30
    mutationLocMode = mode(mutationIndexes)
    areaOfInterest = trimmedSeqStorage[0].DNAseq[mutationLocMode-bufferSize:mutationLocMode+bufferSize:1]
    print("\nNucleotide location with most frequencies: ", mutationLocMode)
    print("Area of interest: ", mutationLocMode-bufferSize, areaOfInterest, mutationLocMode+bufferSize)

    # request blast results which returns xml
    # ***IN PROGRESS: find a way to exclude certain taxid in result_handle
    # excludeTaxID = '2697049'  (SARS-CoV-2 taxid:2697049)
    result_handle = NCBIWWW.qblast("blastn", "nt", areaOfInterest)
    print("XML retrieved")

    # parse xml
    blast_records = NCBIXML.parse(result_handle)
    print("XML parsed")

    # print blast reccord object
    for b in blast_records:
        for alignment in b.alignments:
            for hsp in alignment.hsps:
                print('****Alignment****')
                print('Sequence: ', alignment.title)
                print('Length: ', alignment.length)
                print('E value: ', hsp.expect)
                print(hsp.query[0:75] + '...')
                print(hsp.match[0:75] + '...')
                print(hsp.sbjct[0:75] + '...')

    print("\nend of program")



