# https://www.sec.gov/edgar/browse/?CIK=320193&owner=exclude


if __name__ == '__main__':
    from Scraper import Scraper
    import time

    scraper = Scraper()

    scraper.OpenPage('https://www.sec.gov/edgar/browse/?CIK=320193&owner=exclude')

    # View filings
    scraper.ClickElement('/html/body/main/div[4]/div[1]/div/div/button[1]')

    # Clear date field
    scraper.Send_keysElement('/html/body/main/div[5]/div/div[1]/div[1]/div/input[3]', scraper.keys.CONTROL, 'a', scraper.keys.BACKSPACE, '\n')
    
    # Sort by form type
    scraper.ClickElement('/html/body/main/div[5]/div/div[3]/div[3]/div[1]/div/table/thead/tr/th[1]')
    
    time.sleep(5)

    rows_count = scraper.CountChildren('/html/body/main/div[5]/div/div[3]/div[3]/div[2]/table/tbody')

    for i in range(1, rows_count+1):
        form_type = scraper.LocateElement(f'/html/body/main/div[5]/div/div[3]/div[3]/div[2]/table/tbody/tr[{i}]/td[1]')

        if form_type != "10-K":
            continue

        print(form_type)

    time.sleep(600)