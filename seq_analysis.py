#step 1
from Bio import SeqIO
record=SeqIO.read("orf24.fasta","fasta")
print(record.id)
print(record.description)
print(len(record))

from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
record=SeqIO.read("orf24.fasta","fasta")
gc_content= gc_fraction(record.seq)*100
print(f"{record.id}:{gc_content:.2f}%")
