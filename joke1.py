import requests

def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)

    if response.status_code == 200:
        joke = response.json()
        print(f"Here's a joke for you:\n")
        print(f"{joke['setup']}")
        print(f"{joke['punchline']}")
    else:
        print("Failed to retrieve a joke. Please try again later.")

if __name__ == "__main__":
    get_joke()
