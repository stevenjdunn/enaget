#!/usr/bin/env python
import subprocess
import argparse

# argparse setup
# argparse argument setup
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", required=True ,help="Path to file containing list of barcodes and their corresponding sample name.")
parser.add_argument("-o", "--output", required=True, help="Path to output destination")
parser.add_argument("--man", help="Uses a list of accession numbers to generate and optionally download read data from the ENA. -i <path_to_input_file.txt> -o <path_to_output_url_list.txt>")
args = parser.parse_args()

# Import Accession No.
with open(args.input) as f:
  accessions = f.read().splitlines()
  print accessions

# Query Download
print 'Do you also want to download the files in your current directory?'
download = raw_input("Y/N: ").lower()
yes = set(['yes','y','ye','did you ever hear the tragedy of darth plagueis the wise?'])

# Generate URL
prefix_no = list(accessions)
prefix_url = ['ftp://ftp.sra.ebi.ac.uk/vol1/' + x[:6] + '/' for x in prefix_no]
final_url = [x+y for x,y in zip(prefix_url, prefix_no)]

# Write URLs to file
with open(args.output,'w') as output:
    output.write('\n'.join(final_url))
print ''
print ''
print '##############'
print 'Output written'
print '##############'


# Download files
if download in yes:
    print ''
    print ''
    print 'Commencing download...'
    print ''
    print ''
    subprocess.call(['wget','-i', args.output])

    print ''
    print '###################'
    print 'Downloads complete'
    print '###################'
else:
    print ''
    print ''
    print 'URLs written to:',
    print args.output,
    print 'in the following directory:'
    subprocess.call('pwd')
    print ''
    print ''
    print '########'
    print 'Complete'
    print '########'
    print ''
