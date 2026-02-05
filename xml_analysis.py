from Bio.Blast import NCBIXML
with open("blast_result.xml")as b:
    blast_record=NCBIXML.read(b)
    print(len(blast_record.alignments))
for A in blast_record.alignments:
    print(A.title)
    print(A.length)
    print(len(A.hsps))
for hsp in A.hsps:
    print(f"Identities:{hsp.identities}/{hsp.align_length}")
    print("Query range:",hsp.query_start,"_",hsp.query_end)
    print(f"E-value:{hsp.expect}")
    print(f"Bit Score:{hsp.bits}")
if hsp.expect<1e-10:
    print(f"Accession:{A.accession}")
    print(f"E-value:{hsp.expect}")