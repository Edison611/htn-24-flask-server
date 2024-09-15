# Flask Server
import cohere
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import os
from datetime import datetime
from pymongo import MongoClient
# from cohere import ClassifyExample

class CustomExample:
    def __init__(self, text, label):
        self.text = text
        self.label = label

load_dotenv()

api_key = os.getenv("API_KEY")
co = cohere.Client(api_key=api_key)

app = Flask(__name__)
CORS(app, support_credentials=True)
@cross_origin(supports_credentials=True)


@app.route('/', methods=['GET'])
def test():
    return "Hello World"

@app.route('/excuse', methods=['POST'])
def excuses():
    data = request.get_json()
    task = data['task']
    excuse_type = data['type_of_res']

    response = co.chat(
        # model="command-r-plus",
        message=f"Provide a single custom sarcastic, realistic {excuse_type} excuse that the user can use to avoid doing their {task}. Make sure the excuse is less than 30 words in length. Use 'my productivity is solar-powered, and unfortunately, it's cloudy today' as an example of an absurd excuse. Use science for scientific excuses. don't always start sentences with 'sorry, I can't.",
    )
    CONNECTION_STRING = os.getenv("DB_STRING")
    
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)
    # for db in client.list_databases():
    #     print(db)
    
    # Create the database for our exam  ple (we will use the same database throughout the tutorial
    db = client['htn2024']

    inputs = [task]
    examples = [
    CustomExample("Fix the production server issue immediately", "Critical"),
    CustomExample("Prepare the end-of-year financial report for the board meeting next week", "High Priority"),
    CustomExample("Review team performance for the quarterly report", "Moderate"),
    CustomExample("Clean up the old project files from the archive", "Low Priority"),
    CustomExample("Organize the office stationery cabinet", "Trivial"),
    CustomExample("Respond to an urgent customer complaint", "Critical"),
    CustomExample("Schedule a meeting with the client for project feedback", "High Priority"),
    CustomExample("Update the project documentation for future reference", "Moderate"),
    CustomExample("Check and organize the backup logs for the last month", "Low Priority"),
    CustomExample("Test the new feature that was added last week", "Trivial"),
    CustomExample("Address the security vulnerability in the system immediately", "Critical"),
    CustomExample("Submit the quarterly sales report by the end of this week", "High Priority"),
    CustomExample("Review and update employee handbooks", "Moderate"),
    CustomExample("Organize the team bonding event", "Low Priority"),
    CustomExample("Water the office plants", "Trivial"),
    CustomExample("Resolve the data corruption issue affecting the live environment", "Critical"),
    CustomExample("Draft the proposal for the new client project", "High Priority"),
    CustomExample("Review the latest market research for future projects", "Moderate"),
    CustomExample("Update the employee database with recent changes", "Low Priority"),
    CustomExample("Refill the coffee machine in the break room", "Trivial"),
    CustomExample("Investigate and resolve the network outage in the main office", "Critical"),
    CustomExample("Prepare the presentation for the client meeting tomorrow", "High Priority"),
    CustomExample("Compile the research notes for the next brainstorming session", "Moderate"),
    CustomExample("Check the licenses for software that are expiring soon", "Low Priority"),
    CustomExample("Sort and file old invoices from previous projects", "Trivial"),
    CustomExample("I have an important meeting in 10 minutes", "Critical"),
    CustomExample("Relax", "Trivial"),
    CustomExample("Study", "Moderate")
]

    urgency = co.classify(
        inputs=inputs,
        examples=examples,
    ).classifications[0].prediction
    try:
        # urgency = classify([task]).classifications[0].prediction
        # Added env variables
        history_collection = db['history']
        now = datetime.now().strftime("%Y-%m-%d")
        history_collection.insert_one({"task": task, "urgency": urgency, "date": now, "response": response.text})
    except:
        return jsonify({"response" : response.text, "urgency": "Moderate"})
    return jsonify({"response" : response.text, "urgency": urgency})

@app.route('/history', methods=['GET'])
def history_function():
    CONNECTION_STRING = os.getenv("DB_STRING")
    
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)
    # for db in client.list_databases():
    #     print(db)
    
    # Create the database for our exam  ple (we will use the same database throughout the tutorial
    db =  client['htn2024']
    history_collection = db['history']
    history = list(history_collection.find())  # Returns a cursor object
    needed_history = []
    for h in history:
        h['_id'] = str(h['_id'])
        needed_history.append(h)
    needed_history = sorted(needed_history, key=lambda x: x['date'], reverse=True)
    all_history = {"history": needed_history}
    return jsonify(all_history)


# if __name__ == '__main__':
#     app.run(debug=True)
    