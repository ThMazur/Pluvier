import re

import pandas as pd
import numpy as np

#STROKE_ORDER = "STKPWHRAO*-EUFRPBLGTSDZ"
STROKE_ORDER = "JZSNGDFTYXKMBPVWLHRAO*\-IEUVFRMNJPKXBLGTSDZ"

def load_df(PATH: str = "resources/verified.csv"):
    return pd.read_csv(PATH, sep=";")

def write_df(df, PATH: str = "resources/verified_filtered.csv"):
    df.to_csv(PATH, sep=";")

def compare_strings(string1, string2):
    if string1 == "":
        return True
    if string2 == "":
        return False
    if string1[0] == string2[0]:
        return compare_strings(string1[1:], string2[1:])
    else:
        return compare_strings(string1, string2[1:])

def left_replace_key(df, key, stroke):
    notation = STROKE_ORDER.split(key)
    if len(notation) == 1:
        return df
    elif len(notation) == 2:
        after = notation[1]
        behind = notation[0]
    else:
        after = key.join(notation[1:])
        behind = notation[0]

    def repla(Transcription):
        strokes = Transcription.split("/")
        res = []
        for curr in strokes:
            partitions = curr.split(key)
            if len(partitions) == 3:
                res.append(
                    f"{partitions[0]}{stroke}{key.join(partitions[1:])}"
                )
            elif len(partitions) == 2:
                condition = True
                condition &= compare_strings(partitions[0], behind)
                condition &= compare_strings(partitions[1], after)
                res.append(
                    stroke.join(partitions) if condition else curr
                )
            elif len(partitions) == 1:
                res.append(curr)
            else:
                raise KeyError(f"Stroke {curr} contains three {key}")

        return "/".join(res)

    df['Transcription'] = df['Transcription'].map(repla)
    
    return df

def right_replace_key(df, key, stroke):
    notation = STROKE_ORDER.split(key)
    if len(notation) == 1:
        return df
    elif len(notation) == 2:
        behind = notation[0]
        after = notation[1]
    else:
        behind = key.join(notation[:2])
        after = key.join(notation[2:])


    def repla(Transcription):
        strokes = Transcription.split("/")
        res = []
        for curr in strokes:
            partitions = curr.split(key)
            if len(partitions) == 3:
                res.append(
                    f"{key.join(partitions[:2])}{stroke}{partitions[2]}"
                )
            elif len(partitions) == 2:
                condition = True
                condition &= compare_strings(partitions[0], behind)
                condition &= compare_strings(partitions[1], after)
                res.append(
                    stroke.join(partitions) if condition else curr
                )
            elif len(partitions) == 1:
                res.append(curr)
            else:
                raise KeyError(f"Stroke {curr} contains three {key}")

        return "/".join(res)

    df['Transcription'] = df['Transcription'].map(repla)

    return df

def check_df_validity(df):
    consistant_stroke = re.compile(r'([#STKPWHR]*)([AO]*)([*-]*)([EU]*)([FRPBLGTSDZ]*)')
    for row in df.itertuples():
        strokes = row.Transcription.split('/')
        valid_stroke = True
        for stroke in strokes:
            valid_stroke &= consistant_stroke.fullmatch(stroke) is not None

        if not valid_stroke:
            raise KeyError(f"{row.Word} maps to an invalid stroke {row.Transcription} at {row.Index}.")
            # print(f"<<{row.Word}>> maps to an invalid stroke {row.Transcription}")

    return True


def main():
    df = load_df()
    df = left_replace_key(df, "Y", "KWR")
    df = left_replace_key(df, "M", "PH")
    df = left_replace_key(df, "N", "TPH")
    df = left_replace_key(df, "G", "TKPW")
    df = left_replace_key(df, "J", "SKWR")
    df = left_replace_key(df, "X", "KP")
    df = left_replace_key(df, "L", "HR")
    df = left_replace_key(df, "D", "TK")
    df = left_replace_key(df, "B", "PW")
    df = left_replace_key(df, "F", "TP")
    df = left_replace_key(df, "V", "W")
    df = left_replace_key(df, "Z", "SWR")

    df = right_replace_key(df, "I", "EU")
    df = right_replace_key(df, "V", "F")
    df = right_replace_key(df, "K", "BG")
    df = right_replace_key(df, "M", "PL")
    df = right_replace_key(df, "N", "PB")
    df = right_replace_key(df, "X", "BGS")
    df = right_replace_key(df, "J", "PBTPLG")

    write_df(df)

    check_df_validity(df)


# 

if __name__ == "__main__":
    exit(main())
