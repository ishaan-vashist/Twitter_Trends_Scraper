# Twitter Trends Scraper

## Overview
Twitter Trends Scraper is a Python-based application designed to fetch and analyze trending topics on Twitter. It integrates backend scraping functionality with a simple frontend interface to display results.

## Features
- **Twitter Trends Scraping**: Fetch trending topics directly from Twitter.
- **Web Interface**: Simple HTML frontend to display trends.
- **Configurable**: Easily set API keys and other settings using an `.env` file.
- **Export Output**: Option to save results in a `.docx` format.

## Directory Structure
```
Twitter_Trends_Scraper-main/
├── app.py                        # Main script for running the application
├── scripts/
│   └── scrape_twitter.py         # Script for scraping Twitter trends
├── templates/
│   └── index.html                # HTML template for the web interface
├── .env.example.txt              # Example configuration file
├── OUTPUT.docx                   # Sample output file
├── Twitter Trends Scraper.md     # Documentation
```

## Prerequisites
- Python 3.8+
- Twitter API access (API keys and tokens required)
- Required Python Libraries:
  - Flask
  - Tweepy
  - python-docx

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/Twitter_Trends_Scraper.git
   cd Twitter_Trends_Scraper-main
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the environment variables:
   - Copy `.env.example.txt` to `.env`:
     ```bash
     cp .env.example.txt .env
     ```
   - Update the `.env` file with your Twitter API keys and tokens.

## Usage

### 1. Running the Application
Start the Flask application:
```bash
python app.py
```
Access the web interface at `http://localhost:5000`.

### 2. Scraping Twitter Trends
To fetch the latest trends, ensure your API keys are correctly configured and run:
```bash
python scripts/scrape_twitter.py
```

### 3. Exporting Results
Results can be exported as a Word document (`OUTPUT.docx`) for further use or analysis.

## Contributing
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit changes and push:
   ```bash
   git commit -m "Description of changes"
   git push origin feature-name
   ```
4. Submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For questions or support, please contact ishaanvashista@gmail.com.

