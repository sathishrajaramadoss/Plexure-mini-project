#!/usr/bin/python
# -*- coding: utf-8 -*-

# Import packages
from flask import Flask
from flask import request
from flask import render_template, redirect, url_for
from werkzeug.utils import secure_filename
import Tools
from flask_bootstrap import Bootstrap
import pandas as pd
import os
import datetime as datetime

HTML_DIR = os.path.join("..","HTML")
STATIC_DIR = os.path.join("..","HTML", "static")

app = Flask(__name__, template_folder=HTML_DIR, static_folder=STATIC_DIR)
bootstrap = Bootstrap(app)

# Define initial page
@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")
    

@app.route("/Result", methods=["POST"])

def gmal():
    db = Tools.connect_to_dwh()
    
    if request.method == 'POST':
       
        startdate = request.form['startdate']
        startdate=startdate.replace("-","")
        #print(startdate)
        #print(type(startdate))
        #zs = startdate.split('-')
        enddate = request.form['enddate']
        enddate=enddate.replace("-","")
        #ze = enddate.split('-')
        #Total_Users_q = Tools.read_query("TOTALUSERS")
        #x = Total_Users_q.replace("@STARTDATE", startdate)
        #y = x.replace("@ENDDATE",enddate)
        #print (y)
        
#read query
       
        Total_Users_q=Tools.read_query("TOTALUSERS").replace("@STARTDATE", startdate).replace("@ENDDATE", enddate)
        Total_Email_Reg_q=Tools.read_query("TOTALEMAILREG").replace("@STARTDATE", startdate).replace("@ENDDATE", enddate)
        Unregistered_Email_Users_q=Tools.read_query("UNREGUSERS").replace("@STARTDATE", startdate).replace("@ENDDATE", enddate)
        Reg_Email_Inactive_Users_q=Tools.read_query("REGINACTIVE").replace("@STARTDATE", startdate).replace("@ENDDATE", enddate)
        Reg_Email_Active_Users_q=Tools.read_query("REGACTIVE").replace("@STARTDATE", startdate).replace("@ENDDATE", enddate)
        Redmeers_Active_Users_Email_q=Tools.read_query("REDMACTIVE").replace("@STARTDATE", startdate).replace("@ENDDATE", enddate)
        Non_Redmeers_Active_Users_Email_q=Tools.read_query("NONREDMACTIVE").replace("@STARTDATE", startdate).replace("@ENDDATE", enddate)
        KPIs_q=Tools.read_query("KPIS").replace("@STARTDATE", startdate).replace("@ENDDATE", enddate)
        Migrated_Users_q=Tools.read_query("MIGRATED")
        Device_Reg_Total_q=Tools.read_query("DRTOTAL").replace("@STARTDATE", startdate).replace("@ENDDATE", enddate)
        Device_Reg_Active_q=Tools.read_query("DRACTIVE").replace("@STARTDATE", startdate).replace("@ENDDATE", enddate)
        Device_Reg_Inactive_q=Tools.read_query("DRINACTIVE").replace("@STARTDATE", startdate).replace("@ENDDATE", enddate)
        Device_Active_Redeemers_q=Tools.read_query("DAREDEEM").replace("@STARTDATE", startdate).replace("@ENDDATE", enddate)
        Device_Active_NonRedeemers_q=Tools.read_query("DANONREDEEM").replace("@STARTDATE", startdate).replace("@ENDDATE", enddate)

    
