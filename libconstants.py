import os

INPUT = "alpaca_data.json"
OUTPUT = "haystack-data"
SEP = " *** "
HAYSTACK_IP = os.environ.get("AZ_CACHE_IP", '10.1.0.4')
