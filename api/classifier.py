import cohere
from cohere import ClassifyExample
import os 
from dotenv import load_dotenv

load_dotenv()

co = cohere.Client(os.getenv("API_KEY"))
class CustomExample:
    def __init__(self, text, label):
        self.text = text
        self.label = label

def classify(inputs):
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

    response = co.classify(
        inputs=inputs,
        examples=examples,
    )
    return response
print(classify(["Fix the production server issue immediately"]))
