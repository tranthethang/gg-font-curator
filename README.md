# GG Font Curator

A collection of Python scripts to interact with the Google Fonts API, enabling easy listing, sorting, and fetching of font metadata (trending, popular, etc.)

## Features

- **Fetch Fonts**: Retrieve all Google Fonts from the official API, sorted by popularity
- **Filter Top N**: Extract the top N most popular fonts
- **Localization Filter**: Extract all fonts that support Vietnamese subset
- **Data Optimization**: Generate both raw and optimized JSON files (removes unnecessary keys)
- **File Reduction**: Optional removal of large `files` field to reduce file size
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

4. **Create `.env` file** with your configuration:
   ```bash
   cp .env.example .env
   ```
   Then edit `.env` and add your settings:
   ```
   GOOGLE_FONTS_API_KEY=your_actual_api_key_here
   IS_IGNORE_FILES=1
   ```

   **To get a Google Fonts API key:**
   - Visit [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project
   - Enable the Google Fonts Developer API
   - Create an API key credential
   - Copy the key to your `.env` file

## Usage

### CLI Commands

The project uses **Click** for command-line interface management. All commands are accessed through `main.py`.

### 1. Fetch Fonts from Google Fonts API

Retrieves all fonts from Google Fonts API and generates:
- `raw_fonts.json` - Complete data with all fields
- `raw_fonts.optimize.json` - Optimized version (removes unnecessary fields)

```bash
python main.py fetch
```

**Output:**
```
Saved 1500+ fonts to output/2025-12-05/raw_fonts.json
Saved optimized 1500+ fonts to output/2025-12-05/raw_fonts.optimize.json
```

### 2. Filter and Curate Fonts

Process the fetched fonts to extract:
- Top 20 most popular fonts → `top_20_fonts.json` and `top_20_fonts.optimize.json`
- All Vietnamese-supported fonts → `vietnamese_fonts.json` and `vietnamese_fonts.optimize.json`

```bash
python main.py filter
```

**Options:**

- `--top-n INTEGER`: Number of top fonts to extract (default: 20)
  ```bash
  python main.py filter --top-n 30
  ```

- `--date TEXT`: Process data from a specific date in `yyyy-mm-dd` format (default: today's date)
  ```bash
  python main.py filter --date 2025-12-04
  ```

- `--input-file TEXT`: Use a custom path to raw fonts JSON file
  ```bash
  python main.py filter --input-file /path/to/custom/raw_fonts.json
  ```

**Combined example:**

```bash
python main.py filter --top-n 30 --date 2025-12-04
```

**View help for any command:**

```bash
python main.py --help
python main.py fetch --help
python main.py filter --help
```

## Output Structure

```
output/
├── 2025-12-05/
│   ├── raw_fonts.json                      # All fonts from API
│   ├── raw_fonts.optimize.json             # Optimized (cleaned keys)
│   ├── top_20_fonts.json                   # Top 20 popular fonts
│   ├── top_20_fonts.optimize.json          # Optimized version
│   ├── vietnamese_fonts.json               # Vietnamese-supported fonts
│   └── vietnamese_fonts.optimize.json      # Optimized version
├── 2025-12-04/
│   └── ...
└── ...
```

**Note:** `.optimize.json` files have these keys removed:
- Root level: `version`, `lastModified`, `menu`
- Item level: `version`, `lastModified`, `menu`, `kind`
- Optional: `files` field (if `IS_IGNORE_FILES=1`)


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

## Project Structure

```
gg-font-curator/
├── app/
│   ├── __init__.py
│   ├── fetch_data.py          # Google Fonts API fetching logic
│   ├── filter_curate.py        # Font filtering and curation logic
│   └── optimize.py            # JSON optimization and key removal
├── main.py                     # Click CLI entry point
├── requirements.txt
├── README.md
└── LICENSE
```

## API Reference

### main.py (CLI Entry Point)

- **`python main.py fetch`**: Fetch fonts from Google Fonts API
- **`python main.py filter [OPTIONS]`**: Filter and curate fonts
  - `--input-file TEXT`: Custom path to raw fonts JSON
  - `--top-n INTEGER`: Number of top fonts (default: 20)
  - `--date TEXT`: Date folder in `yyyy-mm-dd` format (default: today)

### app/fetch_data.py

- **`fetch_fonts()`**: Fetches all fonts from Google Fonts API and saves to `output/yyyy-mm-dd/raw_fonts.json`

### app/filter_curate.py

- **`main(input_file=None, top_n=20, date_str=None)`**: Process fonts data and generate filtered outputs
  - `input_file`: Custom path to raw fonts JSON (default: auto-detected from date folder)
  - `top_n`: Number of top fonts to extract (default: 20)
  - `date_str`: Specific date folder in `yyyy-mm-dd` format (default: today's date)

- **`filter_top_n(data, n=20)`**: Extract top N fonts from data
- **`filter_vietnamese(data)`**: Extract Vietnamese-supported fonts
- **`load_fonts(input_file=None, date_str=None)`**: Load fonts from JSON file
- **`save_fonts(data, output_file, output_dir=None)`**: Save fonts to both JSON and optimized JSON files
- **`optimize_data(data)`**: Remove unnecessary keys from font data

### app/optimize.py

- **`optimize_fonts(raw_fonts_path)`**: Optimize raw fonts JSON by removing unnecessary keys and save as `.optimize.json`
  - Removes root-level keys: `version`, `lastModified`, `menu`
  - Removes item-level keys: `version`, `lastModified`, `menu`, `kind`
  - Optionally removes: `files` field (if `IS_IGNORE_FILES=1`)

## Environment Variables

Create a `.env` file in the project root:

```env
GOOGLE_FONTS_API_KEY=your_api_key_here
IS_IGNORE_FILES=1
```

- **`GOOGLE_FONTS_API_KEY`** (required): Your Google Fonts API key for API calls
- **`IS_IGNORE_FILES`** (optional, default: 0): Set to `1` to remove the large `files` field from optimized JSON files (reduces file size)

## Example Workflow

```bash
# Step 1: Fetch latest fonts from Google Fonts API
python main.py fetch

# Step 2: Filter and curate fonts (default: top 20, today's date)
python main.py filter

# Step 3: Or customize the filtering
python main.py filter --top-n 50 --date 2025-12-05
```

Check the `output/2025-12-05/` directory (today's date) for results.

## Format Code

### Setup Python Formatter

Install **Black** (optional but recommended for code formatting):

```bash
pip install black
```

### Format Code Files

Format all Python files in the project:

```bash
black .
```

Format a specific file:

```bash
black app/fetch_data.py
```

Format with specific line length:

```bash
black --line-length 100 .
```

### Code Style Guidelines

- **Line Length**: Maximum 88 characters (Black default) or 100 characters
- **Indentation**: 4 spaces (Python standard)
- **Naming Conventions**:
  - Functions and variables: `snake_case`
  - Classes: `PascalCase`
  - Constants: `UPPER_SNAKE_CASE`
- **Imports**: Group by standard library, third-party, and local imports
- **Docstrings**: Use triple quotes for all modules, functions, and classes

## Requirements

See `requirements.txt` for all dependencies:
- `requests` - HTTP library for API calls
- `python-dotenv` - Environment variable management
- `click` - Command-line interface creation kit

## License

MIT License - see LICENSE file for details

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
