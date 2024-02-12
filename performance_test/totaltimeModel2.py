from pymongo import MongoClient
import time

# Constants
DATABASE_NAME = "29Dec_propertiesModel2"  # The actual database name
COLLECTION_NAME = "rdftojsonviaJena"  # The collection to query
AGGREGATION_PIPELINE = [
    {"$unwind": "$@graph"},
    {"$match": {
        "@graph.@type": "EntityMeasurement",
        "@graph.hasBAT_NR": {"@value": "48", "@type": "xsd:integer"}
    }},
    {"$project": {"_id": 0, "instance": "$@graph.@id"}}
]
ITERATIONS = 100000

# MongoDB Client Setup
client = MongoClient('localhost', 27017)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

def run_aggregation(pipeline):
    """Function to execute an aggregation pipeline and measure the execution time."""
    start_time = time.time()
    results = collection.aggregate(pipeline)
    results = list(results)  # Force pipeline execution to ensure timing includes full query processing
    end_time = time.time()
    return end_time - start_time

def total_aggregation_time(pipeline, iterations):
    """Function to calculate the total time taken for a specific number of iterations of an aggregation pipeline."""
    total_time = 0
    for _ in range(iterations):
        duration = run_aggregation(pipeline)
        total_time += duration
    return total_time

# Calculating the total time for all iterations
total_duration = total_aggregation_time(AGGREGATION_PIPELINE, ITERATIONS)
print(f"Total time for {ITERATIONS} iterations: {total_duration:.4f} seconds.")
