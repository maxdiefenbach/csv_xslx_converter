#!/usr/bin/env python

import sys
import os
import pandas as pd

def csv2xlsx():
    fin = sys.argv[1]
    df = pd.read_csv(fin)
    df.to_excel(os.path.splitext(fin)[0] + '.xlsx', index=False)

def xlsx2csv():
    fin = sys.argv[1]
    df = pd.read_excel(fin)
    df.to_csv(os.path.splitext(fin)[0] + '.csv', index=False)
