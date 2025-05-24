import requests
from send_email import send_email

api_key = "4375011c7ff2431893c76dcb04486983"
topic = "tesla"
url = (f"https://newsapi.org/v2/everything?q={topic}&from=2025-04-24&"
       "sortBy=publishedAt&apiKey=4375011c7ff2431893c76dcb04486983&language=en")

# make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the articles titles and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = (body + article["title"] + "\n" + article["description"] +
                "\n" + article["url"] + 2*"\n")


message = f"""\
Subject: Today's news
{body}
"""
message = message.encode("UTF-8")
send_email(message)


