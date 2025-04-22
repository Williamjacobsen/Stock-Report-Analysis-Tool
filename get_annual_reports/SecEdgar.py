# https://www.sec.gov/edgar/browse/?CIK=320193&owner=exclude


if __name__ == '__main__':
    from Scraper import Scraper
    import time

    scraper = Scraper()

    scraper.OpenPage('https://www.sec.gov/edgar/browse/?CIK=320193&owner=exclude')

    # View filings
    scraper.Click('/html/body/main/div[4]/div[1]/div/div/button[1]')

    # Clear date field
    scraper.SendKeys('/html/body/main/div[5]/div/div[1]/div[1]/div/input[3]', scraper.keys.CONTROL, 'a', scraper.keys.BACKSPACE, '\n')
    
    # Sort by form type
    scraper.Click('/html/body/main/div[5]/div/div[3]/div[3]/div[1]/div/table/thead/tr/th[1]')
    
    time.sleep(5)

    rows_count = scraper.CountChildren('/html/body/main/div[5]/div/div[3]/div[3]/div[2]/table/tbody')

    filing_links = []

    for i in range(1, rows_count+1):
        form_type = scraper.GetText(f'/html/body/main/div[5]/div/div[3]/div[3]/div[2]/table/tbody/tr[{i}]/td[1]')

        if form_type != "10-K":
            continue

        filing_link = scraper.GetAttribute(f'/html/body/main/div[5]/div/div[3]/div[3]/div[2]/table/tbody/tr[{i}]/td[2]/div/a[1]', 'href')

        filing_link = filing_link.replace("ix?doc=", "") # Open HTML not iXBRL/XML

        filing_links.append(filing_link)

    for link in filing_links:
        print("maybe ok link: " + link)

        if "index.htm" in link:
            continue

        if ".txt" in link:
            continue

        print("ok link: " + link)

        scraper.OpenPage(filing_link)
        time.sleep(5)

        lines = []
        children = scraper.GetChildren('/html/body')
        for child in children:
            line = child.get_attribute('innerText')
            lines.append(line)

        # i have a bug:
        # https://chatgpt.com/c/6807fe9e-a7d4-8010-9048-778074c7e67b

        # do someting, like save the report text to a folder or extract financials immediately

    time.sleep(600)