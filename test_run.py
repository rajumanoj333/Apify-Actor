#!/usr/bin/env python3

# Simple test script to demonstrate how the actor works
import asyncio
import sys
import os

# Add src to path so we can import the main module
sys.path.insert(0, 'src')

# Set environment variables to simulate Apify environment
os.environ['APIFY_LOCAL_STORAGE_DIR'] = './storage'

def main():
    print("Telangana Colleges Scraper - Apify Actor")
    print("=" * 40)
    print("To run this actor, you need:")
    print("1. A valid Google Places API key")
    print("2. Install dependencies with: pip install -r requirements.txt")
    print("")
    print("With a valid API key, you can run:")
    print("APIFY_LOCAL_STORAGE_DIR=./storage python -m src.main")
    print("")
    print("Or using Apify CLI:")
    print("apify run --input-file input.json")
    print("")
    print("The input.json file should contain:")
    print('{')
    print('  "googleApiKey": "YOUR_ACTUAL_GOOGLE_API_KEY",')
    print('  "maxImages": 3')
    print('}')
    print("")
    print("Features of this Actor:")
    print("- Scrapes Engineering, Medical, Degree, and Polytechnic colleges in Telangana")
    print("- Extracts college name, district, address, coordinates")
    print("- Gets Google Maps links, ratings, and reviews")
    print("- Downloads Google Images of colleges")
    print("- Outputs structured data for dashboards")

if __name__ == "__main__":
    main()