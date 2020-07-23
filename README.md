# SNP Analyzer
Takes GenBank data (csv and fasta), aggregates set using common attributes, and identifies SNPs. Buffered nucleotide location with most frequent mutations will be BLASTed (Basic Local Alignment Search Tool) to return top organism match.

### Future Considerations
- Need to find a way to exclude certain taxid when calling qblast to get appropriate return_handle data. If implemented successfully, the first qblast result for current/default sources would show Pandolin coronavirus instead of SARS-Cov-2. 

## Author(s)
- Erika Parayno
