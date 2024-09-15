from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = os.getenv("DB_STRING")
    
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)
    # for db in client.list_databases():
    #     print(db)
    
    # Create the database for our exam  ple (we will use the same database throughout the tutorial
    return client['htn2024']

