# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 19:32:27 2023

@author: Alumno
"""

import pymysql #1. pip3 install --upgrade pip 2. pip3 install pymysql

import pandas as pd
import numpy as np
import collections
import itertools
from datetime import date, datetime, timedelta
import random


################ MySQL ###################
database = 'mibd'
username = 'root'
password = '1234'
db = pymysql.connect(host="127.0.0.1", user=username, passwd=password, database=database)
cursor = db.cursor()# prepare a cursor object

lista=["👶","👧","🧒","👦","👩","🧑","👨","👩‍","🦱","👨‍","🦱","👩‍","🦰","👨‍","🦰","👱‍","👱","👱‍","👨‍","👩‍","🦲","👨‍","🦲","🧔","👵","🧓","👴","👲","👳‍","👳","👸","🤴"]

def consulta():
    consulta = " SELECT nombre, salario from empleado "
    print("consulta:", consulta)
    cursor.execute(consulta)
    df = pd.read_sql_query(consulta, db)
    #print("type(df)=", (df))
    #print("df.info()=",df.info())
    #print("df.describe()=",df.describe())
    #print("df.head(10)=",df.head(10))
    #print("df.tail(10)=",df.tail(10))
    #print("df.sample(20)=",df.sample(20))
    
    df.nombre = df.nombre.map(lambda x: x+" "+random.choice(lista))
    print("df.head(21)=",df.head(21))
    
consulta()



