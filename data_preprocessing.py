# -*- coding: utf-8 -*-
"""data_preprocessing.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Nt0hxXdf5qY35bZq9_mpDlnn8OMqXdoR
"""

def preprocess_text(text):

    clean_text = text.lower().strip()
    return clean_text

def table_to_text(table):
   ## """Converts a table into a passage"""##
    passage = ' '.join([' '.join(preprocess_text(str(cell)) for cell in row.values()) for row in table])
    return passage

def preprocess_table_for_dtr(table):
  ##
    return table