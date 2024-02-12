from pymongo import MongoClient
import time

# Constants
DATABASE_NAME = "29Dec_propertiesModel1"  # the database name
COLLECTION_NAME = "rdftojson"  # The collection to query
QUERY = {
    "predicate": "http://www.semanticweb.org/mrinaltyagi/ontologies/29Dec_DataProperties#hasBAT_NR",
    "object": "48"
}
ITERATIONS = 100000

# MongoDB Client Setup
client = MongoClient('localhost', 27017)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

def run_query(query):
    """Function to execute a query and measure the execution time."""
    start_time = time.time()
    results = collection.find(query)
    results = list(results)  # Force query execution to ensure timing includes full query processing
    end_time = time.time()
    return end_time - start_time

def total_query_time(query, iterations):
    """Function to calculate the total time taken for a specified number of iterations of a query."""
    total_time = 0
    for _ in range(iterations):
        duration = run_query(query)
        total_time += duration
    return total_time

# Calculating the total time for all iterations
total_duration = total_query_time(QUERY, ITERATIONS)
print(f"Total time for {ITERATIONS} iterations: {total_duration:.4f} seconds.")
