#!/usr/bin/python3
import sys
import pandas as pd

if not len(sys.argv) == 4:
    print("Precisa chamar com três argumentos, nome arquivo 1, e nome arquivo 2, e nome de arquivo saida")
    exit()

csv1Name = sys.argv[1]
csv2Name = sys.argv[2]

csv1DF = pd.read_csv(csv1Name, delimiter=',', low_memory=False)
csv2DF = pd.read_csv(csv2Name, delimiter=',', low_memory=False)
counter = 0
try:
    for line in csv1DF.itertuples():
        if pd.isna(line.release_date) and not pd.isna(csv2DF.loc[line.Index, 'release_date']):
            print(f'{counter}não tinha, mas conseguiu buscar {line.title}')
            csv1DF.loc[line.Index] = csv2DF.loc[line.Index]
    csv1DF.to_csv(sys.argv[3])
    counter+=1
except:
    csv1DF.to_csv(sys.argv[3])

