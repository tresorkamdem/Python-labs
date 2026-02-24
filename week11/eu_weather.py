import requests
import json
import time
from datetime import datetime

# EU Capitals with coordinates
EU_CAPITALS = [
    {"city": "Vienna", "country": "Austria", "lat": 48.2082, "lon": 16.3738},
    {"city": "Berlin", "country": "Germany", "lat": 52.5200, "lon": 13.4050},
    {"city": "Paris", "country": "France", "lat": 48.8566, "lon": 2.3522},
    {"city": "Rome", "country": "Italy", "lat": 41.9028, "lon": 12.4964},
    {"city": "Madrid", "country": "Spain", "lat": 40.4168, "lon": -3.7038},
    {"city": "Warsaw", "country": "Poland", "lat": 52.2297, "lon": 21.0122},
    {"city": "Amsterdam", "country": "Netherlands", "lat": 52.3676, "lon": 4.9041},
    {"city": "Brussels", "country": "Belgium", "lat": 50.8503, "lon": 4.3517}
]

API_URL = "https://api.open-meteo.com/v1/forecast"


def fetch_weather(lat, lon):
    """Fetch weather data from Open-Meteo API."""
    today = datetime.now().strftime("%Y-%m-%d")

    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        "hourly": "temperature_2m,precipitation_probability,weathercode",
        "start_date": today,
        "end_date": today,
        "timezone": "auto"
    }

    try:
        response = requests.get(API_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
        return None


def process_weather(data, city, country):
    """Structure API data."""
    try:
        current = data.get("current_weather", {})

        return {
            "city": city,
            "country": country,
            "coordinates": {
                "latitude": data.get("latitude"),
                "longitude": data.get("longitude")
            },
            "current_weather": {
                "temperature": current.get("temperature"),
                "windspeed": current.get("windspeed"),
                "weathercode": current.get("weathercode"),
                "time": current.get("time")
            }
        }
    except Exception as e:
        print(f"Processing error for {city}: {e}")
        return None


def collect_weather_data():
    """Collect weather for all capitals."""
    results = {}

    print("Collecting EU capital weather data...\n")

    for capital in EU_CAPITALS:
        city = capital["city"]
        print(f"Fetching {city}...")

        raw = fetch_weather(capital["lat"], capital["lon"])

        if raw:
            processed = process_weather(raw, city, capital["country"])
            if processed:
                results[city] = processed
                print(f"Success: {city}")
        else:
            print(f"Failed: {city}")

        time.sleep(1)  # rate limiting

    return results


def save_to_json(data, filename="eu_weather_data.json"):
    """Save data to JSON file."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print(f"\nSaved data to {filename}")
    except IOError as e:
        print(f"File write error: {e}")


def main():
    data = collect_weather_data()
    save_to_json(data)

    if not data:
        print("No data collected.")
        return

    temps = [
        d["current_weather"]["temperature"]
        for d in data.values()
        if d["current_weather"]["temperature"] is not None
    ]

    if temps:
        avg = sum(temps) / len(temps)
        hottest = max(data.values(), key=lambda x: x["current_weather"]["temperature"])
        coldest = min(data.values(), key=lambda x: x["current_weather"]["temperature"])

        print("\nSummary:")
        print(f"Average temperature: {avg:.2f}°C")
        print(f"Hottest: {hottest['city']}")
        print(f"Coldest: {coldest['city']}")
    else:
        print("No temperature data available.")


if __name__ == "__main__":
    main()