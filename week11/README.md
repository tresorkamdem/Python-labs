# Week 11 – EU Capitals Weather Data Collection

## Objective
This project collects weather data for selected European Union capital cities
using the Open-Meteo API. The application retrieves current weather data,
structures it properly, and saves the output to a JSON file.

## Features
- API integration using requests
- Iteration over multiple cities
- Error handling for failed requests
- Rate limiting (1 second delay)
- JSON output with structured format
- Summary statistics (average, hottest, coldest)

## Output
The script generates:
- eu_weather_data.json

## How to Run
pip install requests
python eu_weather.py