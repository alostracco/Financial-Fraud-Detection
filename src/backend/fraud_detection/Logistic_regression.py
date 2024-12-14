from sqlalchemy import text
from src.backend.utils.database_connection import get_db_connection

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def run_madlib_logistic_regression():
    # Update connection details (.env) with your actual database credentials and host
    # Create a database engine
    engine = get_db_connection()

    with engine.connect() as connection:

        # Drop previous results if they exist
        connection.execute(text("DROP TABLE IF EXISTS LR_results;"))

        # Create train and test split (tables)
        connection.execute(text("DROP TABLE IF EXISTS transactions_LR_train;"))
        connection.execute(text("DROP TABLE IF EXISTS transactions_LR_test;"))

        # Generate random number column for train-test split
        connection.execute(text("CREATE TEMP TABLE transactions_with_rand AS SELECT *, random() AS rnd FROM transactions;"))
        # Populate train and test data
        connection.execute(text("CREATE TABLE transactions_train AS SELECT * FROM transactions_with_rand WHERE rnd < 0.7;"))
        connection.execute(text("CREATE TABLE transactions_test AS SELECT * FROM transactions_with_rand WHERE rnd >= 0.7;"))


        connection.execute(text("DROP TABLE IF EXISTS transactions_features_train;"))
        connection.execute(text("DROP TABLE IF EXISTS transactions_features_test;"))
        connection.execute(text("CREATE TABLE transactions_features_train AS SELECT (is_fraud = 1)::boolean AS is_fraud, ARRAY[transaction_time, amount, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22, v23, v24, v25, v26, v27, v28]::double precision[] AS features FROM transactions_train;"))
        connection.execute(text("CREATE TABLE transactions_features_test AS SELECT (is_fraud = 1)::boolean AS is_fraud, ARRAY[transaction_time, amount, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22, v23, v24, v25, v26, v27, v28]::double precision[] AS features FROM transactions_test;"))


        # Run logistic regression training
        # This trains a model to predict is_fraud based on numeric features
        connection.execute(text("SELECT madlib.logregr_train('transactions_features_train', 'LR_results', 'is_fraud', 'features');"))

        # Fetch and print model results
        # The LR_results table contains model coefficients, p-values, etc.
        result = connection.execute(text("SELECT * FROM LR_results;"))
        rows = result.fetchall()
        print("Logistic Regression Model Coefficients and p-values:")
        for row in rows:
            print(row)

        connection.execute(text("DROP TABLE IF EXISTS predictions;"))
        connection.execute(text("CREATE TABLE predictions AS SELECT t.is_fraud, madlib.logregr_predict(r.coef, t.features) AS prediction FROM transactions_features_test t, LR_results r;"))
        connection.execute(text("""DROP TABLE IF EXISTS predictions_summary;"""))
        # Uncomment this to see the (actual, prediction) for each datapoint
        #predictions = connection.execute(text("SELECT * FROM predictions;")).fetchall()
        #print(predictions)
        connection.execute(text("SELECT madlib.confusion_matrix('predictions', 'predictions_summary', 'prediction', 'is_fraud');"))
        result = connection.execute(text("SELECT * FROM predictions_summary;"))
        predictions_summary = result.fetchall()
        print("\nConfusion Matrix after predicting each transaction in the test set:")
        print(predictions_summary)

#----------------------------------------------------------
        # Plot Generation

        matrix_data = np.array([
            [float(predictions_summary[0][2][0]), float(predictions_summary[0][2][1])],
            [float(predictions_summary[1][2][0]), float(predictions_summary[1][2][1])]
        ])
        plt.figure(figsize=(6, 5))
        sns.heatmap(matrix_data, annot=True, fmt='.2f', cmap='Blues', xticklabels=['False', 'True'],
                   yticklabels=['False', 'True'], cbar=False)
        # Set labels and title
        plt.xlabel('Predicted')
        plt.ylabel('Actual')
        plt.title('Confusion Matrix')

        plt.show()


if __name__ == "__main__":
    run_madlib_logistic_regression()
