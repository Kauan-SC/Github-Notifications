import requests

url = "https://git-not.vercel.app/webhookcallback"

r = requests.post(url)
print(r.content)