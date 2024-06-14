# Stats-and-ORF
Python Script to determine N50 and GC content of sequencing data, followed by ORF identification using prodigal (https://github.com/hyattpd/Prodigal)


Input is sequences in FASTA format, output is statistics on sequencing quality (N50, GC 
content, number of sequences, shortest, longest, median, mean) as well as all open reading 
frames as identified by prodigal.

    python Stats-and-ORF.py <input_file.fasta>
