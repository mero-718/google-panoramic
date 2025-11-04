# Google Street View Panorama Downloader

A Python application that searches for and downloads Google Street View panoramic images from specified geographic coordinates.

## 🚀 Features

- Search for available Street View panoramas at given coordinates
- Download high-quality panoramic images
- Automatic timestamped file naming
- Environment variable configuration for API security
- Error handling and validation
- Organized file structure with static folder for images

## 📋 Prerequisites

- Python 3.9 or higher
- Google Street View Static API key

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mero-718/google-panoramic.git
   cd google-panoramic
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   ```bash
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

4. **Install required packages:**
   ```bash
   pip install streetview python-dotenv pillow
   ```

## 🔑 API Setup

1. **Get a Google Street View Static API key:**
   - Go to the [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select an existing one
   - Enable the "Street View Static API"
   - Create credentials (API key)
   - Optionally, restrict the API key to Street View Static API for security

2. **Configure your API key:**
   - Create a `.env` file in the project root
   - Add your API key:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```

## 🚀 Usage

### Basic Usage

Run the main script to download a Street View image from Rome, Italy:

```bash
python main.py
```

or

```bash
python street_view.py
```

### Customizing Coordinates

To download images from different locations, modify the coordinates in the script:

```python
# Change these coordinates to your desired location
panos = search_panoramas(lat=41.8982208, lon=12.4764804)  # Rome, Italy
```

### Example Coordinates

- **New York City**: `lat=40.7128, lon=-74.0060`
- **Tokyo**: `lat=35.6762, lon=139.6503`
- **London**: `lat=51.5074, lon=-0.1278`
- **Sydney**: `lat=-33.8688, lon=151.2093`

## 📁 Project Structure

```
google-panoramic/
│
├── main.py              # Main application script
├── street_view.py       # Alternative script (identical functionality)
├── .env                 # Environment variables (API key)
├── .gitignore          # Git ignore rules
├── README.md           # This file
├── static/             # Downloaded images folder
│   └── street_view_*.jpg
└── venv/               # Virtual environment (not in git)
```

## 📸 Output

Downloaded images are saved in the `static/` folder with timestamped filenames:
- Format: `street_view_YYYYMMDD_HHMMSS.jpg`
- Example: `street_view_20231105_143022.jpg`