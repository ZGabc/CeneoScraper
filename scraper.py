import requests
from bs4 import BeautifulSoup

#product_code =input("podaj kod produktu: ")
product_code=96693065
url=f"https://www.ceneo.pl/{product_code}#tab=reviews_scroll"
response = requests.get(url)
page_dom = BeautifulSoup(response.text, "html.parser")

print(page_dom.pretify())

