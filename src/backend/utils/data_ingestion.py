import pandas as pd
from sqlalchemy import create_engine
from database_connection import get_db_connection

def ingest_data(file_path):
    df = pd.read_csv(file_path)

    df.rename(columns={
        'Time': 'transaction_time',
        'V1': 'v1', 'V2': 'v2', 'V3': 'v3', 'V4': 'v4', 'V5': 'v5',
        'V6': 'v6', 'V7': 'v7', 'V8': 'v8', 'V9': 'v9', 'V10': 'v10',
        'V11': 'v11', 'V12': 'v12', 'V13': 'v13', 'V14': 'v14',
        'V15': 'v15', 'V16': 'v16', 'V17': 'v17', 'V18': 'v18',
        'V19': 'v19', 'V20': 'v20', 'V21': 'v21', 'V22': 'v22',
        'V23': 'v23', 'V24': 'v24', 'V25': 'v25', 'V26': 'v26',
        'V27': 'v27', 'V28': 'v28', 'Amount': 'amount', 'Class': 'is_fraud'
    }, inplace=True)

    engine = get_db_connection()
    df.to_sql('transactions', engine, if_exists='replace', index=False)

if __name__ == "__main__":
    ingest_data('creditcard.csv')