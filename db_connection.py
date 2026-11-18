import pyodbc


def get_connection():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=SUBBULAKSHMI;"          # Example: localhost or DESKTOP-ABC123\SQLEXPRESS
        "DATABASE=Studentflask;"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )
    return conn