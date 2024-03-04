from pymongo import MongoClient
import time
import psutil

# Hardware Information Gathering
def print_hardware_info():
    print("CPU Information:")
    cpu_logical = psutil.cpu_count()
    cpu_physical = psutil.cpu_count(logical=False)
    cpu_freq = psutil.cpu_freq().current if psutil.cpu_freq() else "Unknown"
    cpu_usage = psutil.cpu_percent(interval=1)

    print(f" Logical CPUs: {cpu_logical}")
    print(f" Physical Cores: {cpu_physical}")
    print(f" CPU Frequency: {cpu_freq}MHz")
    print(f" CPU Usage: {cpu_usage}%")

    print("\nMemory Information:")
    memory = psutil.virtual_memory()
    total_memory = round(memory.total / (1024 ** 3), 2)  # Convert to GB
    used_memory = round(memory.used / (1024 ** 3), 2)
    available_memory = round(memory.available / (1024 ** 3), 2)

    print(f" Total Memory: {total_memory}GB")
    print(f" Used Memory: {used_memory}GB")
    print(f" Available Memory: {available_memory}GB")

    # Process and Thread Information
    print("\nProcess and Thread Information:")
    process_count = len(psutil.pids())  # Total number of processes
    thread_count = psutil.Process().num_threads()  # Number of threads in the current process

    print(f" Total number of processes: {process_count}")
    print(f" Number of threads in current process: {thread_count}")

    # Network Traffic Information
    net_io = psutil.net_io_counters()
    bytes_sent = round(net_io.bytes_sent / (1024 ** 2), 2)  # Convert to MB
    bytes_recv = round(net_io.bytes_recv / (1024 ** 2), 2)  # Convert to MB

    print("\nNetwork Traffic Information:")
    print(f" Data Sent: {bytes_sent}MB")
    print(f" Data Received: {bytes_recv}MB")

# Constants
DATABASE_NAME = "29Dec_propertiesModel3"  # the database name
COLLECTION_NAME = "rdftojsonSegmentDoc"  # The collection to query
QUERY = {"data_properties.hasBAT_NR": "48"} #Set required query for models
PROJECTION = {"_id": 1}
ITERATIONS = 100000  # Set to match the number of iterations you want to test

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
    """Function to calculate the total time taken for a specified number of iterations of a query."""
    total_time = 0
    for _ in range(iterations):
        duration = run_query(query, projection)
        total_time += duration
    return total_time

# Print hardware information before running the performance tests
print_hardware_info()

# Calculating the total time for all iterations
total_duration = total_query_time(QUERY, PROJECTION, ITERATIONS)
print(f"Total time for {ITERATIONS} iterations: {total_duration:.4f} seconds.")
