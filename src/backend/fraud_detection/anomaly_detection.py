import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from src.backend.utils.database_connection import get_db_connection

# Implemented kmeans clustering to detect anomalies
def anomaly_detection():
    engine = get_db_connection()
    with engine.connect() as connection:
        connection.execute("""
            DROP TABLE IF EXISTS transactions_clusters, transactions_anomalies;
            
            SELECT madlib.kmeanspp(
                'public.transactions',
                'transactions_clusters',
                2,
                ARRAY[transaction_time, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10,
                      v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21,
                      v22, v23, v24, v25, v26, v27, v28, amount],
                'madlib.rand()',
                20,
                0.001,
                True 
            )
            FROM public.transactions;
            
            CREATE TABLE transactions_anomalies AS
            SELECT *
            FROM transactions_clusters
            WHERE cluster_id = 1; 
        """)
        print("Anomaly detection completed and stored in 'transactions_anomalies' table.")

if __name__ == "__main__":
    anomaly_detection()
