from Bio.Blast import NCBIWWW
from Bio import SeqIO
record=SeqIO.read("orf24.fasta","fasta")
result_handle=NCBIWWW.qblast(
    program="blastp",
    database="nr",
    sequence=record.seq
    )
with open("blast_result.xml","w")as b:
    b.write(result_handle.read())

    print("BLAST Performed Succesfully")