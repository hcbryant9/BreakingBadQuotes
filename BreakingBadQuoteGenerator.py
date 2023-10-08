import requests

def get_quote():
    url = "https://api.breakingbadquotes.xyz/v1/quotes"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()[0]
        quote = data["quote"]
        author = data["author"]
        return f'"{quote}" - {author}'
    else:
        return None
    
def print_quote():
    quote = get_quote()
    if quote:
        print("Daily quote:")
        print(quote)
    else:
        print("failed to fetch quote")

if __name__ == "__main__":
    print_quote()