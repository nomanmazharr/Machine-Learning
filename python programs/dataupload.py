from sqlalchemy import  create_engine
import mysql.connector
import pandas as pd

con = mysql.connector.connect(user='root', host='localhost', password='')
print(con)

cursor = con.cursor()
cursor.execute('CREATE DATABASE IF NOT EXISTS olympics')
data = pd.read_csv('insurance_data.csv')
# print(data)
engine = create_engine('mysql+pymysql://root:@localhost/olympics')

data.to_sql('insurance', engine)

# Making a database and upload data
# import pandas as pd
# from sqlalchemy import  create_engine
# from flask import Flask
# import mysql.connector
# import sqlalchemy
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def home():
#     print('This is home')
#
#
# con = mysql.connector.connect(host='localhost', user='root', password='')
# # print(con)
#
# cursor = con.cursor()
# db = cursor.execute('CREATE DATABASE IF NOT EXISTS olympics')
# # print(db)
#
# data = pd.read_csv('olympics_cleaned_v4.csv')
# engine = create_engine('mysql+pymysql://root:@localhost/olympics')
# data.to_sql('games', con=engine)
# # print(engine)
# # print(data.head())
