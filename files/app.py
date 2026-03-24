import datetime
from zoneinfo import ZoneInfo

def display_world_times():
    # Define the regions/time zones you want to display
    regions = {
        "London": "Europe/London",
        "New York": "America/New_York",
        "Tokyo": "Asia/Tokyo",
        "Sydney": "Australia/Sydney",
        "Mumbai": "Asia/Kolkata",
        "Dubai": "Asia/Dubai"
    }

    print(f"{'Region':<15} | {'Date':<12} | {'Time (24h)':<10}")
    print("-" * 43)

    for city, zone in regions.items():
        try:
            # Get current time for the specific time zone
            now = datetime.datetime.now(ZoneInfo(zone))
            
            date_str = now.strftime("%Y-%m-%d")
            time_str = now.strftime("%H:%M:%S")
            
            print(f"{city:<15} | {date_str:<12} | {time_str:<10}")
        except Exception as e:
            print(f"Could not retrieve time for {city}: {e}")

if __name__ == "__main__":
    display_world_times()
