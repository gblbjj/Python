import requests 


r = requests.get("https://www.google.com.br")
x = r.status_code
print(x)