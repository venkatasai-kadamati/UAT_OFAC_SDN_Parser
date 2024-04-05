import requests
import os
from requests.packages.urllib3.exceptions import InsecureRequestWarning


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# URL of the sdn_advanced.xml file
url = "https://www.treasury.gov/ofac/downloads/sanctions/1.0/sdn_advanced.xml"

response = requests.get(url, verify=False)
file_path = "source/sdn_advanced.xml"
# Check if the request was successful
if response.status_code == 200:
    # Write the content of the response to a file
    # Check if the file exists
    if os.path.exists(file_path):
        # Delete the file
        os.remove(file_path)
        print(f"{file_path} has been deleted.")
    else:
        print(f"The file {file_path} does not exist.")

    with open("source/sdn_advanced.xml", "wb") as file:
        file.write(response.content)
    print("Download successful.")
else:
    print("Failed to download the file.")
