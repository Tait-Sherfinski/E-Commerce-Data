import sqlite3
import pandas as pd

conn = sqlite3.connect("chinook.db")
cur = conn.cursor()