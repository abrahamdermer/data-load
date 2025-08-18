from services.Router.connect import Connect


class DAL:
    def __init__(self):
        self.db = Connect()

    def get_tabel(self):
        return self.db.execute("SELECT * FROM aaaaaa;") # aaaaaaa = tabal name