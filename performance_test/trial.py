# from pymongo import MongoClient
# import time

# # Constants
# DATABASE_NAME = "29Dec_propertiesModel3"  # The actual database name
# COLLECTION_NAME = "rdftojsonSegmentDoc"  # The collection to query
# QUERY = {"data_properties.Dec_DataProperties:hasBAT_NR": "48"}
# ITERATIONS = 2000

# # MongoDB Client Setup
# client = MongoClient('localhost', 27017)
# db = client[DATABASE_NAME]
# collection = db[COLLECTION_NAME]

# def run_query(query):
#     """Function to execute a query and measure the execution time."""
#     start_time = time.time()
#     results = collection.find(query)
#     results = list(results)  # Force query execution
#     end_time = time.time()
#     return end_time - start_time

# def average_query_time(query, iterations):
#     """Function to calculate the average query time over a number of iterations."""
#     total_time = 0
#     for _ in range(iterations):
#         duration = run_query(query)
#         total_time += duration
#     return total_time / iterations

# # Running the query for 100 iterations and calculating average time
# avg_duration = average_query_time(QUERY, ITERATIONS)
# print(f"Average query time over {ITERATIONS} iterations: {avg_duration:.4f} seconds.")
from pymongo import MongoClient
import time

# Constants
DATABASE_NAME = "29Dec_propertiesModel3"  # the actual database name
COLLECTION_NAME = "rdftojsonSegmentDoc"  # The collection to query
QUERY = {
    "$or": [
        {
            "types": "Dec_DataProperties:EntityMeasurement",
            "data_properties.Dec_DataProperties:hasBAT_NR": "48"
        },
        {
            "types": "Dec_DataProperties:Metadata",
            "data_properties.Dec_DataProperties:hasPrüfmusternummer": "500"
        }
    ]
}
PROJECTION = {"_id": 1}
ITERATIONS = 100

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

def average_query_time(query, projection, iterations):
    """Function to calculate the average query time over a number of iterations."""
    total_time = 0
    for _ in range(iterations):
        duration = run_query(query, projection)
        total_time += duration
    return total_time / iterations

# Running the query for 100 iterations and calculating average time
avg_duration = average_query_time(QUERY, PROJECTION, ITERATIONS)
print(f"Average query time over {ITERATIONS} iterations: {avg_duration:.4f} seconds.")
