# save as indeed_selenium_scrape.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import csv
import time

opts = Options()
opts.add_argument("--headless=new")
opts.add_argument("--no-sandbox")
opts.add_argument("--disable-dev-shm-usage")
opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
opts.add_experimental_option('excludeSwitches', ['enable-logging'])
opts.add_experimental_option('excludeSwitches', ['enable-logging'])
opts.add_argument("--log-level=3")



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)


def scrape_search(query, location="", pages=1):
    rows = []
    base = "https://www.indeed.com"
    for p in range(pages):
        start = p * 10
        url = f"{base}/jobs?q={query}&l={location}&start={start}"
        driver.get(url)
        time.sleep(2)  # wait for JS - adjust or use explicit waits

        cards = driver.find_elements(By.CSS_SELECTOR, "div.job_seen_beacon, div.result")
        for c in cards:
            try:
                title = c.find_element(By.CSS_SELECTOR, "h2.jobTitle").text
            except:
                title = ""
            try:
                company = c.find_element(By.CSS_SELECTOR, "span.companyName").text
            except:
                company = ""
            try:
                loc = c.find_element(By.CSS_SELECTOR, "div.companyLocation").text
            except:
                loc = ""
            try:
                summary = c.find_element(By.CSS_SELECTOR, "div.job-snippet").text
            except:
                summary = ""
            try:
                link_el = c.find_element(By.CSS_SELECTOR, "a")
                href = link_el.get_attribute("href")
            except:
                href = ""
            rows.append({"title": title, "company": company, "location": loc, "summary": summary, "url": href})
        time.sleep(1.5)
    return rows

def save_csv(rows, filename="indeed_selenium.csv"):
    keys = rows[0].keys() if rows else []
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(rows)

import pandas as pd

if __name__ == "__main__":
    # scrape jobs for "machine learning" with no location filter
    data = scrape_search("machine learning", location="", pages=2)

    # convert list of dicts to DataFrame
    df = pd.DataFrame(data)

    # print all rows in terminal
    pd.set_option("display.max_rows", None)
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", None)
    print(df)

    # save to Excel
    df.to_excel("indeed_machine_learning_jobs.xlsx", index=False)
    print("\n✅ Saved results to indeed_machine_learning_jobs.xlsx")

    driver.quit()

