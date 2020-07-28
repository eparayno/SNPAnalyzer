# BUFFERGENERATOR.PY
# AUTHOR: Erika Parayno
# DATE: 07/22/2020
# LAST EDITED: 07/28/2020
# DESCRIPTION:  Takes Sequence object, SNP of interest, and buffer size to find sequence of interest
# ASSUMPTIONS:  - SNP of interest is at location that is at least buffer_size away from start and end of sequence
#               - Sequence object exists
#               - buffer_size is a positive number


# pre-condition: takes seqObject, snpLocation, and buffer_size
# post-condition: generates buffered sequence
# return: area_of_interest
def create_buffer(seqObject, snpLocation, buffer_size):
    # get sequence starting from buffer_size upstream and ending in buffer_size downstream
    area_of_interest = seqObject.dna_seq[snpLocation - buffer_size:snpLocation + buffer_size:1]

    # print snp of interest
    print("\nNucleotide location with most frequencies: ", snpLocation)

    # print generated buffer from snp of interest
    print("Area of interest: ", snpLocation - buffer_size, area_of_interest, snpLocation + buffer_size)

    return area_of_interest
