"""
rosalind.py

Common functions used to support solutions for problems at rosalind.info
"""

def import_data(problem, attempt=1, strip_newlines=True, parse_fasta=False):
    """ Import data from problem dataset, data returned as list of lines """
    if attempt > 1:
        problem += ' (' + str(attempt - 1) + ')'

    datafile = open('rosalind_' + problem + '.txt', 'r')
    data = datafile.readlines()
    datafile.close()

    # strip newlines
    if strip_newlines:
        for linenum in range(0, len(data)):
            data[linenum] = data[linenum].strip('\n')

    # convert fasta format
    if parse_fasta:
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

        data = {'raw_data': data,
                'dna_seqs': dna_seqs}

    return data
