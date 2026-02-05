from Bio import SeqIO
record=SeqIO.read("orf24.fasta","fasta")
print(record.id)
print(record.description)
print(len(record.seq))
print(record.seq)

from Bio import Entrez
from Bio import SeqIO
Entrez.email="clustrasubs@gmail.com"
accession_id="UOF83159"
print(f"Retrieving data for {accession_id} from GenBank.")
with Entrez.efetch(db="protein",id=accession_id,rettype="gb",retmode="text")as handle:
    record=SeqIO.read(handle,"genbank")
    print("\n---Functional Annotations---")
    print(f"Predicted Product:{record.description}")
    print(f"Organism Relevance:{record.annotations.get('source')}")
for feature in record.features:
    if feature.type=="Protien":
        product=feature.qualifiers.get('product',['No Product Listed'])[O]
        print(f"Biological Role:{product}")