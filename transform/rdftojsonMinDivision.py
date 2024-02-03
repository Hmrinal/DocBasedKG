from rdflib import Graph, RDF, OWL, RDFS, URIRef, Literal, BNode
import json
import os
import re

# Initialize a graph and parse the RDF file
g = Graph()
g.parse("/Users/mrinaltyagi/University/Thesis/Ontology/29Dec_DataProperties.rdf", format="xml")

# Containers for different elements
classes = set()
data_properties = set()
object_properties = set()
instances = {}
restrictions = {}

# Define the namespaces of your ontology to filter relevant object properties
ontology_namespace = "http://www.semanticweb.org/mrinaltyagi/ontologies/29Dec_DataProperties#"

# Helper functions
def serialize_uri(uri):
    if isinstance(uri, URIRef):
        return uri.n3(g.namespace_manager)
    return str(uri)

def sanitize_filename(uri):
    return re.sub(r'[^\w\-_\.]', '_', uri)

def save_to_json(filename, data, directory="output_directory"):
    os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(directory, sanitize_filename(filename))
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

# Process the graph
for s, p, o in g:
    if p == RDF.type and (o == OWL.Class or o == RDFS.Class):
        classes.add(s)
    elif p == RDF.type and isinstance(s, URIRef):
        instances.setdefault(s, {'types': [], 'data_properties': {}, 'object_properties': {}})
        instances[s]['types'].append(serialize_uri(o))
    elif isinstance(p, URIRef) and isinstance(o, Literal):
        data_properties.add(p)
        if s in instances:
            instances[s]['data_properties'].setdefault(serialize_uri(p), []).append(serialize_uri(o))
    elif isinstance(p, URIRef) and isinstance(o, URIRef) and p.startswith(ontology_namespace):
        object_properties.add(p)
        if s in instances:
            instances[s]['object_properties'].setdefault(serialize_uri(p), []).append(serialize_uri(o))

# Save classes and properties
save_to_json("classes.json", {"all_classes": list(classes)})
save_to_json("data_properties.json", {"all_data_properties": list(data_properties)})
save_to_json("object_properties.json", {"all_object_properties": list(object_properties)})

# Process and save restrictions
for s, p, o in g.triples((None, None, OWL.Restriction)):
    restriction_id = serialize_uri(s)
    restrictions[restriction_id] = {}
    for restriction_property, value in g.predicate_objects(subject=s):
        if restriction_property not in (RDF.type, OWL.onProperty):
            restrictions[restriction_id][serialize_uri(restriction_property)] = serialize_uri(value)
save_to_json("restrictions.json", {"all_restrictions": restrictions})

# Save instances
for instance_uri, details in instances.items():
    save_to_json(f"instance_{sanitize_filename(instance_uri)}.json", details)

print("RDF data has been separated and saved into JSON files.")