#commit query
    Total_Users_res = Tools.commit_query(Total_Users_q, db)
    Total_Email_Reg_res = Tools.commit_query(Total_Email_Reg_q, db)
    Unregistered_Email_Users_res = Tools.commit_query(Unregistered_Email_Users_q, db)
    Reg_Email_Inactive_Users_res = Tools.commit_query(Reg_Email_Inactive_Users_q, db)
    Reg_Email_Active_Users_res = Tools.commit_query(Reg_Email_Active_Users_q, db)
    Redmeers_Active_Users_Email_res = Tools.commit_query(Redmeers_Active_Users_Email_q, db)
    Non_Redmeers_Active_Users_Email_res = Tools.commit_query(Non_Redmeers_Active_Users_Email_q, db)
    KPIs_res = Tools.commit_query(KPIs_q, db)
    Migrated_Users_res = Tools.commit_query(Migrated_Users_q, db)
    Device_Reg_Total_res = Tools.commit_query(Device_Reg_Total_q, db)
    Device_Reg_Active_res = Tools.commit_query(Device_Reg_Active_q, db)
    Device_Reg_Inactive_res = Tools.commit_query(Device_Reg_Inactive_q, db)
    Device_Active_Redeemers_res = Tools.commit_query(Device_Active_Redeemers_q, db)
    Device_Active_NonRedeemers_res = Tools.commit_query(Device_Active_NonRedeemers_q, db)
    
    
  
    return render_template("success.html",Total_Users_res =list(Total_Users_res['Total_Users'])[0],
                           Total_Email_Reg_res =list(Total_Email_Reg_res['Total_Email_Users'])[0],
                           Unregistered_Email_Users_res=list(Unregistered_Email_Users_res['Unregistered_Users'])[0],
                           Reg_Email_Inactive_Users_res =list(Reg_Email_Inactive_Users_res['Reg_Email_Inactive_Users'])[0],
                           Reg_Email_Active_Users_res =list(Reg_Email_Active_Users_res['Reg_Email_Active_Users'])[0],
                          Redmeers_Active_Users_Email_res =list(Redmeers_Active_Users_Email_res['Redmeers_Active_Users_Email'])[0],
                          Non_Redmeers_Active_Users_Email_res =list(Non_Redmeers_Active_Users_Email_res['Non_Redmeers_Active_Users_Email'])[0],
                          KPIs_res1 =list(KPIs_res['App_start_up'])[0],
                          KPIs_res2 =list(KPIs_res['Adv_Impressions'])[0],
                          KPIs_res3 =list(KPIs_res['Adv_Clicks'])[0],
                          KPIs_res4 =list(KPIs_res['Offer_Impressions'])[0],
                          KPIs_res5 =list(KPIs_res['Offer_Clicks'])[0],
                          KPIs_res6 =list(KPIs_res['Offer_Redemptions'])[0],
                          KPIs_res7 =list(KPIs_res['Offer_Instore_Redemptions'])[0],
                          KPIs_res8 =list(KPIs_res['Push_Msg_Sent'])[0],
                          KPIs_res9 =list(KPIs_res['Push_Msg_Seen'])[0],
                          KPIs_res10 =list(KPIs_res['Push_Msg_Clicked'])[0],
                          KPIs_res11 =list(KPIs_res['Loyalty_Card_Impressions'])[0],
                          KPIs_res12 =list(KPIs_res['Loyalty_Card_Instance_Activated'])[0],
                          KPIs_res13 =list(KPIs_res['Loyalty_Card_Points_Created'])[0],
                          KPIs_res14 =list(KPIs_res['Loyalty_Card_Rewards_Activated'])[0],
                          KPIs_res15 =list(KPIs_res['App_Page_Impressions'])[0],
                          KPIs_res16 =list(KPIs_res['Button_Clicks'])[0],
                          Migrated_Users_res1 =list(Migrated_Users_res['Total_Migrated_Users'])[0],
                          Migrated_Users_res2 =list(Migrated_Users_res['Non_Converted_Migrated_Users'])[0],
                          Migrated_Users_res3 =list(Migrated_Users_res['Migrated_Users_Logged_In'])[0],
                          Device_Reg_Total_res =list(Device_Reg_Total_res['Device_Reg_Total'])[0],
                          Device_Reg_Active_res =list(Device_Reg_Active_res['Device_Reg_Active'])[0],
                          Device_Reg_Inactive_res =list(Device_Reg_Inactive_res['Device_Reg_Inactive'])[0],
                          Device_Active_Redeemers_res =list(Device_Active_Redeemers_res['Device_Active_Redeemers'])[0],
                          Device_Active_NonRedeemers_res =list(Device_Active_NonRedeemers_res['Device_Active_NonRedeemers'])[0])

# Ran the web application
if __name__ == "__main__":
    app.run(debug=True)