import pandas as pd
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time
import random

def scrape_chunk(start_page, end_page):
    chunk_data = []
    print(f"--- Starting Chunk: Pages {start_page} to {end_page} ---")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
        page = context.new_page()
        page.route("**/*.{png,jpg,jpeg,gif,webp}", lambda route: route.abort())

        for i in range(start_page, end_page + 1):
            url = f"https://nigeriapropertycentre.com/property-for-rent-sale/lagos?page={i}"
            try:
                # Reduced timeout slightly but added more robust waiting
                page.goto(url, timeout=60000, wait_until="domcontentloaded")
                page.wait_for_timeout(2000)
                
                soup = BeautifulSoup(page.content(), 'html.parser')
                listings = soup.find_all("div", class_="wp-block-body")
                
                if not listings: break

                for item in listings:
                    title = item.find("h4", class_="content-title").get_text(strip=True) if item.find("h4") else "N/A"
                    price = item.find("span", class_="pull-sm-left").get_text(strip=True) if item.find("span") else "N/A"
                    address = item.find("address").get_text(strip=True) if item.find("address") else "N/A"
                    details = item.find("ul", class_="aux-info").get_text(" | ", strip=True) if item.find("ul") else "N/A"
                    
                    chunk_data.append({"Title": title, "Price": price, "Address": address, "Details": details})
                
                print(f"Page {i} processed. Subtotal: {len(chunk_data)}")
                time.sleep(random.uniform(1, 2))
                
            except Exception as e:
                print(f"Skipped page {i} (Network/Timeout)")
                continue
        browser.close()
    return chunk_data

def run_mega_scraper():
    final_data = []
    for start in [1, 51, 101]:
        data = scrape_chunk(start, start + 49)
        final_data.extend(data)
        time.sleep(5)

    if final_data:
        df = pd.DataFrame(final_data)
        save_path = r"C:\Users\Najib\Documents\lagos_raw_data.csv"
        # Added encoding='utf-8-sig' to handle symbols correctly in Excel/Windows
        df.to_csv(save_path, index=False, encoding='utf-8-sig')
        print(f"DONE: Saved {len(df)} properties to {save_path}")
    else:
        print("No data was collected.")

if __name__ == "__main__":
    run_mega_scraper()
