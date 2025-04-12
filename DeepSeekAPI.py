import PyPDF2
from openai import OpenAI
import os
from dotenv import load_dotenv
import tiktoken

# Load environment variables
load_dotenv()

# Initialize tokenizer for precise token counting
encoder = tiktoken.get_encoding("cl100k_base")

def calculate_tokens(text):
    return len(encoder.encode(text))

def extract_pdf_text(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        return " ".join([page.extract_text() for page in reader.pages])

def process_large_document(pdf_path, prompt):
    client = OpenAI(
        api_key=os.environ.get("DEEPSEEK_API_SK"),
        base_url="https://api.deepseek.com"
    )
    
    # Extract and compress text
    full_text = extract_pdf_text(pdf_path)
    compressed_text = " ".join(full_text.split())  # Remove redundant whitespace
    
    # Calculate token limits
    prompt_tokens = calculate_tokens(prompt)
    max_total_tokens = 65536  # DeepSeek's context limit
    max_response_tokens = 1000
    available_tokens = max_total_tokens - prompt_tokens - max_response_tokens - 500  # Safety buffer
    
    # Split text into manageable chunks
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=available_tokens,
        chunk_overlap=200,
        length_function=calculate_tokens
    )
    
    chunks = text_splitter.split_text(compressed_text)
    
    # Process each chunk and combine results
    summaries = []
    for chunk in chunks:
        response = client.chat.completions.create(
            model="deepseek-reasoner",
            messages=[
                {"role": "system", "content": "You are a research assistant. Analyze this text chunk:"},
                {"role": "user", "content": f"{prompt}\n\n{chunk}"}
            ],
            temperature=0.3,
            max_tokens=max_response_tokens
        )
        summaries.append(response.choices[0].message.content)
    
    # Create final summary
    final_response = client.chat.completions.create(
        model="deepseek-reasoner",
        messages=[
            {"role": "system", "content": "Combine these summaries into a coherent final report:"},
            {"role": "user", "content": "\n".join(summaries)}
        ],
        temperature=0.3,
        max_tokens=2000
    )
    
    return final_response.choices[0].message.content

