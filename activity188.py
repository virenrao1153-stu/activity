import requests

url = "https://jsonplaceholder.typicode.com/posts"

for i in range(5):
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"Request {i+1} successful")
        print(f"First post title: {data[0]['title']}")
        print()
    else:
        print("Request failed")