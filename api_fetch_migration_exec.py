import requests
from pymongo import MongoClient


client = MongoClient("localhost", 4344)
response = requests.get("https://api.binance.com/api/v3/ticker/bookTicker").json()
db = client.api_fetch
table = db.table
table.delete_many({})
table.insert_many(response)