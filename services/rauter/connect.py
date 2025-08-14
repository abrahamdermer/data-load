import mysql.connector


class Connect:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._init_connection()
        return cls._instance


    def _init_connection(self):
            self.mydb = mysql.connector.connect(
                host="", # לראות מאיפה הוא יקבל את זה
                user="myuser", 
                password="mypassword",
                database="mydb",
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