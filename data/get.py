import os
import requests
import json
from multiprocessing import Pool

def download_file(data):
    # Get the media_url
    media_url = data["media_url"]
    
    # Extract the filename from the data
    filename = media_url.split('/')[-1]
    
    # Download the file
    response = requests.get(media_url)
    
    # Save the file in the "imgs" folder
    with open(os.path.join("imgs", filename), "wb") as img_file:
        img_file.write(response.content)

if __name__ == "__main__":
    # Create the "imgs" folder if it doesn't exist
    if not os.path.exists("imgs"):
        os.makedirs("imgs")

    # Read the JSONL file
    with open("vibe-eval.v1.jsonl", "r") as file:
        data_list = [json.loads(line) for line in file]

    # Create a pool of worker processes
    pool = Pool()

    # Use the pool to download files in parallel
    pool.map(download_file, data_list)

    # Close the pool
    pool.close()
    pool.join()

    print("All media files downloaded and saved in the 'imgs' folder.")