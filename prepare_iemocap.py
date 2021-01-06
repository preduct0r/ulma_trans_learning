import pandas as pd
import numpy as np


def class_define(arousal, valence):
    dict_change = {1: -1, 2: -1, 3: 0, 4: 1, 5: 1}
    ar, val = dict_change[int(arousal)], dict_change[int(valence)]
    dict_class = {(-1, -1): 0, (-1, 0): 1, (0, -1): 3, (-1, 1): 2, (0, 0): 4, (0, 1): 5, (1, 1): 8, (1, 0): 7,
                  (1, -1): 6}
    return dict_class[(ar, val)]


df = pd.read_csv('/home/den/datasets/iemocap/meta.csv', sep=';')
df['activation'] = df['activation'].map(round)
df['valence'] = df['valence'].map(round)
df['valence'] = [x if x <=5  else 5 for x in df['valence'] ]

df['arvalmix'] = [class_define(x,y) for x,y in zip(df['activation'], df['valence'])]

print(df)