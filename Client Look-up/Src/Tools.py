#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import pandas as pd
import yaml
import pyodbc
from datetime import datetime
import win32com.client as win32

CONFIGURATION = os.path.join("..","Src","Config.yml")

# Read database settings
with open(CONFIGURATION, "r") as reader:
    config = yaml.load(reader)

def connect_to_dwh():
    """Connect to marketing data warehouse
    """
    # Connect to db with credentials
    cnxn = pyodbc.connect("DRIVER={ODBC Driver 13 for SQL Server};SERVER=" + config["GMAL"]["SERVER"] + 
                           ";PORT=1443;DATABASE=" + config["GMAL"]["DATABASE"] + 
                           ";UID="+ config["GMAL"]["USERNAME"] + ";PWD=" + config["GMAL"]["PASSWORD"])
    cursor = cnxn.cursor()
    return cnxn

def read_query(keyword):
    """Read query according to request
    """
    query = os.path.join("..", config["DIR"]["SOURCE"], config["QUERY"][keyword])
    # Read query
    with open(query, "r") as reader:
       q = reader.read()#.replace('\n', '')

    return q

def commit_query(query, cnxn):
    """Commit the queries to the database
    """
    # Split queries
    query = query.split(";")
    # Commit
    df = pd.concat([pd.read_sql_query(q,cnxn) for q in query], axis=1)

    return df

