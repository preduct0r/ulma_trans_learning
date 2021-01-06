import pandas as pd
import numpy as np
from glob import glob


def class_define(arousal, valence):
    dict_change = {1: -1, 2: -1, 3: 0, 4: 1, 5: 1}
    ar, val = dict_change[int(arousal)], dict_change[int(valence)]
    dict_class = {(-1, -1): 0, (-1, 0): 1, (0, -1): 3, (-1, 1): 2, (0, 0): 4, (0, 1): 5, (1, 1): 8, (1, 0): 7,
                  (1, -1): 6}
    return dict_class[(ar, val)]


def add_arvalmix(path_to_meta):
    for meta in glob(path_to_meta + "/*.csv"):
        df = pd.read_csv(meta, sep=';')

        temp = [x if x <=5  else 5 for x in df['valence'].map(round) ]
        df['arvalmix'] = [class_define(x,y) for x,y in zip(df['activation'].map(round), temp)]
        df.to_csv(meta, index=False, sep=';')
