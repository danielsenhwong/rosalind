# Bioinformatics Stronghold
# Problem revc

s = 'AATACATTTAATCGGAGGGCGCGACCCTATAGGTCCTAACCAAATCTTACCAAGATTTTGGTGCAGGGAGTGCGGGAGTATTCGCAAGAAATAGGGGCCCCAAGCTAATGCATCCTGAGCTTACCTGGGTAGTGAATCCATCTTCTAGACATGTATTATGTGACACGTCATGCCACCCCATGTATTGTCGGATACTGCGCTAGCGCGTTGTCCCGGCAGGCCAAGCACTAGTTACTCCGAGAAGTTGTTACGCACCCATCATCTATACGGGGTGACTATCTTAGTGGAGGGGGGCTGTCGGAGAAGCCCTTTTCAGTTCCATATAGGATTTATACCCATGGAACGAACCCCATGCGACGAGATACGAAAGGGAGGTGTTGGCACCCTAATGGACAGCCAGCGCCTTATACACGGTAATAGTAAATCCAGCCAAATTTGCGACACTGCTTGAAGAGATACTATTCTTAACAGCGATAACGTAACGACGCATACGAGCTAACCCGCGGTACCATTGAAGCCGTACGGCTAGGCTGGCCGCACATCTCAGACAAAACATCCTCTGTACTAACAGCTGTTCCAATACGAAGGTAAAGAACGATCTCACTCAGGACAGGGAGATCGTCGCGGCTCGGAACCGTCAATTGAACGAAAATTTGAACTCAGCCCGCTCGGTGGGACGTTTATCGTAGTTCAGTCAACACTGGCCAAACCGCTCAGACACAAGATCTTGAATTCTCGGTCGAGTTGCTCAGGTTGGTCAGTCAAGGTCTATCACCCGGGTGTCGTGGAGTAGGTGCCGGTTAGATTAAAGGGGCGTAATTCCGTTCCATAGGCAAATTAGCATACGGGAGACCGAACTCGTGGGCTT'
revc = ''

for l in s:
    if l == 'A':
        revc = 'T' + revc
    elif l == 'T':
        revc = 'A' + revc
    elif l == 'C':
        revc = 'G' + revc
    elif l == 'G':
        revc = 'C' + revc

print revc