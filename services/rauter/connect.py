import mysql.connector


class Connect:
    _instance = None

# REQUIRED_VARS=("DB_HOST" "DB_USER" "DB_PASS" "DB_NAME")

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._init_connection()
        return cls._instance


    def _init_connection(self):
            self.mydb = mysql.connector.connect(
                host="DB_HOST", # לראות מאיפה הוא יקבל את זה
                user="DB_USER",  # לראות מאיפה הוא יקבל את זה
                password="DB_PASS",  # לראות מאיפה הוא יקבל את זה
                database="DB_NAME",  # לראות מאיפה הוא יקבל את זה
                auth_plugin=''  # לראות מאיפה הוא יקבל את זה
            )
            self.cursor = self.mydb.cursor()

    def execute(self, query):
        # if not self._instance:
        #     self._instance._init_connection()
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        if self.cursor:
            self.cursor.close()
            self.cursor = None
        if self.mydb:
            self.mydb.close()
            self.mydb = None