import json

# Maybe use AI for this


def filter_urls(urls, include_keywords, exclude_keywords, require_pdf=False):
    """
    Filters a list of URLs based on exclusion and inclusion keywords.
    
    Args:
        urls (list): The list of URLs.
        include_keywords (list): The list of keywords to include in the URL.
        exclude_keywords (list): The list of keywords that if found, will skip the URL.
        require_pdf (bool): If True, only URLs ending with '.pdf' will be considered.
    
    Returns:
        list: Filtered list of URLs.
    """
    filtered_urls = []
    
    for url in urls:
        if any(ex_kw.lower() in url.lower() for ex_kw in exclude_keywords):
            continue

        if require_pdf and not url.lower().endswith(".pdf"):
            continue

        if any(inc_kw.lower() in url.lower() for inc_kw in include_keywords):
            filtered_urls.append(url)
            
    return filtered_urls

def FilterUrlsForReports(filename="urls.txt", log=False, SaveToFilename=""):
    with open("urls.txt", "r") as f:
        urls = f.read().splitlines()

    exclude_keywords = ["Governance", "remuneration", "20-f", "update"]
    annual_keywords = ["annual-report", "annual_report"]
    quarterly_keywords = ["q1", "q2", "q3", "q4"]

    annual_urls = filter_urls(urls, annual_keywords, exclude_keywords, require_pdf=False)
    quarterly_urls = filter_urls(urls, quarterly_keywords, exclude_keywords, require_pdf=False)

    if log:
        print("Annual URLs:")
        for url in annual_urls:
            print(url)

        print("\nQuarterly URLs:")
        for url in quarterly_urls:
            print(url)

    if SaveToFilename:
        data = {
            "annual_urls": annual_urls,
            "quarterly_urls": quarterly_urls
        }
        with open(SaveToFilename, "w") as f_out:
            json.dump(data, f_out, indent=4)
        print(f"\nOutput successfully saved to {SaveToFilename}")

if __name__ == '__main__':
    FilterUrlsForReports(SaveToFilename="reportUrls.json")