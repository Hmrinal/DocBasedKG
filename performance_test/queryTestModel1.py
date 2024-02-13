# from pymongo import MongoClient
# import time

# # Constants
# DATABASE_NAME = "29Dec_propertiesModel1"  # The database name
# COLLECTION_NAME = "rdftojson"  # The collection to query
# QUERY = {
#     "predicate": "http://www.semanticweb.org/mrinaltyagi/ontologies/29Dec_DataProperties#hasBAT_NR",
#     "object": "48"
# }
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

# # Running the query for 2000 iterations and calculating average time
# avg_duration = average_query_time(QUERY, ITERATIONS)
# print(f"Average query time over {ITERATIONS} iterations: {avg_duration:.4f} seconds.")
from pymongo import MongoClient
import time

# Constants
DATABASE_NAME = "29Dec_propertiesModel1"  # The database name
COLLECTION_NAME = "rdftojson"  # The collection to query
QUERY = {
    "$or": [
        {"$and": [
            {"predicate": "http://www.semanticweb.org/mrinaltyagi/ontologies/29Dec_DataProperties#hasBAT_NR", "object": "48"}
        ]},
        {"$and": [
            {"predicate": "http://www.semanticweb.org/mrinaltyagi/ontologies/29Dec_DataProperties#hasPrüfmusternummer", "object": "500"}
        ]}
    ]
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

def average_query_time(query, iterations):
    """Function to calculate the average query time over a number of iterations."""
    total_time = 0
    for _ in range(iterations):
        duration = run_query(query)
        total_time += duration
    return total_time / iterations

# Running the query for 100,000 iterations and calculating average time
avg_duration = average_query_time(QUERY, ITERATIONS)
print(f"Average query time over {ITERATIONS} iterations: {avg_duration:.4f} seconds.")
