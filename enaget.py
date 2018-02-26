#!/usr/bin/env python
import subprocess
import argparse
import os

# Version
_version_ = "0.1"

# argparse argument setup
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", required=True ,help="Path to file containing list of accession numbers.")
parser.add_argument("-o", "--output", required=True, help="Path to output fastq files.")
parser.add_argument("-l", "--list", action="store_true", help="Generates a list of URL's for retrieval at a later time (i.e. does not invoke wget).")
parser.add_argument("--man", help="Uses a list of accession numbers to generate and optionally download read data from the ENA. -i <path_to_input_file.txt> -o <path_to_output_url_list.txt>")
args = parser.parse_args()

# Directory creation and orientation
invoked_from = os.getcwd()
if not os.path.exists(args.output):
    os.mkdir(args.output)
    print 'Output directory created:',
else:
    print 'Output will be placed in:',
os.chdir(args.output)
output_path = os.getcwd()
os.chdir(invoked_from)
print output_path
print ''

# Import Accession No.
with open(args.input) as f:
  accessions = f.read().splitlines()

# Generate URL
prefix_no = list(accessions)
prefix_url = ['ftp://ftp.sra.ebi.ac.uk/vol1/fastq/' + x[:6] + '/' for x in prefix_no]
final_url = [x+y for x,y in zip(prefix_url, prefix_no)]

# Write URLs to file
output_file = output_path + '/url_list.txt'
with open(output_file,'w') as output:
    output.write('\n'.join(final_url))
print ''
print ''
print '##############'
print 'Output written'
print '##############'
print ''
print 'URLs written to:',
print output_file


# Download files
if not args.list:
    print ''
    print ''
    print 'Commencing download...'
    print ''
    print ''
    subprocess.call(['wget', '-m', '-nd', '-i', output_file, '-P', output_path])

    print ''
    print '###################'
    print 'Downloads complete'
    print '###################'
print ''
print ''
print ''
print ''
print 'Author: www.github.com/stevenjdunn'
print ''
print ''
print '################'
print 'EnaGet Complete!'
print '################'
