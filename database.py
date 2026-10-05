import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="yash8890",
        database="sales_db"
    )


def run_query(query, params=None):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(query, params or ())
    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result

# if __name__ == "__main__":
#     result = run_query("SELECT * FROM sales LIMIT 5")
#     print(result)