from flask import Flask, jsonify, render_template
from pymongo import MongoClient
from datetime import datetime
import subprocess
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Flask app initialization
app = Flask(__name__)

# MongoDB connection
def get_mongo_client():
    """
    Initializes and returns a MongoDB client using environment variables.
    """
    try:
        mongo_uri = os.getenv("MONGO_URI")
        if not mongo_uri:
            raise ValueError("MONGO_URI is not set in the environment variables.")
        return MongoClient(mongo_uri)
    except Exception as e:
        raise ConnectionError(f"Failed to connect to MongoDB: {str(e)}")

# Initialize MongoDB client and database
try:
    client = get_mongo_client()
    db = client.twitter_trends
    collection = db.trending
except Exception as e:
    print(f"Error initializing MongoDB client: {str(e)}")
    collection = None  # Ensure collection is None if connection fails

@app.route('/')
def home():
    """
    Render the homepage with the latest trends from MongoDB.
    """
    try:
        if collection is None:  # Correct the check here
            raise Exception("MongoDB collection is not initialized.")
        # Fetch the latest record from MongoDB
        latest_trend = collection.find_one(sort=[("_id", -1)])
        return render_template('index.html', data=latest_trend)
    except Exception as e:
        return render_template('index.html', error=f"Error fetching data: {str(e)}")

@app.route('/run-script', methods=['GET'])
def run_script():
    """
    Trigger the Selenium script to scrape Twitter trends.
    """
    try:
        # Path to the Selenium script
        script_path = os.path.join('scripts', 'scrape_twitter.py')
        if not os.path.exists(script_path):
            raise FileNotFoundError(f"Script not found: {script_path}")
        result = subprocess.run(
            ['python', script_path],
            check=True,
            capture_output=True,
            text=True
        )
        return jsonify({"message": "Script executed successfully!", "output": result.stdout})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Script execution failed: {e.stderr}"})
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"})

@app.route('/get-trends', methods=['GET'])
def get_trends():
    """
    Return the latest trends from MongoDB in JSON format.
    """
    try:
        if collection is None:  # Correct the check here
            raise Exception("MongoDB collection is not initialized.")
        latest_trend = collection.find_one(sort=[("_id", -1)])
        if latest_trend:
            return jsonify(latest_trend)
        else:
            return jsonify({"trends": [], "timestamp": None, "proxy_ip": None})
    except Exception as e:
        return jsonify({"error": f"An error occurred while fetching trends: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
