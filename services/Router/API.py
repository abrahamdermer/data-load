from typing import Union
from services.Router.DAL import DAL
from fastapi import FastAPI

# ייבא את  DAL

app = FastAPI()
dal = DAL()


@app.get("/")
def read_root():
    # זה יפנה לDAL ויביא את הטבלאה
    return DAL.get_tabel()
