# from pymongo import MongoClient
# import time

# # Constants
# DATABASE_NAME = "29Dec_propertiesModel2"  # The database name
# COLLECTION_NAME = "rdftojsonviaJena"  # The collection to query
# AGGREGATION_PIPELINE = [
#     {"$unwind": "$@graph"},
#     {"$match": {
#         "@graph.@type": "Dec_DataProperties:EntityMeasurement",
#         "@graph.Dec_DataProperties:hasBAT_NR": {"@value": "48", "@type": "xsd:integer"}
#     }},
#     {"$project": {"_id": 0, "instance": "$@graph.@id"}}
# ]
# ITERATIONS = 2000

# # MongoDB Client Setup
# client = MongoClient('localhost', 27017)
# db = client[DATABASE_NAME]
# collection = db[COLLECTION_NAME]

# def run_aggregation(pipeline):
#     """Function to execute an aggregation pipeline and measure the execution time."""
#     start_time = time.time()
#     results = collection.aggregate(pipeline)
#     results = list(results)  # Force pipeline execution
#     end_time = time.time()
#     return end_time - start_time

# def average_aggregation_time(pipeline, iterations):
#     """Function to calculate the average time of an aggregation pipeline over several iterations."""
#     total_time = 0
#     for _ in range(iterations):
#         duration = run_aggregation(pipeline)
#         total_time += duration
#     return total_time / iterations

# # Running the aggregation query for 2000 iterations and calculating average time
# avg_duration = average_aggregation_time(AGGREGATION_PIPELINE, ITERATIONS)
# print(f"Average aggregation time over {ITERATIONS} iterations: {avg_duration:.4f} seconds.")
from pymongo import MongoClient
import time

# Constants
DATABASE_NAME = "29Dec_propertiesModel2"  # The database name
COLLECTION_NAME = "rdftojsonviaJena"  # The collection to query
AGGREGATION_PIPELINE = [
    {
        "$unwind": "$@graph"
    },
    {
        "$facet": {
            "EntityMeasurement": [
                {
                    "$match": {
                        "@graph.@type": "Dec_DataProperties:EntityMeasurement",
                        "@graph.Dec_DataProperties:hasBAT_NR": {"@value": "48", "@type": "xsd:integer"}
                    }
                }
            ],
            "Metadata": [
                {
                    "$match": {
                        "@graph.@type": "Dec_DataProperties:Metadata",
                        "@graph.Dec_DataProperties:hasPrüfmusternummer": {"@value": "500", "@type": "xsd:integer"}
                    }
                }
            ]
        }
    },
    {
        "$project": {
            "combinedResults": {"$setUnion": ["$EntityMeasurement", "$Metadata"]}
        }
    },
    {
        "$unwind": "$combinedResults"
    },
    {
        "$replaceRoot": {"newRoot": "$combinedResults"}
    },
    {
        "$project": {"_id": 0, "instance": "$@graph.@id"}
    }
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

def average_aggregation_time(pipeline, iterations):
    """Function to calculate the average time of an aggregation pipeline over several iterations."""
    total_time = 0
    for _ in range(iterations):
        duration = run_aggregation(pipeline)
        total_time += duration
    return total_time / iterations

# Running the aggregation pipeline for 100,000 iterations and calculating average time
avg_duration = average_aggregation_time(AGGREGATION_PIPELINE, ITERATIONS)
print(f"Average aggregation time over {ITERATIONS} iterations: {avg_duration:.4f} seconds.")
