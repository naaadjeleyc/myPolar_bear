import os
import sqlite3
import csv

filePath = './Data_Extract_From_World_Development_Indicators.xlsx'


connect = sqlite3.connect('../db_guo.sqlite3')
cursor = connect.cursor()


connect.execute(
    '''
    CREATE TABLE IF NOT EXISTS country (
        country_name CHAR(50),
        country_code CHAR(50) PRIMARY KEY,
    );
    CREATE TABLE IF NOT EXISTS series (
        series_name CHAR(50),
        series_code CHAR(50) PRIMARY KEY,
    )
    ''')

print("table countries created")