from sqlalchemy import text
from database_connection import get_db_connection

def test_madlib_connection():
    engine = get_db_connection()
    with engine.connect() as connection:
        result = connection.execute(text("SELECT madlib.version()"))
        print("MADlib Version:", result.scalar())

if __name__ == "__main__":
    test_madlib_connection()
