from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pymongo import MongoClient
from datetime import datetime
import uuid
import re
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def scrape_trending_topics():
    """
    Scrapes the trending topics from Twitter and saves them into MongoDB.

    Returns:
        dict: Contains scraped trends, timestamp, and proxy IP.
    """
    # Fetch environment variables
    MONGO_URI = os.getenv('MONGO_URI')
    TWITTER_USERNAME = os.getenv('TWITTER_USERNAME')
    TWITTER_PASSWORD = os.getenv('TWITTER_PASSWORD')

    if not MONGO_URI or not TWITTER_USERNAME or not TWITTER_PASSWORD:
        raise ValueError("Missing required environment variables. Ensure MONGO_URI, TWITTER_USERNAME, and TWITTER_PASSWORD are set.")

    # Set up WebDriver options
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    # Uncomment below for headless mode
    # chrome_options.add_argument("--headless")

    # Define the path to the ChromeDriver
    driver_path = "C:/Users/ishaa/Desktop/stir_assignment/chromedriver.exe"
    driver_service = Service(driver_path)
    driver = webdriver.Chrome(service=driver_service, options=chrome_options)

    try:
        print("Navigating to Twitter login page...")
        driver.get("https://x.com/i/flow/login")

        # Log in to Twitter
        print("Entering username...")
        username_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "text"))
        )
        username_field.send_keys(TWITTER_USERNAME)
        username_field.send_keys(Keys.RETURN)

        print("Entering password...")
        password_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password_field.send_keys(TWITTER_PASSWORD)
        password_field.send_keys(Keys.RETURN)

        # Wait for the trending section
        print("Waiting for the 'Trending now' section...")
        try:
            trending_container = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Timeline: Trending now"]'))
            )
        except TimeoutException:
            print("Error: 'Trending now' section not found. Please check the XPath or page structure.")
            return None

        # Extract and process trends
        print("Extracting trends...")
        raw_content = trending_container.text
        print("Raw content:", raw_content)

        # Filter and clean trends
        lines = raw_content.split("\n")
        trends = [
            line.strip() for line in lines
            if not re.search(r"(what's happening|trending|\d+k posts|posts)", line, re.IGNORECASE)
        ]
        trends = list(dict.fromkeys(trends))[:5]  # Remove duplicates and limit to top 5

        if not trends:
            print("No valid trends found. Check the raw content or parsing logic.")
            return {"trends": [], "timestamp": None, "proxy_ip": "127.0.0.1"}

        print("Top 5 Trends:", trends)

        # Prepare data for MongoDB
        unique_id = str(uuid.uuid4())
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        document = {
            "_id": unique_id,
            "nameoftrend1": trends[0] if len(trends) > 0 else None,
            "nameoftrend2": trends[1] if len(trends) > 1 else None,
            "nameoftrend3": trends[2] if len(trends) > 2 else None,
            "nameoftrend4": trends[3] if len(trends) > 3 else None,
            "nameoftrend5": trends[4] if len(trends) > 4 else None,
            "timestamp": timestamp,
            "proxy_ip": "127.0.0.1"
        }

        # Save trends to MongoDB
        print("Connecting to MongoDB...")
        try:
            client = MongoClient(MONGO_URI)
            db = client.twitter_trends
            collection = db.trending

            print("Saving data to MongoDB...")
            collection.insert_one(document)
            print("Data saved successfully:", document)

            return {
                "trends": trends,
                "timestamp": timestamp,
                "proxy_ip": "127.0.0.1"
            }
        except Exception as e:
            print("Failed to connect or save to MongoDB:", e)
            return None

    except Exception as e:
        print("An error occurred:", e)
        return None

    finally:
        print("Closing the browser...")
        driver.quit()

# Run the scraper if this script is executed directly
if __name__ == "__main__":
    result = scrape_trending_topics()
    if result:
        print("Scraping completed successfully:", result)
    else:
        print("No data scraped.")
