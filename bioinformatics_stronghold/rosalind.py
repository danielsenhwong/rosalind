"""
rosalind.py

Common functions used to support solutions for problems at rosalind.info
"""

def import_data(problem, attempt=1, strip_newlines=True):
    """ Import data from problem dataset, data returned as list of lines """
    if attempt > 1:
        problem += ' (' + str(attempt - 1) + ')'

    datafile = open('rosalind_' + problem + '.txt', 'r')
    data = datafile.readlines()

    if strip_newlines:
        for linenum in range(0, len(data)):
            data[linenum] = data[linenum].strip('\n')

    datafile.close()

    return data
