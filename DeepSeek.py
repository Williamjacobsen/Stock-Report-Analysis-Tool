import os
import time
from dotenv import load_dotenv
from Scraper import Scraper

def Clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def SignIntoDeepSeek(scraper):
    scraper.OpenPage('https://chat.deepseek.com/')

    scraper.LocateElement('/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div/div[2]/div[1]/div/')

    # EMAIL FIELD
    # /html/body/div[1]/div[1]/div[2]/div/div/div[2]/div/div[2]/div[1]/div/input
    scraper.Send_keysElement(
        '/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div/div[2]/div[1]/div/input', 
        os.environ.get('EMAIL')
        )

    # PASSWORD FIELD
    # /html/body/div[1]/div[1]/div[2]/div/div/div[2]/div/div[3]/div[1]/div/input
    scraper.Send_keysElement(
        '/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div/div[3]/div[1]/div/input',
        os.environ.get('PASSWORD')
        )

    # LOGIN BUTTON
    # /html/body/div[1]/div[1]/div[2]/div/div/div[2]/div/div[5]
    scraper.ClickElement('/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div/div[5]')

def InitialPrompt(scraper, prompt="Test Prompt"):
    # Wait for prompt field to load
    scraper.LocateElement('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[1]/textarea')

    # (Prompt Options) DeepThink Button
    # /html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[2]/div[1]/span
    scraper.ClickElement('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[2]/div[1]/span')

    # (Prompt Options) Search Button
    # /html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[2]/div[2]/span
    scraper.ClickElement('/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[2]/div[2]/span')

    # INITIAL PROMPT FIELD
    # /html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[1]/textarea
    scraper.Send_keysElement(
        '/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[1]/textarea',
        prompt+'\n'
        )

if __name__ == '__main__':
    Clear()
    load_dotenv()

    scraper = Scraper()

    SignIntoDeepSeek(scraper)
    InitialPrompt(
        scraper=scraper, 
        prompt="I will link you pdf file then you need to return every financial value like revenue net income etc."
        )



    input("")

    