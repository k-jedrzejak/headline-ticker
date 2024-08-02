import feedparser
import time
from obswebsocket import obsws, requests, exceptions

# Configuration
OBS_HOST = 'localhost'
OBS_PORT = 4455
OBS_PASSWORD = '<your-password>'
RSS_URL = '<feeds ur>' #e.g https://www.prlog.org/news/rss.xml
TEXT_SOURCE_NAME = '<source name>'
UPDATE_INTERVAL = 60  # seconds
MAX_HEADLINES = 5  # Limit the number of headlines
MAX_HEADLINE_LENGTH = 20

def fetch_rss_headlines(url):
    """Fetch headlines from RSS feed and return a list of formatted headlines."""
    print(f"Fetching RSS feed from {url} at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    feed = feedparser.parse(url)
    if 'entries' in feed:
        headlines = [entry.title[:MAX_HEADLINE_LENGTH] for entry in feed.entries[:MAX_HEADLINES]]
        return headlines
    else:
        print("Error fetching RSS feed.")
        return []

def set_text_source(ws, source_name, new_text):
    """Update the OBS text source with the given text."""
    try:
        print(f"Updating text source '{source_name}' with new text: '{new_text}'...")

        # Get the current settings for the input
        response = ws.call(requests.GetInputSettings(inputName=source_name))
        
        # Access the response data
        response_data = response.data()  # Call the method to get data
        print(f"Response data: {response_data}")

        # Extract the settings from the data
        settings = response_data.get('inputSettings', {})
        print(f"Current settings: {settings}")

        # Update the settings with the new text
        settings['text'] = new_text
        print(f"Updated settings: {settings}")

        # Send the updated settings to OBS
        update_response = ws.call(requests.SetInputSettings(inputName=source_name, inputSettings=settings))

        # Print the update response
        print(f"Update response: {update_response}")

        if update_response.status == 'ok':
            print("Successfully updated text source.")
        else:
            print(f"Failed to update text source: {update_response.status}")
            print(f"Update response details: {update_response.data()}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def main():
    ws = obsws(OBS_HOST, OBS_PORT, OBS_PASSWORD)

    # Connect to OBS WebSocket
    try:
        ws.connect()
        print("Connected to OBS WebSocket")
    except exceptions.ConnectionFailure:
        print("Failed to connect to OBS WebSocket, retrying in 5 seconds...")
        time.sleep(5)
        return

    try:
        while True:
            headlines = fetch_rss_headlines(RSS_URL)
            if headlines:
                headlines_text = '\n'.join(headlines)
                print(f"Fetched headlines: {headlines_text}")
                set_text_source(ws, TEXT_SOURCE_NAME, headlines_text)
            else:
                print("No headlines found.")
            time.sleep(UPDATE_INTERVAL)
            
    except KeyboardInterrupt:
        print("Script interrupted by user")
    finally:
        ws.disconnect()
        print("Disconnected from OBS WebSocket")

if __name__ == '__main__':
    main()
