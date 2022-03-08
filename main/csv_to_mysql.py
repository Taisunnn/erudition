from sqlalchemy import create_engine, false
import pymysql
import pandas as pd

table_name = "housing_development"

csv_listings = pd.read_csv(
    f"/Users/tyson/new_projects/assignment/sample_data/zillow_cleaned.csv"
)

sqlEngine = create_engine("mysql+pymysql://tyson:tyson@localhost/first_db")
dbConnection = sqlEngine.connect()

csv_listings.to_sql(table_name, dbConnection, if_exists="append", index=false)

dbConnection.close()
