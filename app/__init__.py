"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrq9lpmbg5e4khreg50-a",
        database="todolist_swii",
        user="rohan_nagula",
        password="Q5Fl07mno2BkGoCW58OgwKyfKxEHGnSH")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
