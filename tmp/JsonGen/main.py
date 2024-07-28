import json

def extract_patterns(data, parent_key='', patterns=None):
    if patterns is None:
        patterns = []

    if isinstance(data, dict):
        current_pattern = f"{parent_key}:object" if parent_key else "root:object"
        patterns.append(current_pattern)
        for key, value in data.items():
            extract_patterns(value, f"{parent_key}.{key}" if parent_key else key, patterns)
    elif isinstance(data, list):
        current_pattern = f"{parent_key}:array"
        patterns.append(current_pattern)
        for item in data:
            item_key = f"{parent_key}_items"
            extract_patterns(item, item_key, patterns)
    else:
        current_pattern = f"{parent_key}:{type(data).__name__}"
        patterns.append(current_pattern)
    
    return patterns

# Read JSON from file
with open('input.json', 'r') as f:
    data = json.load(f)

# Extract patterns
patterns = extract_patterns(data)

# Remove duplicates while preserving order
seen = set()
unique_patterns = []
for pattern in patterns:
    if pattern not in seen:
        seen.add(pattern)
        unique_patterns.append(pattern)

# Write patterns to output file
with open('output.txt', 'w') as f:
    for pattern in unique_patterns:
        f.write(pattern + '\n')
