# gg-font-curator

A collection of Python scripts to interact with the Google Fonts API, enabling easy listing, sorting, and fetching of font metadata (trending, popular, etc.)

## Features

- **Fetch Fonts**: Retrieve all Google Fonts from the official API, sorted by popularity
- **Filter Top N**: Extract the top N most popular fonts
- **Localization Filter**: Extract all fonts that support Vietnamese subset
- **Date-organized Output**: Automatically organize results in `output/yyyy-mm-dd/` folders
- **Secure API Key Management**: Use `.env` file for API key configuration

## Installation

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Setup

1. **Clone the repository** (if not already done):
   ```bash
   git clone https://github.com/yourusername/gg-font-curator.git
   cd gg-font-curator
   ```

2. **Create and activate virtual environment**:
   
   **On Linux/macOS:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
   
   **On Windows:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create `.env` file** with your Google Fonts API key:
   ```bash
   cp .env.example .env
   ```
   Then edit `.env` and add your API key:
   ```
   GOOGLE_FONTS_API_KEY=your_actual_api_key_here
   ```

   **To get a Google Fonts API key:**
   - Visit [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project
   - Enable the Google Fonts Developer API
   - Create an API key credential
   - Copy the key to your `.env` file

## Usage

### 1. Fetch Fonts from Google Fonts API

Retrieves all fonts from Google Fonts API and saves them to `output/yyyy-mm-dd/raw_fonts.json`:

```bash
python fetch_data.py
```

**Output:**
```
Saved 1500+ fonts to output/2025-12-05/raw_fonts.json
```

### 2. Filter and Curate Fonts

Process the fetched fonts to extract:
- Top 20 most popular fonts → `output/yyyy-mm-dd/top_20_fonts.json`
- All Vietnamese-supported fonts → `output/yyyy-mm-dd/vietnamese_fonts.json`

```bash
python filter_curate.py
```

**To extract top 30 fonts instead:**

```python
from filter_curate import main
main(top_n=30)
```

**To process data from a specific date:**

```python
from filter_curate import main
main(top_n=20, date_str='2025-12-04')
```

## Output Structure

```
output/
├── 2025-12-05/
│   ├── raw_fonts.json          # All fonts from API
│   ├── top_20_fonts.json        # Top 20 popular fonts
│   └── vietnamese_fonts.json    # Fonts with Vietnamese support
├── 2025-12-04/
│   ├── raw_fonts.json
│   ├── top_20_fonts.json
│   └── vietnamese_fonts.json
└── ...
```

## JSON Output Format

### raw_fonts.json
```json
{
  "items": [
    {
      "family": "Open Sans",
      "variants": ["300", "400", "700", ...],
      "subsets": ["latin", "latin-ext", "vietnamese", ...],
      ...
    }
  ]
}
```

### top_20_fonts.json / vietnamese_fonts.json
```json
{
  "items": [...],
  "count": 20
}
```

## API Reference

### fetch_data.py

- **`fetch_fonts()`**: Fetches all fonts from Google Fonts API and saves to `output/yyyy-mm-dd/raw_fonts.json`

### filter_curate.py

- **`main(input_file=None, top_n=20, date_str=None)`**: Process fonts data and generate filtered outputs
  - `input_file`: Custom path to raw fonts JSON (default: auto-detected from date folder)
  - `top_n`: Number of top fonts to extract (default: 20)
  - `date_str`: Specific date folder in `yyyy-mm-dd` format (default: today's date)

- **`filter_top_n(data, n=20)`**: Extract top N fonts from data
- **`filter_vietnamese(data)`**: Extract Vietnamese-supported fonts
- **`load_fonts(input_file=None, date_str=None)`**: Load fonts from JSON file
- **`save_fonts(data, output_file, output_dir=None)`**: Save fonts to JSON file

## Environment Variables

Create a `.env` file in the project root:

```env
GOOGLE_FONTS_API_KEY=your_api_key_here
```

The `GOOGLE_FONTS_API_KEY` is required for `fetch_data.py` to work.

## Example Workflow

```bash
# Step 1: Fetch latest fonts from Google Fonts API
python fetch_data.py

# Step 2: Filter and curate fonts
python filter_curate.py
```

Check the `output/2025-12-05/` directory (today's date) for results.

## Requirements

See `requirements.txt` for all dependencies:
- `requests` - HTTP library for API calls
- `python-dotenv` - Environment variable management

## License

MIT License - see LICENSE file for details

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
