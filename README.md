# enaget
A simple script for downloading ENA read data by accession number.

Invoke it in the directory you want the read files downloading to, it'll prompt you enter the path to a file containing the list of your accession numbers, and that's it.

If you don't want to download right away it will output a list of generated URLs in 'out.txt' which you can use with wget later.



All the script is doing is basic text manipulation to format the urls correctly.

From the ENA:

Submitted read data files are organised by submission accession number under vol1/ directory in ftp.sra.ebi.ac.uk:
ftp://ftp.sra.ebi.ac.uk/vol1/<submission accession prefix>/<submission accession>

where <submission accession prefix> contains the first 6 letters and numbers of the SRA Submission accession.
