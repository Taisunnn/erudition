from sqlalchemy import create_engine, false
import pymysql
import pandas as pd

sqlEngine = create_engine("mysql+pymysql://tyson:tyson@localhost/first_db")
dbConnection = sqlEngine.connect()

query = pd.read_sql("SELECT COUNT(house_id) FROM housing_development", dbConnection)

print(query)
