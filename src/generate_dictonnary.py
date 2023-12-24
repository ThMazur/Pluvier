from collections import defaultdict 

import json
import pandas as pd
from tqdm import tqdm

from constants import *

def generate_entry(word):
    syllables = word.syll.split('-')
    structs = word._22.split('-')
    stroke = ''
    for syllable, struc in zip(syllables, structs):
        stroke += f'{syllable}/'

    return stroke[:-1]

def resolve_conflict(stroke, conflict):
    return {stroke: conflict[0].ortho}

def main():
    lexicon = pd.read_csv(LEXICON_PATH, sep='\t')
    lexicon = lexicon.drop(columns=["freqlemfilms2",
                                "freqfilms2",
                                "cvcv",
                                "orthrenv",
                                "phonrenv",
                                "cgramortho",
                                "deflem",
                                "defobs",
                                "old20",
                                "pld20"])

    pluvier_dictionnary_with_conflict = defaultdict(list)
    lex_it = tqdm(lexicon.itertuples(), total=lexicon.shape[0])
    for word in lex_it:
        lex_it.set_description(f'Processing {word.ortho}')
        pluvier_dictionnary_with_conflict[generate_entry(word)].append(word)

    pluvier_dictionnary = {}
    conflicts_it = tqdm(pluvier_dictionnary_with_conflict.items())
    for key, conflict in conflicts_it:
        conflicts_it.set_description(f'resolving {len(conflict)} for stroke {key}')
        pluvier_dictionnary.update(resolve_conflict(key, conflict))
    
    with open('dictionnaries/Pluvier_main.json', 'w', encoding='utf8') as file:
        file.write(json.dumps(pluvier_dictionnary, indent=1, ensure_ascii=False))

if __name__ == '__main__': 
    exit(main())