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

#####DATABASE RELATED FUNCTIONS#####
def connect_to_dwh():
    """Connect to marketing data warehouse
    """
    # Connect to db with credentials
    cnxn = pyodbc.connect("DRIVER={ODBC Driver 13 for SQL Server};SERVER=" + config["DB"]["SERVER"] + 
                           ";PORT=1443;DATABASE=" + config["DB"]["DATABASE"] + 
                           ";UID="+ config["DB"]["USERNAME"] + ";PWD=" + config["DB"]["PASSWORD"])
    cursor = cnxn.cursor()
    return cnxn

def read_query(keyword):
    """Read query according to request
    """
    query = os.path.join("..", config["DIR"]["SOURCE"], config["QUERY"][keyword])
    # Read query
    with open(query, 'r') as reader:
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
#####CHECK FUNCTION#####
def check_column(data):
    """
        Check the column ID and column number
        Input: data - Pandas dataframe
    """
    
    try:
        assert len(data.columns) == 12
    except:
        print("Error: Missing columns")

    try:
        assert all(elem in config["Column_ID"] for elem in list(data.columns))
    except:
        print("Error: Column names")