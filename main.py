import requests

api_key = "4375011c7ff2431893c76dcb04486983"
url = ("https://newsapi.org/v2/everything?q=tesla&from=2025-04-23&sortBy=publishedAt&apiKey"
       "=4375011c7ff2431893c76dcb04486983")

# make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the articles titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])




