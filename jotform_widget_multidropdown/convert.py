import json

def parse_line(line):
    """Parse a line and return its indent level and the content."""
    stripped_line = line.strip()  # Use strip() to remove both leading and trailing whitespace
    indent_level = len(line) - len(stripped_line)
    return indent_level // 2, stripped_line

def convert_to_json(file_path):
    data = {}
    current_level1 = None
    current_level2 = None
    current_list = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            indent_level, content = parse_line(line)

            if indent_level == 0:
                # Level 1
                if current_level1 is not None:
                    if current_level2 is not None:
                        data[current_level1][current_level2] = current_list
                current_level1 = content
                data[current_level1] = {}  # Initialize the dictionary for level 1
                current_level2 = None
                current_list = []  # Reset the list for the next set of level 2 items
            elif indent_level == 1:
                # Level 2
                if current_level2 is not None:
                    data[current_level1][current_level2] = current_list
                current_level2 = content
                current_list = []  # Reset the list for the next set of level 3 items
            elif indent_level == 2:
                # Level 3
                current_list.append(content)

        # Handle the last entry
        if current_level1 is not None:
            if current_level2 is not None:
                data[current_level1][current_level2] = current_list

    return data

# Path to the input text file
input_file_path = 'confrarias.txt'

# Convert to JSON
result = convert_to_json(input_file_path)

# Print or save the result as JSON
output_file_path = 'output.json'
with open(output_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(result, json_file, indent=4, ensure_ascii=False)

print(f'JSON conversion complete. Output saved to {output_file_path}')
