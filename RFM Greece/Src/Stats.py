#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
import os
import pandas as pd
import yaml
import pyodbc

CONFIGURATION = os.path.join("..","Src","Config.yml")

#####CONFIGURATION#####

with open(CONFIGURATION, 'r') as reader:
    config = yaml.load(reader)

####£DRAW£####
class Stats(object):
    """
        Summarise statistics table
    """
    def __init__(self, data):
        self.data = data

    def calculate(self):
        """
            Calculate table
        """
        # Fetch relevant data
        stat = self.data[["RecencyValue","FrequencyValue","MonetaryValue","Segment"]].copy()
        temp = stat.groupby("Segment").count()

        # Get stats
        temp["Average Customer Value (Over time period)"] = stat.groupby("Segment")["MonetaryValue"].mean()
        temp["Total Customers"] = stat.groupby("Segment")["FrequencyValue"].count()
        temp["Average Transaction Value"] = stat.groupby("Segment")["MonetaryValue"].mean()/stat.groupby("Segment")["FrequencyValue"].mean()
        temp["Average Transaction Frequency (Over time period)"] = stat.groupby("Segment")["FrequencyValue"].mean()
        temp["Average days since last shop"] = stat.groupby("Segment")["RecencyValue"].mean()

        # Drop unnecesary data
        temp = temp.drop(columns=["RecencyValue","FrequencyValue","MonetaryValue"])

        return temp
