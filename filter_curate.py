import json
from pathlib import Path
from datetime import datetime


def get_output_dir(date_str=None):
    """Get output directory with yyyy-mm-dd subfolder structure."""
    if date_str is None:
        date_str = datetime.now().strftime('%Y-%m-%d')
    output_dir = Path('output') / date_str
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


def load_fonts(input_file=None, date_str=None):
    """Load fonts from the raw JSON file."""
    if input_file is None:
        output_dir = get_output_dir(date_str)
        input_file = output_dir / 'raw_fonts.json'
    with open(input_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def filter_top_n(data, n=20):
    """
    Filter and extract the top N most popular fonts.
    
    Args:
        data: Dictionary with 'items' key containing list of fonts
        n: Number of top fonts to return (default 20)
    
    Returns:
        Dictionary with top N fonts
    """
    items = data.get('items', [])
    top_n_items = items[:n]
    
    return {
        'items': top_n_items,
        'count': len(top_n_items)
    }


def filter_vietnamese(data):
    """
    Filter all fonts that support Vietnamese subset.
    
    Args:
        data: Dictionary with 'items' key containing list of fonts
    
    Returns:
        Dictionary with fonts supporting Vietnamese
    """
    items = data.get('items', [])
    vietnamese_items = [
        font for font in items 
        if 'vietnamese' in font.get('subsets', [])
    ]
    
    return {
        'items': vietnamese_items,
        'count': len(vietnamese_items)
    }


def save_fonts(data, output_file, output_dir=None):
    """Save fonts data to JSON file."""
    if output_dir is None:
        output_dir = get_output_dir()
    
    output_path = output_dir / output_file
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"Saved {data.get('count', 0)} fonts to {output_path}")


def main(input_file=None, top_n=20, date_str=None):
    """
    Process fonts data: extract top N and Vietnamese fonts.
    
    Args:
        input_file: Path to raw fonts JSON file (default: output/yyyy-mm-dd/raw_fonts.json)
        top_n: Number of top fonts to extract (default 20)
        date_str: Date folder in yyyy-mm-dd format (default: today's date)
    """
    data = load_fonts(input_file, date_str)
    output_dir = get_output_dir(date_str)
    
    top_n_data = filter_top_n(data, n=top_n)
    save_fonts(top_n_data, f'top_{top_n}_fonts.json', output_dir)
    
    vietnamese_data = filter_vietnamese(data)
    save_fonts(vietnamese_data, 'vietnamese_fonts.json', output_dir)


if __name__ == '__main__':
    main()
