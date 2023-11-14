import bz2
import json

def extract_lines_with_year(bz2_file_path, start_year, end_year, output_file_path):
    matching_lines = []
    with bz2.BZ2File(bz2_file_path, 'r') as bz2_file:
        for line in bz2_file:
            try:
                # Decode the line as UTF-8
                line_str = line.decode('utf-8')
                
                data = json.loads(line_str)
                created_at_year = int(data.get("created_at", "").split()[-1])
                if start_year <= created_at_year <= end_year:
                    matching_lines.append(line_str.strip())
            except json.JSONDecodeError:
                # Handle the case where a line is not a valid JSON
                continue
            except (KeyError, IndexError, ValueError):
                # Handle other possible errors while extracting the year
                continue

    # Write matching lines to the output file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for matched_line in matching_lines:
            output_file.write(matched_line + '\n')

# Example usage
start_year = 2016
end_year = 2020
bz2_file_path = "C:\Users\Carlos\Desktop\Career\Career\Algoritmos\Python\EC2\06\00\30.json.bz2"
output_file_path = "C:\Users\Carlos\Desktop\matched_lines.txt"

extract_lines_with_year(bz2_file_path, start_year, end_year, output_file_path)
