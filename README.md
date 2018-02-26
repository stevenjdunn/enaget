# enaget
A simple script for downloading ENA fastq data by accession number.

### Usage
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Path to file containing list of accession numbers.
  -o OUTPUT, --output OUTPUT
                        Path to output fastq files.
  -l, --list            Generates a list of URL's for retrieval at a later
                        time (i.e. does not invoke wget).


### Input File
The script is expecting a text file with a list of accession numbers, eg:

    ACC000001
    ACC000002
    ACC000003
    
It won't work with study numbers - if you want to retrieve all data in a particular study, or a single acession number, I'd recommmend using ENA's own scripts: https://github.com/enasequence/enaBrowserTools

### How does it work?

All the script is doing is basic text manipulation to format the urls correctly.

From the ENA:

Submitted read data files are organised by submission accession number under vol1/ directory in ftp.sra.ebi.ac.uk:
ftp://ftp.sra.ebi.ac.uk/vol1/ [submission accession prefix] / [submission accession]

where [submission accession prefix] contains the first 6 letters and numbers of the SRA Submission accession.
