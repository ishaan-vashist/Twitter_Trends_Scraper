Twitter Trends Scraper

Project Overview

The Twitter Trends Scraper project is designed to scrape the latest trending topics on Twitter (now X), save them in a MongoDB database, and display them on a web page. Users can trigger the script to fetch new trends, view the trends from the database, and run the query again for updated results.


Key Features

Web Scraping: Uses Selenium to log in to Twitter and scrape trending topics.

Data Storage: Stores the trends in a MongoDB collection for retrieval.

Web Interface: A Flask-based web app to display the trends, timestamp, proxy IP, and a JSON extract of the record.

Interactive: Users can run the scraping script directly from the web interface.


Technologies Used

Python: For the backend scraping and web app logic.

Selenium: For automated web scraping of Twitter trends.

MongoDB: To store scraped trends.

Flask: For serving the web interface.

HTML, CSS, JavaScript: For the frontend.


Setup Instructions

Prerequisites

Python 3.7+

MongoDB Atlas (or a local MongoDB instance)

Chrome browser and ChromeDriver

Required Python libraries:

selenium

flask

pymongo

Installation

Clone this repository.


Install the required Python libraries:

pip install selenium flask pymongo

Download ChromeDriver and place it in the scripts directory or a known path.

Configure your MongoDB connection string in the Python scripts.

Update your Twitter username and password in the scrape_twitter.py script.


Project Structure:
.
├── scripts
│   └── scrape_twitter.py  # Selenium script to scrape trends
├── templates
│   └── index.html         # Web page template
├── app.py                 # Flask application
└── README.md              # Project documentation


Usage Instructions

Running the Application

Start the Flask application:

python app.py

Open a browser and navigate to:



http://127.0.0.1:5000


### Features
- **Click to Run Script**: Click on "Click here to run the script" to trigger the scraping script.
- **View Trends**: Displays the most recent trends stored in MongoDB, along with the timestamp and IP address used.
- **JSON Extract**: Shows the full JSON document of the latest trends from the database.
- **Run Query Again**: Allows you to refresh and fetch the latest trends.

---

## Code Walkthrough

### 1. `scrape_twitter.py`
- Automates Twitter login and navigates to the "Trending now" section.
- Scrapes trending topics while filtering out unwanted content (e.g., "What’s happening").
- Stores the top 5 trends in MongoDB.

### 2. `app.py`
- **`/` Endpoint**: Serves the main HTML page.
- **`/run-script` Endpoint**: Triggers the Selenium script to fetch new trends.
- **`/get-trends` Endpoint**: Fetches the latest record from MongoDB and returns it as JSON.

### 3. `index.html`
- Displays trends and metadata (timestamp, IP address).
- Allows interaction to re-run the query and view updated trends.

---

## Example Output
### Web Interface
1. **Initial Page**: "Click here to run the script" link.
2. **After Running**:
   - Displays trending topics with timestamp and IP address.
   - Shows JSON extract of the MongoDB record.
   - Provides a link to re-run the query.

### Console Output
```bash
Navigating to Twitter login page...
Waiting for username field...
Waiting for password field...
Waiting for the 'Trending now' section...
Extracting raw text content...
Parsed trends: ['#Trend1', '#Trend2', '#Trend3', '#Trend4', '#Trend5']
Saving data to MongoDB...
Data saved to MongoDB: {...}

Troubleshooting

Selenium Errors:

Ensure ChromeDriver matches your Chrome browser version.

Check the XPaths in scrape_twitter.py if Twitter changes its structure.

MongoDB Connection Issues:

Verify your MongoDB connection string and database credentials.

Ensure the MongoDB service is running.

Web App Not Running:

Check for Flask errors in the terminal.

Ensure all required libraries are installed.

Future Enhancements

Add user authentication for the web interface.

Implement error logging for Selenium scripts.

Use Docker to containerize the application.

Improve the UI with dynamic charts for trend analysis.



Author

Ishaan Vashist

License

This project is open-source and available under the MIT License.

