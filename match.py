#!/usr/bin/env python3

from difflib import get_close_matches
import pandas as pd

voc = pd.read_excel("voc.xlsx")


def fuzzy_vlookup(manual_input_to_parse: str, voc: pd.DataFrame) -> str:
    """
    Will compare input string with first column of voc,
    find best match
    and then return corresponding value from second column
    """
    return voc.loc[
        voc[voc.columns[0]]
        == get_close_matches(
            manual_input_to_parse, voc[voc.columns[0]].values, n=1, cutoff=0.0
        )[0]
    ][voc.columns[1]].values[0]


df = pd.read_clipboard(sep="\t", header=None)
df[df.columns[0]].apply(lambda x: fuzzy_vlookup(x, voc=voc)).to_clipboard(
    index=False, header=False
)
