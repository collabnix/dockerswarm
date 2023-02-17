import requests

# Set the API endpoint and search query
url = "https://api.github.com/search/repositories"
query = "docker swarm"

# Set the query parameters, including the search query and API token
params = {"q": query, "access_token": "<your_access_token>"}

# Send the GET request to the API endpoint
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Get the list of repositories from the response JSON
    repos = response.json()["items"]

    # Print the name and URL of each repository
    for repo in repos:
        print(f"{repo['full_name']}: {repo['html_url']}")
else:
    # Print an error message if the request was not successful
    print(f"Error {response.status_code}: {response.text}")
