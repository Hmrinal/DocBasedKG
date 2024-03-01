import json
from collections import defaultdict, Counter

# Define the paths to your JSON files
json_files = [
    '/Users/mrinaltyagi/University/Thesis/CodeFile/PythonFiles/analyzeFile/29Dec_propertiesModel1.rdftojson.json',
    '/Users/mrinaltyagi/University/Thesis/CodeFile/PythonFiles/analyzeFile/29Dec_propertiesModel2.rdftojsonviaJena.json',
    '/Users/mrinaltyagi/University/Thesis/CodeFile/PythonFiles/analyzeFile/29Dec_propertiesModel3.rdftojsonSegmentDoc.json'
]

def analyze_json(json_data):
    unique_keys = set()
    value_types = Counter()
    depth_counter = Counter()
    common_keys = defaultdict(int)

    def recursive_analysis(data, depth=1):
        if isinstance(data, dict):
            depth_counter[depth] += 1
            for key, value in data.items():
                unique_keys.add(key)
                common_keys[key] += 1
                value_types[type(value).__name__] += 1
                recursive_analysis(value, depth + 1)
        elif isinstance(data, list):
            value_types['list'] += 1
            for item in data:
                recursive_analysis(item, depth)
        else:
            value_types[type(data).__name__] += 1

    recursive_analysis(json_data)

    truly_common_keys = {k: v for k, v in common_keys.items() if v > 1}
    context_presence = '@context' in unique_keys
    type_presence = '@type' in unique_keys

    return {
        'total_unique_keys': len(unique_keys),
        'value_types': dict(value_types),
        'max_depth': max(depth_counter),
        'common_keys': truly_common_keys,
        '@context_presence': context_presence,
        '@type_presence': type_presence,
    }

# Function to load a JSON file and return its data
def load_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Analyze each file and print the results
for file_path in json_files:
    json_data = load_json_file(file_path)
    analysis_result = analyze_json(json_data)
    print(f"Analysis for {file_path.split('/')[-1]}:")
    print(json.dumps(analysis_result, indent=4))
    print("\n")