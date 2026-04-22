# Data cleaning script
# Purpose: Clean raw scraped data for database storage
# Input: data/raw_data.csv (raw scraped book prices)
# Output: data/cleaned_data.csv (cleaned & standardized data)

import pandas as pd

def clean():
    """
    Clean raw scraped data with the following transformations:
    
    1. Remove currency symbols (£) - Books.toscrape uses British Pounds
    2. Remove encoding artifacts (Â) - UTF-8 encoding issues from HTML
    3. Strip whitespace - Handle extra spaces from HTML parsing
    4. Remove null values - Drop rows with missing data (incomplete records)
    5. Convert to float - Standardize price format for database storage
    6. Remove duplicates - Handle repeated scrapes of same products
    """
    df = pd.read_csv("data/raw_data.csv", encoding='utf-8-sig')

    # Decision: Strip currency symbols and encoding artifacts
    # Reason: Need numeric values for price calculations and comparisons
    df["price"] = df["price"].str.replace("£", "").str.replace("Â", "").str.strip()

    # Decision: Drop rows with missing names or prices
    # Reason: Can't use incomplete product records for analysis
    df.dropna(inplace=True)

    # Decision: Convert price to float type
    # Reason: Required for aggregation (e.g., average price calculation)
    # Also handles any remaining invalid prices with 'coerce' parameter
    df["price"] = pd.to_numeric(df["price"], errors='coerce')
    
    # Remove rows where conversion failed (invalid prices)
    df.dropna(inplace=True)

    # Decision: Remove duplicate rows
    # Reason: Website might return same products across different pages
    df.drop_duplicates(inplace=True)

    # Save cleaned data to CSV
    df.to_csv("data/cleaned_data.csv", index=False)

    print("Cleaning Done")

if __name__ == "__main__":
    clean()