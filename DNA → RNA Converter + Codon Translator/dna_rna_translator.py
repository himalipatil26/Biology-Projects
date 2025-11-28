# DNA → RNA Converter + Codon Translator

# RNA Codon Table
CODON_TABLE = {
    "UUU": "Phe", "UUC": "Phe",
    "UUA": "Leu", "UUG": "Leu",

    "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
    "AUU": "Ile", "AUC": "Ile", "AUA": "Ile",
    "AUG": "Met (Start)",
    
    "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",

    "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser",
    "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
    "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
    "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",

    "UAU": "Tyr", "UAC": "Tyr",
    "UAA": "STOP", "UAG": "STOP",
    "CAU": "His", "CAC": "His",
    "CAA": "Gln", "CAG": "Gln",

    "AAU": "Asn", "AAC": "Asn",
    "AAA": "Lys", "AAG": "Lys",
    "GAU": "Asp", "GAC": "Asp",
    "GAA": "Glu", "GAG": "Glu",

    "UGU": "Cys", "UGC": "Cys",
    "UGA": "STOP",
    "UGG": "Trp",

    "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
    "AGU": "Ser", "AGC": "Ser",
    "AGA": "Arg", "AGG": "Arg",
    "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly"
}

# Validate DNA sequence
def is_valid_dna(dna):
    return all(base in "ATGC" for base in dna)

# DNA → RNA
def dna_to_rna(dna):
    return dna.replace("T", "U")

# RNA → Amino Acids
def rna_to_protein(rna):
    protein = []
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        if len(codon) < 3:
            break
        amino = CODON_TABLE.get(codon, "Invalid")
        protein.append(amino)
        if amino == "STOP":
            break
    return protein

# Print Codon Table
def print_codon_table():
    print("RNA Codon Table:")
    for codon, amino in CODON_TABLE.items():
        print(f"{codon}: {amino}")
        

# ---------- SAMPLE RUN ----------
if __name__ == "__main__":
    dna = input("Enter DNA sequence (A,T,G,C only): ").upper()

    if not is_valid_dna(dna):
        print("Invalid DNA sequence!")
    else:
        rna = dna_to_rna(dna)
        print("RNA Sequence:", rna)

        protein = rna_to_protein(rna)
        print("Amino Acid Sequence:", "-".join(protein))

        print("\n--- CODON TABLE ---")
        print_codon_table()

