import requests

url = "https://github-notifications-bot.vercel.app/webhookcallback"

r = requests.post(url)
print(r.content)