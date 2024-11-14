from pathlib import Path
import json
import os

# Get the base directory (directory where this file resides)
BASE_DIR = Path(__file__).parent.parent
SCRAP_DIR = BASE_DIR / 'scrap'
CACHE_FILE = SCRAP_DIR / 'config_cache.json'  # Path to the cache file
CONFIG_FILE = SCRAP_DIR / 'config.json'
DATA_DIR = BASE_DIR / 'data'


def load_config():
    with open(CONFIG_FILE, 'r') as config_file:
        return json.load(config_file)


def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r') as cache_file:
            return json.load(cache_file)
    return None


def save_cache(selection):
    with open(CACHE_FILE, 'w') as cache_file:
        json.dump(selection, cache_file)


def choose_source(config):
    print("Please choose a source:")
    for i, source in enumerate(config['sources']):
        print(f"{i + 1}. {source['url']} -> {source['csv']}")
    choice = int(input("Enter the number of your choice: ")) - 1
    return config['sources'][choice]
