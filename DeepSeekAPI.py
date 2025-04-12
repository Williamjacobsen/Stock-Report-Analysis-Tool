from openai import OpenAI
import os
import sys
from dotenv import load_dotenv

load_dotenv()

def analyze_financial_data(question, data_path="./ExtractFinancialsFromPDF/financials_output_unpolished.txt"):
    try:
        with open(data_path, 'r', encoding='utf-8') as file:
            financial_data = file.read()
    except FileNotFoundError:
        print(f"Error: Data file {data_path} not found")
        return

    prompt = f"""Please turn this random financial data into json format:
    
    Financial Data:
    {financial_data}
    """ # Truncate to first 3000 characters to stay within token limits

    api_key = os.getenv("DEEPSEEK_API_SK")
    if not api_key:
        print("Error: DeepSeek API key not found in environment variables")
        return

    client = OpenAI(
        api_key=api_key,
        base_url="https://api.deepseek.com/v1",
    )

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",  # Check latest model name in DeepSeek docs
            messages=[
                {"role": "system", "content": "You are a financial expert analyzing corporate reports."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=5000
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error making API call: {str(e)}")
        return None

if __name__ == "__main__":
    question = "Please turn this random financial data in to a json format"
    answer = analyze_financial_data(question)
    print(answer)