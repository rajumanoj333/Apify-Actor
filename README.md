# Telangana Colleges Scraper

This Apify actor scrapes information about colleges in Telangana state from Google Places API, including engineering, medical, degree, and polytechnic colleges.

## Features

The actor extracts the following information for each college:
- College name
- District (Hyderabad, Warangal, Karimnagar, etc.)
- Category (Engineering, Medical, Degree, Polytechnic)
- Address
- Google Maps link
- Latitude & longitude
- Google Images
- Google rating & total reviews

## Input Parameters

- `googleApiKey`: Your Google Places API key (required)
- `maxImages`: Maximum number of images to fetch per college (default: 5)

## Output

The actor outputs a dataset with college information that can be used for dashboards, parent-student platforms, or educational portals.