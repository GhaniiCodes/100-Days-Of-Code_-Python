import requests

category = input("Enter the category of news you are intersted in : ")
url = f"https://www.nytimes.com/international/section/{category}"
 
r = requests.get(url)

print(r.text)

