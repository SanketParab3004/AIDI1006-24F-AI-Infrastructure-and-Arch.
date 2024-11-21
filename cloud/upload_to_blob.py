from azure.storage.blob import BlobServiceClient
import os

# Azure Storage connection string and container name
STORAGE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=aidi1006;AccountKey=siqB6kFfkMt0u3CYfhxDmVy4lvP/pkwjIIKveyTMGYHnJZn52DISwb5Zsslt9s30ySg0y0fhTKqw+AStf6nVJA==;EndpointSuffix=core.windows.net"
CONTAINER_NAME = "sentiment-analysis-data"

def upload_to_blob(local_file_path, blob_name):
    try:
        # Check if the local file exists
        if not os.path.exists(local_file_path):
            print(f"Error: The file {local_file_path} does not exist.")
            return
        
        # Connect to Azure Blob Service
        blob_service_client = BlobServiceClient.from_connection_string(STORAGE_CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=blob_name)
        
        # Upload file
        with open(local_file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)
            print(f"Uploaded {local_file_path} to Azure Blob Storage as {blob_name}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Upload sentiment results
    local_files = [
        ("../data/results/vader_vader_sentiment_results.csv", "results/vader_sentiment.csv"),
        ("../data/results/textblob_vader_sentiment_results.csv", "results/textblob_sentiment.csv"),
    ]

    for local_file, blob_name in local_files:
        upload_to_blob(local_file, blob_name)
