import os
from streetview import search_panoramas, get_panorama_meta, get_streetview, get_panorama
from dotenv import load_dotenv
from datetime import datetime

# Load variables from .env file
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("GOOGLE_API_KEY")

# Check if API key is available
if not api_key:
    print("Error: GOOGLE_API_KEY environment variable is not set!")
    exit(1)

# Search for panoramas at the given coordinates (Rome, Italy)
print("Searching for panoramas...")
panos = search_panoramas(lat=41.8982208, lon=12.4764804)

# Check if any panoramas were found
if not panos:
    print("No panoramas found at the specified coordinates!")
    exit(1)

print(f"Found {len(panos)} panorama(s)")

# Use the first panorama (index 0 is safer than index 1)
pano_id = panos[0].pano_id

print("Panorama ID:", pano_id)

# Create 'static' folder if it doesn't exist
folder = "static"
os.makedirs(folder, exist_ok=True)

# Download the street view image
try:
    print("Downloading street view image...")
    image = get_streetview(
        pano_id=pano_id,
        api_key=api_key,
    )
    print("Image downloaded successfully!")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save the image
    filename = os.path.join(folder, f"street_view_{timestamp}.jpg")
    image.save(filename, "jpeg")
    print(f"Image saved as '{filename}'")
    
except Exception as e:
    print(f"Error downloading street view image: {e}")