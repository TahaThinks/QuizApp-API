import requests

request = requests.get(url="https://opentdb.com/api.php?amount=10&category=18&type=boolean")
question_data = request.json()["results"]
