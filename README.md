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
    -p, --parallel      Executes wget in parallel for faster downloads.

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

### I wanna go fast
Use the -p flag to invoke wget under GNU parallel. This will usually spawn as many wget processes as you have available threads, and allows multiple concurrent downloads instead of a one-by-one approach. Useful for high speed connections or when downloading a lot of files. I've found that this script in general is a lot faster than fastq-dump by default, and using --parallel/-p is a different league entirely.

###  How do I add options to wget?
Edit the script at line 117. Additional flags must be enclosed in quotation marks, with any spaces demarked with commas. Alternatively, use the -l flag to simply generate a list of URLs that you can retrieve on your own.
