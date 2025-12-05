import os
import requests
import json
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv


load_dotenv()


def get_output_dir():
    """Create output directory with yyyy-mm-dd subfolder structure."""
    date_folder = datetime.now().strftime('%Y-%m-%d')
    output_dir = Path('output') / date_folder
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


def fetch_fonts():
    """
    Fetch fonts from Google Fonts API and save to output/yyyy-mm-dd/raw_fonts.json.
    
    API Key is retrieved from GOOGLE_FONTS_API_KEY environment variable.
    Results are sorted by popularity.
    """
    api_key = os.getenv('GOOGLE_FONTS_API_KEY')
    
    if not api_key:
        raise ValueError("GOOGLE_FONTS_API_KEY environment variable not set")
    
    url = "https://www.googleapis.com/webfonts/v1/webfonts"
    params = {
        'key': api_key,
        'sort': 'popularity'
    }
    
    response = requests.get(url, params=params)
    response.raise_for_status()
    
    data = response.json()
    
    output_dir = get_output_dir()
    output_file = output_dir / 'raw_fonts.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"Saved {len(data.get('items', []))} fonts to {output_file}")


if __name__ == '__main__':
    fetch_fonts()
