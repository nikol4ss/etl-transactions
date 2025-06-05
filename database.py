from sqlalchemy import create_engine
from urllib.parse import quote_plus
import pandas as pd

params = quote_plus(
    "Driver={ODBC Driver 18 for SQL Server};"
    "Server=localhost;"
    "Database=Onebeat;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

df = pd.read_csv('data/validated_transactions.csv')

DATABASE_URL = f"mssql+pyodbc:///?odbc_connect={params}"
engine = create_engine(DATABASE_URL)

df.to_sql('Transactions', con=engine, if_exists='append', index=False)
