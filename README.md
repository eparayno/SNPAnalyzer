# SNP Analyzer
Takes GenBank data (csv and fasta), aggregates set using common attributes, and identifies SNPs. Buffered nucleotide location with most frequent mutations will be BLASTed (Basic Local Alignment Search Tool) to return top organism match.

## Getting Started
These instructions will get you a copy of the program onto your local machine. 

### Prerequisites
Make sure [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) is installed in your computer. 

### Installing 
Run the following command in working directory: 
```
$ git clone https://github.com/eparayno/SNPAnalyzer.git
```

## Running Program
```
$ python3 SNPAnalyzer.py
```

### Future Considerations
- Need to find a way to exclude certain taxid when calling qblast to get appropriate return_handle data. With current sources, the first qblast result should show Pandolin coronavirus instead of SARS-Cov-2. 

## Author(s)
- Erika Parayno
