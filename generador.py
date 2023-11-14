import bz2
import json
import os

def extract_lines_with_year(bz2_file_path, start_year, end_year):
    matching_lines = 0
    with bz2.BZ2File(bz2_file_path, 'r') as bz2_file:
        for line in bz2_file:
            try:
                data = json.loads(line)
                created_at_year = int(data.get("created_at", "").split()[-1])
                if start_year <= created_at_year <= end_year:
                    matching_lines += 1
            except json.JSONDecodeError:
                # Handle the case where a line is not a valid JSON
                continue
            except (KeyError, IndexError, ValueError):
                # Handle other possible errors while extracting the year
                continue
    return matching_lines

# Example usage
start_year = 2016
end_year = 2020
bz2_file_path = "C:\\Users\\Carlos\\Desktop\\Career\\Career\\Algoritmos\\Python\\EC2\\06\\00\\30.json.bz2"
matching_lines = extract_lines_with_year(bz2_file_path, start_year, end_year)
print(f"Number of matching lines: {matching_lines}")
