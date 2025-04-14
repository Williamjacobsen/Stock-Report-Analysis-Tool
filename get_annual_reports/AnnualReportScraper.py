import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from colorama import init, Fore, Style

init(autoreset=True)

base_url = "https://www.annualreports.com"
start_url = f"{base_url}/Company/novo-nordisk"

download_dir = "reports"
os.makedirs(download_dir, exist_ok=True)

def download_pdf(pdf_url):
    """Download the PDF from pdf_url and save it to the download directory."""
    local_filename = os.path.join(download_dir, pdf_url.split("/")[-1])
    try:
        with requests.get(pdf_url, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
        print(f"{Fore.GREEN}Downloaded: {local_filename}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Failed to download {pdf_url}: {e}{Style.RESET_ALL}")

def find_report_links(soup):
    """Return a list of absolute URLs for any PDF report links on the page."""
    report_links = []

    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "pdf" in href.lower():
            pdf_url = urljoin(base_url, href)
            report_links.append(pdf_url)
    return report_links

def scrape_reports(url):
    """Scrape a given page URL for report PDF links, download them, and follow pagination if available."""
    print(f"{Fore.CYAN}Scraping page: {url}{Style.RESET_ALL}")
    response = requests.get(url)
    if response.status_code != 200:
        print(f"{Fore.RED}Failed to retrieve page: {url}{Style.RESET_ALL}")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    for pdf_link in find_report_links(soup):
        download_pdf(pdf_link)

if __name__ == "__main__":
    scrape_reports(start_url)
