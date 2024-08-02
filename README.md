# OBS RSS Headline Ticker

**OBS RSS Headline Ticker** is a Python script designed to fetch RSS feed headlines and display them as text in an OBS (Open Broadcaster Software) text source. This script is intended for use with OBS WebSocket 5.0.1 and requires configuration to connect to your OBS instance.

## Requirements

- **OBS Studio**: Ensure you have OBS Studio installed on your system.
- **OBS WebSocket**: You need to have OBS WebSocket 5.0.1 installed. You can download it from [the official GitHub repository](https://github.com/obsproject/obs-websocket/releases/tag/5.0.1).
- **Python**: This script is compatible with Python 3.x.
- **Python Packages**: The script requires the `obs-websocket-py` and `feedparser` packages.

## Installation

1. **Install OBS WebSocket:**
   - Download and install the `obs-websocket-5.0.1` package from [this link](https://github.com/obsproject/obs-websocket/releases/tag/5.0.1).
   - After installation, configure the WebSocket server in OBS to enable remote control.

2. **Install Required Python Packages:**
   - Create a virtual environment if you haven't already:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     ```bash
     # On Windows
     venv\Scripts\activate

     # On macOS/Linux
     source venv/bin/activate
     ```
   - Install the required Python packages:
     ```bash
     pip install obs-websocket-py feedparser
     ```

## Configuration

1. **Configure OBS WebSocket:**
   - Open OBS Studio.
   - Go to `Tools` -> `WebSocket Server Settings`.
   - Ensure the WebSocket server is enabled and note the port (default is 4455) and password.

2. **Update Configuration in the Script:**
   - Edit the `test.py` script to configure the WebSocket connection details:
     ```python
     OBS_HOST = 'localhost'
     OBS_PORT = 4455  # Change this if your WebSocket port is different
     OBS_PASSWORD = 'your_websocket_password_here'  # Set the WebSocket password
     RSS_URL = 'https://www.example.com/rss'  # Replace with the desired RSS feed URL
     TEXT_SOURCE_NAME = 'test'  # Set this to the name of your text source in OBS
     ```

## Usage

1. **Run the Script:**
   ```bash
   python test.py


## Demo Video

![Demo](./headline-ticker.mp4)
