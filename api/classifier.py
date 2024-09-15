import cohere
from cohere import ClassifyExample
import os 
from dotenv import load_dotenv

load_dotenv()

co = cohere.Client(os.getenv("API_KEY"))

def classify(inputs):
    examples = [
    ClassifyExample(text="Fix the production server issue immediately", label="Critical"),
    ClassifyExample(text="Prepare the end-of-year financial report for the board meeting next week", label="High Priority"),
    ClassifyExample(text="Review team performance for the quarterly report", label="Moderate"),
    ClassifyExample(text="Clean up the old project files from the archive", label="Low Priority"),
    ClassifyExample(text="Organize the office stationery cabinet", label="Trivial"),
    ClassifyExample(text="Respond to an urgent customer complaint", label="Critical"),
    ClassifyExample(text="Schedule a meeting with the client for project feedback", label="High Priority"),
    ClassifyExample(text="Update the project documentation for future reference", label="Moderate"),
    ClassifyExample(text="Check and organize the backup logs for the last month", label="Low Priority"),
    ClassifyExample(text="Test the new feature that was added last week", label="Trivial"),
    ClassifyExample(text="Address the security vulnerability in the system immediately", label="Critical"),
    ClassifyExample(text="Submit the quarterly sales report by the end of this week", label="High Priority"),
    ClassifyExample(text="Review and update employee handbooks", label="Moderate"),
    ClassifyExample(text="Organize the team bonding event", label="Low Priority"),
    ClassifyExample(text="Water the office plants", label="Trivial"),
    ClassifyExample(text="Resolve the data corruption issue affecting the live environment", label="Critical"),
    ClassifyExample(text="Draft the proposal for the new client project", label="High Priority"),
    ClassifyExample(text="Review the latest market research for future projects", label="Moderate"),
    ClassifyExample(text="Update the employee database with recent changes", label="Low Priority"),
    ClassifyExample(text="Refill the coffee machine in the break room", label="Trivial"),
    ClassifyExample(text="Investigate and resolve the network outage in the main office", label="Critical"),
    ClassifyExample(text="Prepare the presentation for the client meeting tomorrow", label="High Priority"),
    ClassifyExample(text="Compile the research notes for the next brainstorming session", label="Moderate"),
    ClassifyExample(text="Check the licenses for software that are expiring soon", label="Low Priority"),
    ClassifyExample(text="Sort and file old invoices from previous projects", label="Trivial"),
    ClassifyExample(text="I have an important meeting in 10 minutes", label="Critical")
]

    response = co.classify(
        inputs=inputs,
        examples=examples,
    )
    return response
