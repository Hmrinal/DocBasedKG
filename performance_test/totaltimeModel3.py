from pymongo import MongoClient
import time

# Constants
DATABASE_NAME = "29Dec_propertiesModel3"  # Replace with your actual database name
COLLECTION_NAME = "rdftojsonSegmentDoc"  # The collection to query
QUERY = {"data_properties.hasBAT_NR": "48"}
PROJECTION = {"_id": 1}
ITERATIONS = 100000

# MongoDB Client Setup
client = MongoClient('localhost', 27017)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

def run_query(query, projection):
    """Function to execute a query with a projection and measure the execution time."""
    start_time = time.time()
    results = collection.find(query, projection)
    results = list(results)  # Force query execution to ensure timing includes full query processing
    end_time = time.time()
    return end_time - start_time

def total_query_time(query, projection, iterations):
    """Function to calculate the total time taken for a specific number of iterations."""
    total_time = 0
    for _ in range(iterations):
        duration = run_query(query, projection)
        total_time += duration
    return total_time

# Calculating the total time for all iterations
total_duration = total_query_time(QUERY, PROJECTION, ITERATIONS)
print(f"Total time for {ITERATIONS} iterations: {total_duration:.4f} seconds.")
