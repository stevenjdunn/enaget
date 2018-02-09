#!/usr/bin/env python
import subprocess

# Import Accession No.
inputfile = raw_input("Path to accession no. text file:")
with open(inputfile) as f:
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
with open('out.txt','w') as output:
    output.write('\n'.join(final_url))

print '##############'
print 'Output written'
print '##############'
print ''
# Download files
if download in yes:
    subprocess.call(['wget','-i','out.txt'])

    print ''
    print '###################'
    print 'Downloads complete'
    print '###################'
else:
    print 'URLs written to out.txt in:'
    subprocess.call('pwd')
    print ''
    print '########'
    print 'Complete'
    print '########'
    print ''
