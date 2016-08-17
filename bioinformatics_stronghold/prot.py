"""Translate an RNA sequence into a protein sequence"""
# RNA codon table import
RNA_CODON_TABLE = open('rna_codon_table.txt', 'r')
LINE = RNA_CODON_TABLE.readlines()
RNA_CODON_TABLE.close()
RNA_CODONS = {}
for line in LINE:
    parts = line.split()

    for i in range(0, (len(parts) / 2)):
        j = (2 * i) # codon index
        k = j + 1 # AA index

        RNA_CODONS[parts[j]] = parts[k]

def translate_rna(test=False):
    """Translate an RNA sequence into a protein sequence"""
    if not test:
        datafile = open('rosalind_prot.txt', 'r')
        data = datafile.readline().strip('\n')
        datafile.close()
    else:
        data = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'

    codons = []
    prot = str()
    for index in range(0, len(data), 3):
        codons.append(data[index:index+3])
        if RNA_CODONS[data[index:index+3]] == 'Stop':
            break
        else:
            prot += RNA_CODONS[data[index:index+3]]

    return prot
