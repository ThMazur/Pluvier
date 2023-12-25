import pandas as pd
from tqdm import tqdm

from src.constants import * 

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

    # lex_it = tqdm(lexicon.itertuples(), total=lexicon.shape[0])
    print(lexicon[lexicon['phon'].notna() & lexicon['phon'].str.contains('°')])

if __name__ == '__main__':
    exit(main())