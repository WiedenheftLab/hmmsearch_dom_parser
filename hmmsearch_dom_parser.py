#!/software/mambaforge/envs/Murat_scripts/bin/python

import argparse
import subprocess
import sys
import os
import textwrap

try:
    import tqdm
except ImportError, e:
    print "tqdm module is not installed! Please install tqdm and try again."
    sys.exit()


parser = argparse.ArgumentParser(prog='python hmmsearch_dom_parser.py',
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog=textwrap.dedent('''\

Author: Murat Buyukyoruk

Associated lab: Wiedenheft lab

        hmmsearch_dom_parser help:

This script is developed parse hmmsearch domain table outfile (domtblout) to extract domain positions in each accession based on i-Evalue.

SeqIO and Seq packages from Bio is required to fetch sequences. Additionally, tqdm is required to provide a progress bar since some multifasta files can contain long and many sequences.

Syntax:

        python hmmsearch_dom_parser.py -i demo_domtblout.txt -o out_summary.txt -e 0.001

hmmsearch_dom_parser dependencies:

	tqdm                                                    refer to https://pypi.org/project/tqdm/

Input Paramaters (REQUIRED):
----------------------------
	-i/--input		domtblour		Specify a hmmsearch domtblout file

	-o/--output		Output file	        Specify a output filename.
	
	-e/--evalue     	i-Evalue            	Specify an E-value cut off (i.e., 0.001).

Basic Options:
--------------
	-h/--help		HELP			Shows this help text and exits the run.

      	'''))
parser.add_argument('-i', '--input', required=True, type=str, dest='filename', help='Specify a hmmsearch domtblout file.\n')
parser.add_argument('-e', '--evalue', required=True, type=float, dest='E_value', help='Specify an E-value cut off (i.e., 0.001).\n')
parser.add_argument('-o', '--out', required=True, type=str, dest='out', help='Specify a output file name.\n')

results = parser.parse_args()
filename = results.filename
E_value = results.E_value
out = results.out

os.system("> " + out)

proc = subprocess.Popen("wc -l < " + filename, shell=True, stdout=subprocess.PIPE, )
length = int(proc.communicate()[0].split('\n')[0])

f = open(out, 'a')
sys.stdout = f

print "Accession\ti-Evalue\tEnv_start\tEnv_stop\tProt_len"

with tqdm.tqdm(range(length)) as pbar:
    with open(filename,'rU') as file:
        for line in file:
            pbar.update()
            if line[0] != "#" and len(line.split())!=0:
                arr = line.split(" ")
                new_list = [x for x in arr if x != '']
                arr = new_list
                acc = arr[0]
                seq_len = arr[2]
                iE = arr[12]
                temp = float(iE)
                env_start = arr[19]
                env_stop = arr[20]

                if(temp <= E_value):
                    print acc + "\t" + iE + "\t" + env_start + "\t" + env_stop + "\t" + seq_len
