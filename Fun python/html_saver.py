import requests
from bs4 import BeautifulSoup
import os

def save_webpage_as_html(url, output_directory):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Get the webpage content
        webpage_content = response.text
        
        # Parse the URL to create a valid filename
        filename = url.replace("https://", "").replace("http://", "").replace("/", "_") + ".html"
        
        # Ensure the output directory exists
        os.makedirs(output_directory, exist_ok=True)
        
        # Save the HTML content to a file
        file_path = os.path.join(output_directory, filename)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(webpage_content)
        
        print(f"Saved '{url}' as '{file_path}'")
        
    except requests.RequestException as e:
        print(f"Failed to retrieve {url}: {e}")

def save_multiple_webpages(urls, output_directory):
    for url in urls:
        save_webpage_as_html(url, output_directory)

# Example usage
if __name__ == "__main__":
    # List of URLs to save as HTML put URLs to clone in here
    urls = [
        
    ]
    
    # Directory where HTML files will be saved
    output_directory = "downloaded_html"
    
    # Save all the webpages
    save_multiple_webpages(urls, output_directory)