import pandas as pd

def readAll():
    tbl0 = pd.read_csv('tbl0.tsv', sep='\t')
    tbl1 = pd.read_csv('tbl1.tsv', sep='\t')
    tbl2 = pd.read_csv('tbl2.tsv', sep='\t')
    return (tbl0, tbl1, tbl2)
