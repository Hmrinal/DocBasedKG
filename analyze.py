# Let's load the JSON data from both files to analyze and compare their structures and contents.
import json

# Load the direct RDF to JSON conversion file
with open("/Users/mrinaltyagi/University/Thesis/Ontology/27Dec_Output.json", 'r') as file:
    rdf_json_data = json.load(file)

# Load the RDF to JSON-LD to JSON conversion file
with open('/Users/mrinaltyagi/University/Thesis/Ontology/27dec_ldoutput.json', 'r') as file:
    jsonld_json_data = json.load(file)

# Analyze the structure and content of the direct RDF to JSON conversion file
rdf_json_structure = {
    "total_keys": len(rdf_json_data.keys()),
    "sample_keys": list(rdf_json_data.keys())[:5],  # Get a sample of keys
    "sample_values": {k: rdf_json_data[k] for k in list(rdf_json_data.keys())[:5]}  # Sample of content
}

# Analyze the structure and content of the RDF to JSON-LD to JSON conversion file
jsonld_json_structure = {
    "total_elements": len(jsonld_json_data),
    "sample_elements": jsonld_json_data[:5]  # Get a sample of elements
}

# Display the results in the console
print("Direct RDF to JSON Conversion Structure:")
print(json.dumps(rdf_json_structure, indent=4))

print("\nRDF to JSON-LD to JSON Conversion Structure:")
print(json.dumps(jsonld_json_structure, indent=4))
