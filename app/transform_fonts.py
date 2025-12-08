import json
from pathlib import Path


def transform_optimize_json(optimize_json_path):
    """
    Transform .optimize.json file format.
    
    Converts from:
    {
      "items": [
        {
          "family": "Roboto",
          "variants": [...],
          "subsets": [...],
          "category": "sans-serif"
        }
      ]
    }
    
    To:
    {
      "Roboto": {
        "weight": [...],  # variants without "italic"
        "subsets": [...],
        "category": "sans-serif"
      }
    }
    """
    input_path = Path(optimize_json_path)
    
    if not input_path.exists():
        raise FileNotFoundError(f"File not found: {input_path}")
    
    if not input_path.name.endswith(".optimize.json"):
        raise ValueError(f"File must end with .optimize.json: {input_path.name}")
    
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    items = data.get("items", [])
    transformed = {}
    
    for item in items:
        family = item.get("family")
        if not family:
            continue
        
        variants = item.get("variants", [])
        weight = [v for v in variants if "italic" not in v]
        
        family_key = family.replace(" ", "+")
        transformed[family_key] = {
            "family": family,
            "weight": weight,
            "subsets": item.get("subsets", []),
            "category": item.get("category")
        }
    
    output_filename = input_path.stem + ".family.json"
    output_path = input_path.parent / output_filename
    
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(transformed, f, indent=2, ensure_ascii=False)
    
    print(f"Transformed {len(transformed)} fonts to {output_path}")