# Usage
pdf_path = "report1.pdf"
summary = process_large_document(pdf_path, """Extract financial data into this JSON format:
{
{
  "ticker": {
    "2001": {
      "Period": "Jan 01, 2000 - Jan 01, 2001",
      "Income": {
        "Revenue": {
          "Revenue": 0,
          "Revenue Per Product": [
            { "Iphone": 0 },
            { "Mac": 0 },
            { "Etc etc.": 0 }
          ],
          "Cost of Revenue": 0
        },
        "Gross Profit": {
          "Gross Profit": 0,
          "Gross Margin": 0,
          "Selling, General & Admin": 0,
          "Research & Development": 0,
          "Operating Expenses": 0
        },
        "Operating Income": {
          "Operating Income": 0,
          "Operating Margin": 0,
          "Interest & Investment Income": 0,
          "Other Non Operating Income (Expense)": 0
        },
        "Pretax Income": {
          "Pretax Income": 0,
          "Income Tax Expense": 0
        },
        "Net Income": {
          "Net Income": 0,
          "Net Income to Common": 0,
          "Profit Margin": 0
        },
        "Shares Outstanding": {
          "Shares Outstanding (Basic)": 0,
          "Shares Outstanding (Diluted)": 0
        },
        "EPS": {
          "EPS (Basic)": 0,
          "EPS (Diluted)": 0
        },
        "Free Cash Flow": {
          "Free Cash Flow": 0,
          "Free Cash Flow Per Share": 0,
          "Free Cash Flow Margin": 0
        },
        "Dividend Per Share": 0,
        "EBITDA": {
          "EBITDA": 0,
          "EBITDA Margin": 0,
          "D&A For EBITDA": 0
        },
        "EBIT": {
          "EBIT": 0,
          "EBIT Margin": 0
        },
        "Effective Tax Rate": 0,
        "Revenue as Reported": 0
      },
      "Balance Sheet": {
        "Assets": {
          "Total Assets": 0,
          "Current Assets": {
            "Total Current Assets": 0,
            "Cash & Short-Term Investments": {
              "Cash & Equivalents": 0,
              "Short-Term Investments": 0,
              "Cash & Short-Term Investments Total": 0
            },
            "Receivables": {
              "Accounts Receivable": 0,
              "Other Receivables": 0,
              "Receivables Total": 0
            },
            "Inventory": 0,
            "Other Current Assets": 0
          },
          "Long-Term Assets": {
            "Total Long-Term Assets": 0,
            "Property, Plant & Equipment": {
              "Land": 0,
              "Machinery": 0,
              "Leasehold Improvements": 0,
              "Property, Plant & Equipment Total": 0
            },
            "Long-Term Investments": 0,
            "Long-Term Deferred Tax Assets": 0,
            "Other Long-Term Assets": 0
          }
        },
        "Liabilities": {
          "Total Liabilities": 0,
          "Current Liabilities": {
            "Total Current Liabilities": 0,
            "Accounts Payable": 0,
            "Short-Term Debt": 0,
            "Current Portion of Long-Term Debt": 0,
            "Current Portion of Leases": 0,
            "Current Income Taxes Payable": 0,
            "Current Unearned Revenue": 0,
            "Other Current Liabilities": 0
          },
          "Long-Term Liabilities": {
            "Total Long-Term Liabilities": 0,
            "Long-Term Debt": 0,
            "Long-Term Leases": 0,
            "Other Long-Term Liabilities": 0
          }
        },
        "Equity": {
          "Common Stock": 0,
          "Retained Earnings": 0,
          "Comprehensive Income & Other": 0,
          "Shareholders' Equity": 0,
          "Total Liabilities & Equity": 0
        },
        "Metrics": {
          "Total Debt": 0,
          "Net Cash (Debt)": 0,
          "Net Cash Per Share": 0,
          "Working Capital": 0,
          "Book Value Per Share": 0,
          "Tangible Book Value": 0,
          "Tangible Book Value Per Share": 0,
          "Shares Data": {
            "Filing Date Shares Outstanding": 0,
            "Total Common Shares Outstanding": 0
          }
        }
      },
      "Cash Flow": {
        "Operating Activities": {
          "Net Income": 0,
          "Addbacks & Adjustments": {
            "Depreciation & Amortization": 0,
            "Stock-Based Compensation": 0,
            "Other Operating Activities": 0
          },
          "Operating Cash Flow": 0
        },
        "Investing Activities": {
          "Capital Expenditures": 0,
          "Acquisitions": {
            "Cash Acquisitions": 0
          },
          "Investments": {
            "Investment in Securities": 0
          },
          "Other Investing Activities": 0,
          "Investing Cash Flow": 0
        },
        "Financing Activities": {
          "Debt Activity": {
            "Issued": {
              "Short-Term Debt Issued": 0,
              "Long-Term Debt Issued": 0,
              "Total Debt Issued": 0
            },
            "Repaid": {
              "Short-Term Debt Repaid": 0,
              "Long-Term Debt Repaid": 0,
              "Total Debt Repaid": 0
            },
            "Net Debt Issued (Repaid)": 0
          },
          "Equity Activity": {
            "Repurchase of Common Stock": 0,
            "Common Dividends Paid": 0
          },
          "Other Financing Activities": 0,
          "Financing Cash Flow": 0
        },
        "Metrics": {
          "Net Cash Flow": 0,
          "Free Cash Flow": {
            "Free Cash Flow": 0,
            "Free Cash Flow Margin": 0,
            "Free Cash Flow Per Share": 0
          },
          "Cash Payments": {
            "Cash Interest Paid": 0,
            "Cash Income Tax Paid": 0
          },
          "Advanced Metrics": {
            "Levered Free Cash Flow": 0,
            "Unlevered Free Cash Flow": 0
          }
        }
      },
      "Ratios": {
        "Valuation": {
          "Market Metrics": {
            "Market Capitalization": 0,
            "Enterprise Value": 0,
            "Last Close Price": 0
          },
          "Price Ratios": {
            "PE Ratio": 0,
            "Forward PE": 0,
            "PS Ratio": 0,
            "PB Ratio": 0,
            "P/TBV Ratio": 0,
            "P/FCF Ratio": 0,
            "P/OCF Ratio": 0,
            "PEG Ratio": 0
          },
          "Enterprise Value Ratios": {
            "EV/Sales Ratio": 0,
            "EV/EBITDA Ratio": 0,
            "EV/EBIT Ratio": 0,
            "EV/FCF Ratio": 0
          }
        },
        "Leverage": {
          "Debt Ratios": {
            "Debt/Equity Ratio": 0,
            "Debt/EBITDA Ratio": 0,
            "Debt/FCF Ratio": 0
          }
        },
        "Efficiency": {
          "Turnover Ratios": {
            "Asset Turnover": 0,
            "Inventory Turnover": 0
          },
          "Liquidity Ratios": {
            "Quick Ratio": 0,
            "Current Ratio": 0
          }
        },
        "Profitability": {
          "Return Ratios": {
            "Return on Equity (ROE)": 0,
            "Return on Assets (ROA)": 0,
            "Return on Capital (ROIC)": 0,
            "Return on Capital Employed (ROCE)": 0
          }
        },
        "Yield & Payout": {
          "Yields": {
            "Earnings Yield": 0,
            "FCF Yield": 0,
            "Dividend Yield": 0
          },
          "Payout Metrics": {
            "Payout Ratio": 0,
            "Buyback Yield/Dilution": 0
          }
        },
        "Shareholder Returns": {
          "Total Shareholder Return": 0
        }
      },
      "metadata": {
        "currency": "USD",
        "units": "millions",
        "reporting_standard": "GAAP",
        "filing_date": "2001-03-01"
      }
    }
  }
}
""")
print("Final Summary:", summary)

"""
instead of a summary it should return the financial data and save it to a json file named "ticker".json

{
  "aapl": {
    "2024": {
      "Period": "Jan 01, 2000 - Jan 01, 2001",
      "Income": {},
      "Balance Sheet": {},
      "Cash Flow": {},
      "Ratios": {}
      }
    }
  }
}

"""