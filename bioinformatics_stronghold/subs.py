""" Find locations of a substring """

def substring_search(test=False):
    """ Find locaitons of a substring in a larger string """
    if not test:
        datafile = open('rosalind_subs (1).txt', 'r')
        data = datafile.readlines()
        datafile.close()

        seq = data[0].strip('\n')
        query = data[1].strip('\n')

    else:
        seq = 'GATATATGCATATACTT'
        query = 'ATAT'

    chunk_size = len(query)

    # do a first search to find positions where the sequence matches
    # the first character of the query
    start_sites = []
    for i in range(0, len(seq)):
        if seq[i] == query[0]:
            start_sites.append(i)

    positions_found = []
    positions_found_str = str()
    for pos in start_sites:
        j = pos
        k = pos + chunk_size
        if seq[j:k] == query:
            positions_found.append(pos + 1) # 1-based numbering
            positions_found_str += str(pos) + ' '

    return positions_found_str
