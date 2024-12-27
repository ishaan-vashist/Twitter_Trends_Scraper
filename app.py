from flask import Flask, jsonify, render_template
from pymongo import MongoClient
from datetime import datetime
import subprocess
import os  # For file path handling

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb+srv://ivashist:mrllwT72sMg8tJFd@cluster0.npu82.mongodb.net/')
db = client.twitter_trends
collection = db.trending

@app.route('/')
def home():
    """
    Render the homepage with the latest trends from MongoDB.
    """
    try:
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
        script_path = os.path.join('scripts', 'scrape_twitter.py')  # Adjust the path if needed
        result = subprocess.run(['python', script_path], check=True, capture_output=True, text=True)
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
        latest_trend = collection.find_one(sort=[("_id", -1)])
        if latest_trend:
            return jsonify(latest_trend)
        else:
            return jsonify({"trends": [], "timestamp": None, "proxy_ip": None})
    except Exception as e:
        return jsonify({"error": f"An error occurred while fetching trends: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
