# enaget
A simple script for downloading ENA fastq data by accession number.

### Usage

    -h, --help          show this help message and exit
    -i INPUT, --input INPUT
                        Path to file containing list of accession numbers.
    -o OUTPUT, --output OUTPUT
                        Path to output fastq files.
    -l, --list          Generates a list of URL's for retrieval at a later
                        time (i.e. does not invoke wget).
    -r, --remove        Removes temporary files generated during URL resolution


### Input File
The script is expecting a text file with a list of accession numbers, eg:

    ACC000001
    ACC000002
    ACC000003
    SRR589123
  
It will retrieve any fastq files stored under that accession number only. The script can use any accession number attributed to a single sample.

It won't work with study numbers - if you want to retrieve all data in a particular study, or a single acession number, I'd recommmend using ENA's own scripts: https://github.com/enasequence/enaBrowserTools - this is also useful if you want something other than fastqs.

### How does it work?

The script queries ENA using the provided accession numbers and locates the correpsonding file report. From this report, the fastq URL is extracted and handed to wget. 

This *should* mean that you can use any one of the sample accession numbers ENA uses, including cross archived SRA accessions, secondary accessions etc. 

It's worked on everything I've passed to it, just let me know if you're having problems.
