import os
import json
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()


def optimize_fonts(raw_fonts_path):
    """
    Optimize raw fonts JSON by removing unnecessary keys.
    Creates a .optimize.json file from the raw_fonts.json file.
    
    Removes from root level: version, lastModified, menu
    Removes from each item: version, lastModified, menu, kind
    Optionally removes: files (if IS_IGNORE_FILES=1)
    """
    raw_path = Path(raw_fonts_path)
    
    with open(raw_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    data.pop('version', None)
    data.pop('lastModified', None)
    data.pop('menu', None)
    
    is_ignore_files = os.getenv('IS_IGNORE_FILES', '0') == '1'
    items = data.get('items', [])
    for item in items:
        item.pop('version', None)
        item.pop('lastModified', None)
        item.pop('menu', None)
        item.pop('kind', None)
        if is_ignore_files:
            item.pop('files', None)
    
    optimize_filename = raw_path.stem + '.optimize.json'
    optimize_path = raw_path.parent / optimize_filename
    
    with open(optimize_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"Saved optimized {len(data.get('items', []))} fonts to {optimize_path}")
