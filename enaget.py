#!/usr/bin/env python
import subprocess
import argparse
import os
import sys

# Version
_version_ = "0.3"

# argparse argument setup
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", required=True ,help="Path to file containing list of accession numbers.")
parser.add_argument("-o", "--output", required=True, help="Path to output fastq files.")
parser.add_argument("-l", "--list", action="store_true", help="Generates a list of URL's for retrieval at a later time (i.e. does not invoke wget).")
parser.add_argument("-r", "--remove", action="store_true", help="Removes intermediate files (i.e. temp folder in output path)")
parser.add_argument("-p", "--parallel", action="store_true", help="Executes wget in parallel for faster downloads.")
args = parser.parse_args()

# Space Saving
def scriptend():
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
    sys.exit(1)

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
temp = output_path + '/temp'
if not os.path.exists(temp):
    os.mkdir(temp)
else:
    print ''
    print 'Output directory contains files which will intefere with script and risk being overwritten.'
    print ''
    print 'Select a new output directory, or remove the old one.'
    print ''
    sys.exit(1)

# Import Accession No.
with open(args.input) as f:
  accessions = f.read().splitlines()

# Generate warehouse report links and write to file
prefix_no = list(accessions)
warehouse = ['https://www.ebi.ac.uk/ena/data/warehouse/filereport?accession=' + x + '&result=read_run&fields=fastq_ftp&download=txt' for x in prefix_no]
ENA_warehouse = temp + '/meta_fetch.txt'
ENA_data = temp + '/ENA_data.csv'
with open(ENA_warehouse, 'w') as output:
    output.write('\n'.join(warehouse))

# Fetch resolved ftp addresses
print ENA_warehouse
print ENA_data
subprocess.call(['wget', '-i', ENA_warehouse, '-O', ENA_data])

# Format CSV for url resolution
ENA_scrubbed = temp + '/ENA_scrubbed.csv'
URLs = output_path + '/URL_list.txt'
with open(ENA_scrubbed, 'w') as csv:
    for line in file(ENA_data):
        if 'fastq_ftp' not in line:
            csv.write(line)
with open(ENA_scrubbed, 'r') as csv:
    rawcsv = csv.read()
rawcsv = rawcsv.replace(';', '\n')
with open(URLs, 'w') as csv:
    csv.write(rawcsv)
print ''
print ''
print '##############'
print 'Output written'
print '##############'
print ''
print 'URLs written to:',
print URLs

# File cleanup
if args.remove:
    import shutil
    print ''
    print 'Removing temp files...'
    print ''
    shutil.rmtree(temp)
    print ''
    print 'Done!'

# --list exit
if args.list:
    print 'Exit #1'
    scriptend()


# Download files 
if not args.list and not args.parallel:
    print ''
    print ''
    print 'Commencing download...'
    print ''
    print ''
    subprocess.call(['wget', '-c', '-t', '5','-nd', '-i', URLs, '-P', output_path])
    print ''
    print '###################'
    print 'Downloads complete'
    print '###################'
    scriptend()

# Parallel download of files 
if args.parallel and not args.list:
    print ''
    print ''
    print 'Commencing download...'
    print ''
    print ''
    cat = subprocess.Popen(['cat', URLs], stdout=subprocess.PIPE)
    subprocess.call(['parallel', '--gnu', 'wget', '{}', '-P', output_path], stdin=cat.stdout)
    print ''
    print '###################'
    print 'Downloads complete'
    print '###################'
    scriptend()
