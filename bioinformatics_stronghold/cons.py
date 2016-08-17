""" Solution for cons problem """
from rosalind import import_data

def cons_seq(test=False, attempt_num=1):
    """ Build a consensus sequence from several DNA sequences """
    if not test:
        data = import_data(problem='cons', attempt=attempt_num)

        # convert fasta format
        temp_dna_id = str()
        dna_seqs = {}
        for linenum in range(0, len(data)):
            if data[linenum][0] != '>':
                if temp_dna_id in dna_seqs:
                    dna_seqs.update({temp_dna_id: dna_seqs[temp_dna_id] + \
                            data[linenum].strip('\n')})
                else:
                    dna_seqs[temp_dna_id] = data[linenum].strip('\n')
            else:
                temp_dna_id = data[linenum][1:len(data[linenum])]

    else:
        data = ['>Rosalind_1',
                'ATCCAGCT',
                '>Rosalind_2',
                'GGGCAACT',
                '>Rosalind_3',
                'ATGGATCT',
                '>Rosalind_4',
                'AAGCAACC',
                '>Rosalind_5',
                'TTGGAACT',
                '>Rosalind_6',
                'ATGCCATT',
                '>Rosalind_7',
                'ATGGCACT']

        # Build a dictionary of the sequences with names as keys
        dna_seqs = {}
        for i in range(0, len(data), 2):
            if data[i][0] == '>':
                start_str = 1
            else:
                start_str = 0

            dna_seqs[data[i][start_str:len(data[i])]] = data[i+1]

    # Count appearance of each base by position
    dna_len = len(dna_seqs.values()[0])
    count_list = []
    consensus_seq = str()

    for pos in range(0, dna_len):
        base_count = {
            'A': 0,
            'C': 0,
            'G': 0,
            'T': 0}

        # count
        for dna in dna_seqs.values():
            if dna[pos] == 'A':
                base_count['A'] += 1
            elif dna[pos] == 'C':
                base_count['C'] += 1
            elif dna[pos] == 'G':
                base_count['G'] += 1
            elif dna[pos] == 'T':
                base_count['T'] += 1

        # add the base to the consensus sequence
        consensus_seq += max(base_count, key=base_count.get)

        # append the base count to the list of counts
        count_list.append(base_count)

    # make a pretty text table to show counts
    count_str = str()
    bases = ['A', 'C', 'G', 'T']
    for base in bases:
        count_str += base + ': '

        for col in range(0, dna_len):
            count_str += str(count_list[col][base])

            if col == dna_len - 1:
                count_str += '\n'
            else:
                count_str += ' '

    output = {'consensus_sequence': consensus_seq,
              'count_list': count_list,
              'count_str': count_str}

    output_file = open('cons_output.txt', 'w')
    output_file.write(consensus_seq + '\n')
    output_file.write(count_str)
    output_file.close()

    return output

