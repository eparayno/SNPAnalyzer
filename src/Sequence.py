# SEQUENCE.PY
# AUTHOR: Erika Parayno
# DATE: 07/22/2020
# LAST EDITED: 07/28/2020
# DESCRIPTION:  Class containing Sequence attributes and data. Contains constructor and print menthod.
# ASSUMPTIONS:  - None


class Sequence:

    # pre-condition: sequence object is called
    # post-condition: initializes attributes to empty string values
    # return: none
    def _init_(self):
        self.accession = ""
        self.species = ""
        self.length = ""
        self.nuc_completeness = ""
        self.geo_location = ""
        self.us_state = ""
        self.isolation_source = ""
        self.collection_date = ""
        self.dna_seq = ""

    # pre-condition: none
    # post condition: prints attributes of self in formatted version
    # return: none
    def to_string(self):
        print(
            f'Accession[{self.accession}] = {self.species}, {self.length}, {self.nuc_completeness}, {self.geo_location}, {self.us_state}, {self.isolation_source}, {self.collection_date}')
