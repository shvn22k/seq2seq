import json

def fix_jsonl_with_emojis(input_file_path, output_file_path):
    """
    Fix a JSONL file by removing trailing commas and ensuring emojis are preserved.
    
    Args:
        input_file_path (str): Path to the input JSONL file
        output_file_path (str): Path to save the fixed JSONL file
    """
    fixed_data = []
    
    # Read the input file
    with open(input_file_path, 'r', encoding='utf-8') as file:
        line_number = 0
        for line in file:
            line_number += 1
            line = line.strip()
            
            # Skip empty lines
            if not line:
                continue
            
            # Remove trailing comma if it exists
            if line.endswith(','):
                line = line[:-1]
            
            # Validate JSON
            try:
                data = json.loads(line)
                fixed_data.append(data)
            except json.JSONDecodeError as e:
                print(f"Error in line {line_number}: {e}")
                print(f"Problematic line: {line}")
    
    # Write the fixed data with ensure_ascii=False to preserve emojis
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for item in fixed_data:
            file.write(json.dumps(item, ensure_ascii=False) + '\n')
    
    print(f"Fixed file saved to {output_file_path}")
    print(f"Processed {len(fixed_data)} valid JSON objects")

if __name__ == "__main__":
    # Replace these with your actual file paths
    input_file = r"brainrot-dataset\data\train.jsonl"
    output_file = r"brainrot-dataset\data\train_cleaned.jsonl"
    
    fix_jsonl_with_emojis(input_file, output_file)