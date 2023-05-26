# hmmsearch_dom_parser

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
	-h/--help		HELP	                Shows this help text and exits the run.

