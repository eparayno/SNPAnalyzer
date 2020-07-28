# SEQUENCEBLASTER.PY
# AUTHOR: Erika Parayno
# DATE: 07/22/2020
# LAST EDITED: 07/28/2020
# DESCRIPTION:  Takes sequence and uses qBlast to find organism match from National Center for Biotechnology Information
# ASSUMPTIONS:  - Sequence type is valid nt
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML


# pre-condition: area_of_interest is a valid type of nt
# post-condition: will print each result with sequence comparison
# return: none
def blast_sequence(area_of_interest):
    # request blast results which returns xml
    # ***IN PROGRESS: find a way to exclude certain taxid in result_handle
    # excludeTaxID = '2697049'  (SARS-CoV-2 taxid:2697049)
    result_handle = NCBIWWW.qblast("blastn", "nt", area_of_interest)
    print("XML retrieved")

    # parse xml
    blast_records = NCBIXML.parse(result_handle)
    print("XML parsed")

    # print blast record object
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
