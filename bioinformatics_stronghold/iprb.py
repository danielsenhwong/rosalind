from __future__ import division

def iprb(test=False):
    if not test:
        f = open('rosalind_iprb.txt', 'r')
        l = f.readline()
        f.close()

        ls = l.split()
    else:
        ls = [2, 2, 2]

    d = int(ls[0]) # dominant homozygous
    h = int(ls[1]) # heterozygous
    r = int(ls[2]) # recessive homozygous
    t = d + h + r # total population

    # probability of phenotypic dominant offspring
    p_d1 = (d / t) # pick homozygous dominant first parent
    p_h1d2 = (h / t) * (d / (t - 1)) # het first parent, dom second
    p_h1h2 = (h / t) * ((h - 1) / (t - 1)) * 0.75 # both het, 0.75 from punnett
    p_h1r2 = (h / t) * (r / (t - 1)) * 0.5 # het first, rec second
    p_r1d2 = (r / t) * (d / (t - 1)) # rec dom
    p_r1h2 = (r / t) * (h / (t - 1)) * 0.5 # rec het
            
    p_dom = p_d1
    p_het = p_h1d2 + p_h1h2 + p_h1r2
    p_rec = p_r1d2 + p_r1h2
                                
    p_total = p_dom + p_het + p_rec
                                        
    return p_total
