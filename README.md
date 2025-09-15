🕵️ Indeed Job Scraper

A simple Python project that automates job searching on Indeed.com using Selenium and exports the results into an Excel file for easy analysis.

📌 Project Overview

Manually searching for jobs can be repetitive and time-consuming. This project solves that by automatically scraping job postings from Indeed based on a given role (e.g., Machine Learning Engineer) and location.

The scraped data includes:

✅ Job Title

✅ Company Name

✅ Location

✅ Job Summary/Description

✅ Direct Job URL

Results are saved in an Excel (.xlsx) file for quick filtering, sorting, or further analysis.

⚙️ Features

🔍 Search jobs by keyword and location

📑 Scrape multiple pages of job listings

💾 Save results in Excel format

🖥️ Print scraped results directly in the terminal

🔧 Easily customizable for different roles or regions

🛠️ Tech Stack

Python 3.8+

Selenium – browser automation

Pandas – data handling

OpenPyXL – Excel support

📂 Installation & Setup

Clone the repository:

git clone https://github.com/your-username/indeed-job-scraper.git
cd indeed-job-scraper


Install dependencies:

pip install -r requirements.txt


Make sure you have Chrome installed and download the correct ChromeDriver matching your browser version.

Place the driver in your project folder or add it to your system PATH.

▶️ Usage

Run the script from terminal:

python indeed_selenium_scrape.py


Example inside the script:

if __name__ == "__main__":
    data = scrape_search("machine learning", location="", pages=2)

    df = pd.DataFrame(data)
    print(df)

    df.to_excel("indeed_machine_learning_jobs.xlsx", index=False)
    print("✅ Saved results to indeed_machine_learning_jobs.xlsx")

    driver.quit()

🚀 Future Enhancements

📈 Data visualization of job stats (roles, companies, locations)

🤖 NLP to analyze job descriptions

🌐 Web interface for non-technical users

🗄️ Database integration for long-term storage

🤝 Contributing

Contributions are welcome! Feel free to fork this repo, submit issues, or create pull requests.

📜 License

This project is licensed under the MIT License – free to use and modify.

👉 Pro Tip: Add a requirements.txt file with this content so others can install easily:

selenium
pandas
openpyxl
