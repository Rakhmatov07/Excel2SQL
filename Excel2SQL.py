import pandas
import csv
import sqlite3

"""This project imports excel file to database"""
excel_file = input('Enter an excel file (ex:file.xls/xlsx):')
database = input('Create new database(ex:example.db):')


def import_excel2sqlite(excel_file, database):
    print("Hello")
    df = pandas.read_excel(excel_file, header=0)
    connection = sqlite3.connect(database)
    df.to_sql(
        name='full_info',
        con=connection,
        if_exists='replace',
        index=False,
        dtype={
            'First Name': 'txt',
            'Last Name': 'txt',
            'Gender': 'txt',
            'Country': 'txt',
            'Age': 'real',
            'Date': 'real',
            'Id': 'real'
        }
    )
    return df


print(import_excel2sqlite(excel_file=excel_file, database=database))
