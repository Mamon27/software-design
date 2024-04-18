import sqlite3

def create_info_table():
    try:
        conn = sqlite3.connect("infodatabase.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS infodatabase (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                lastname TEXT,
                firstname TEXT,
                patronymic TEXT,
                age INTEGER,
                gender TEXT,
                notes TEXT
            )
        """)

        conn.commit()

    except Exception as e:
        print(f"Error creating infodatabase table: {str(e)}")

    finally:
        if conn:
            conn.close()
