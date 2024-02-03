import json
from rdflib import Graph, URIRef
from pymongo import MongoClient

# Function to convert RDF to a list of JSON objects
def rdf_to_json(rdf_file_path, rdf_format):
    g = Graph()
    g.parse(rdf_file_path, format=rdf_format)

    json_data = []
    for subj, pred, obj in g:
        # Simplifying the assumption: converting each triple into a JSON object
        json_obj = {
            'subject': str(subj),
            'predicate': str(pred),
            'object': str(obj) if not isinstance(obj, URIRef) else str(obj)
        }
        json_data.append(json_obj)

    return json_data

# Connect to MongoDB
client = MongoClient('localhost', 27017)  # Update with your MongoDB URI if needed
db = client['29Dec_propertiesModel1'] # Replace with your database name
collection = db['rdftojson']  # Replace with your collection name

# Convert RDF to JSON
rdf_file_path = '/Users/mrinaltyagi/University/Thesis/Ontology/29Dec_DataProperties.rdf'  # Update with your RDF file path
rdf_format = 'xml'  # Update with your RDF file format ('xml', 'turtle', 'nt', etc.)
json_data = rdf_to_json(rdf_file_path, rdf_format)

# Importing the JSON data into MongoDB
collection.insert_many(json_data)

print("Data imported successfully into MongoDB.")
