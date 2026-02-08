import csv
import json
import os

def convert_csv_to_json(csv_path, json_path):
    if not os.path.exists(csv_path):
        print(f"Error: {csv_path} not found.")
        return

    data = []
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)

    with open(json_path, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Successfully converted to {json_path}")

# Example usage
# convert_csv_to_json('data.csv', 'data.json')
