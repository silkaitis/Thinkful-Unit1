# -*- coding: utf-8 -*-
"""
Created on Thu Jul 07 20:25:39 2016

@author: Danius
"""

import sqlite3 as lite
import pandas as pd

con=lite.connect('project3.db')
tables={'cities':'(name text, state text)','weather':'(city text, year integer, warm_month text, cold_month text, avg_high integer)'}
for tab in tables.keys():
    con.execute("drop table if exists %s" % tab)
    con.execute("create table %s %s" % (tab,tables[tab]))

citydata=(('New York City','NY'),('Boston','MA'),('Chicago','IL'),('Miami','FL'),('Dallas','TX'),('Seattle','WA'),('Portland','OR'),('San Francisco','CA'),('Los Angeles','CA'))
weatherdata=(('New York City', 2013, 'July','January',62),('Boston', 2013, 'July','January',59),('Chicago', 2013, 'July','January',59),('Miami', 2013,'August','January',84),('Dallas', 2013,'July','January',77),('Seattle', 2013,'July','January',61),('Portland', 2013,'July','December',63),('San Francisco', 2013,'September','December',64),('Los Angeles', 2013,'September','December',75))

cur=con.cursor()
cur.executemany("insert into cities values(?,?)",citydata)
cur.executemany("insert into weather values(?,?,?,?,?)",weatherdata)

cur.execute("select city,state,year,warm_month,cold_month,avg_high from cities left outer join weather on name=city")
rows = cur.fetchall()
df = pd.DataFrame(rows)

print('The cities that are warmest in July are:'+' '.join(df[0][i]+','+df[1][i] for i in range(0,len(df[3])) if df[3][i]=='July' ))

con.commit()
con.close()