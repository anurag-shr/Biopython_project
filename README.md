# Sequence Analysis of ORF24 from Fowl Aviadenovirus C

## Project Overview

This project performs a **computational sequence analysis and functional inference** of **ORF24 from Fowl aviadenovirus C** using **Biopython** and standard bioinformatics workflows.  
The primary goal is to demonstrate end-to-end sequence handling, quality control, homology search, and biological interpretation based on sequence conservation.

The project is designed as an **educational and reproducible bioinformatics pipeline**, emphasizing correct methodology, documentation, and biological reasoning rather than experimental validation.

---

## Objectives

- Retrieve and process a viral ORF sequence
- Perform basic sequence quality checks
- Conduct homology search using BLASTp
- Annotate the sequence based on similarity to known proteins
- Provide a biologically sound interpretation grounded in sequence conservation

---

## Dataset / Sequence Information

- **Organism:** Fowl aviadenovirus C  
- **Gene / ORF:** ORF24  
- **Sequence Type:** Protein (amino acid sequence)  
- **Source:** Public viral genome databases (e.g., NCBI)

---

## Tools and Technologies

- **Python** (≥3.x)
- **Biopython**
  - `SeqIO`
  - `Seq`
  - `NCBIWWW` / `NCBIXML` (for BLAST handling)
- **BLASTp**
- **Git & GitHub** (version control and reproducibility)

---

## Project Workflow

1. **Sequence Retrieval**
   - Import ORF24 protein sequence in FASTA format
   - Parse and validate sequence using Biopython

2. **Quality Control**
   - Verify sequence length and composition
   - Check for invalid or ambiguous residues

3. **Homology Search**
   - Perform BLASTp against protein databases
   - Identify homologous ORFs in related adenoviruses

4. **Functional Annotation**
   - Infer potential function based on conserved homologs
   - Evaluate degree of conservation across viral species

5. **Biological Interpretation**
   - Translate computational results into biological insight

---

## Step 6: Biological Interpretation

The selected sequence represents **ORF24 from Fowl aviadenovirus C**.  
Based on BLASTp analysis, this protein shows similarity to ORF proteins found in other related adenoviruses, suggesting that it is **conserved across viral species**.

The conservation of ORF24 indicates that it is likely to have an **essential role in the viral life cycle**. Proteins preserved across related viruses are typically involved in critical viral processes necessary for survival and propagation.

Although the exact molecular function of ORF24 has not been experimentally confirmed, the observed sequence similarity suggests potential involvement in **viral replication**, **structural organisation**, or **virus–host interactions**.

Overall, this functional prediction is derived from **homology-based inference and sequence conservation**, and therefore represents a **computational hypothesis rather than experimental validation**.

---

## Limitations

- No wet-lab or experimental validation is included
- Results should be interpreted as **predictive**, not definitive

---


