#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
import os
import pandas as pd
import math
import yaml
import pyodbc
import seaborn as sns

CONFIGURATION = os.path.join("..","Src","Config.yml")

#####CONFIGURATION#####

with open(CONFIGURATION, 'r') as reader:
    config = yaml.load(reader)

####£DRAW£####
class Draw(object):
    """
        Plotting function
    """
    fontsize = 20
    def __init__(self, data):
        # Load data
        self.data = data
        # Set styles
        sns.set(style = "dark", context = "talk")

    def compute_matrix(self):
        "aggregate data"
        df_means = df.groupby(["Recency", "Frequency", "Monetary"]).agg({"ID": pd.Series.nunique,
                                                                     "RecencyValue":   pd.Series.mean,
                                                                     "FrequencyValue": pd.Series.mean,
                                                                     "MonetaryValue":  pd.Series.mean})
        df_sums = df.groupby(["Recency", "Frequency", "Monetary"]).agg({"ID": pd.Series.nunique,
                                                                     "RecencyValue":   pd.Series.sum,
                                                                     "FrequencyValue": pd.Series.sum,
                                                                     "MonetaryValue":  pd.Series.sum})
        "rename columns"
        df_means.rename(index=str,
                    columns={"ID": "TransactionCount",
                             "RecencyValue":   "RecencyMean",
                             "FrequencyValue": "FrequencyMean",
                             "MonetaryValue":  "MonetaryMean"},
                    inplace=True)
        df_sums.rename(index=str,
                   columns={"ID": "TransactionCount",
                            "RecencyValue":   "RecencySum",
                            "FrequencyValue": "FrequencySum",
                            "MonetaryValue":  "MonetarySum"},
                   inplace=True)
        "merge & return"
        ret = pd.merge(df_means, df_sums, left_index=True, right_index=True)
