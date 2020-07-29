# SNP Analyzer
Takes GenBank data (csv and fasta), aggregates set using common lengt, and identifies SNPs. Buffered nucleotide location with most frequent mutations will be BLASTed (Basic Local Alignment Search Tool) to return top organism match.

## Getting Started
These instructions will get you a copy of the calculator onto your local machine. 

### Prerequisites
- Make sure [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git), [Python](https://www.python.org/downloads/), and [BioPython](https://biopython.org/wiki/Download are installed in your environment

### Installing 
Run the following command in working directory: 
```
$ git clone https://github.com/eparayno/SNPAnalyzer.git
```

### Running the program
Run the main class:
```
$ python3 SnpAnalyzer.py
```

### Future Considerations
- Need to find a way to exclude certain taxid when calling qblast to get appropriate return_handle data. If implemented successfully, the first qblast result for current/default sources would show Pandolin coronavirus instead of SARS-Cov-2. 
- Instead of creating set based on common length, utilize pairwise sequence alignment to allow for analysis of larger, more varied sequences.

## Author(s)
- Erika Parayno
