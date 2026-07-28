import json

from api_client import APIClient
from database import Database
from logger import Logger


with open("config.json", "r") as file:
    config = json.load(file)

logger = Logger()

database = Database(config["database"])
database.create_table()

client = APIClient(
    config["api_url"],
    config["timeout"]
)

users = client.fetch_data()

for user in users:
    database.insert_user(user)

logger.log.info("Users saved successfully.")

database.show_users()

database.close()
