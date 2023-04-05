import requests
from bs4 import BeautifulSoup

#product_code =input("podaj kod produktu: ")
product_code=96693065
url=f"https://www.ceneo.pl/{product_code}#tab=reviews_scroll"
response = requests.get(url)
page_dom = BeautifulSoup(response.text, "html.parser")
opinions = page_dom.select("div.js_product.review")
all__opinions = []
for opionion in opinions:
    single_opinion = {
        "opinion_id": opionion["data-entry-id"],
        "author":opionion.select_one("span.user__post-name").text.strip(),
        "recomendation":opionion.select_one("span.user-post_author.recomendation>em").text.strip(),
        "rating":opionion.select_one("span.user-post__score-count").text.strip(),
        "verified":opionion.select_one("div.review-pz").text.strip(),
        "post_date":opionion.select_one("span.user-post__published>time:nth-child(1)")["datetime"].text.strip(),
        "purchase_date":opionion.select_one("span.user-post__published>time:nth-child(2)")["datetime"].text.strip(),
        "vote_up":opionion.select_one("button.vote-yes")["data-total-vote"].strip(),
        "vote_down":opionion.select_one("button.vote-no")["data-total-vote"].strip(),
        "content":opionion.select_one("div.user-post__text").text.strip(),
        "pros":[pros.text.strip() for pros in opionion.select_one("div.review-feature__titles—positives~div.review-feature-item")],
        "cons":[cons.text.strip() for cons in opionion.select_one("div.review-feature__titles—negatives~div.review-feature-item")]
    }
all__opinions.append(single_opinion)

print(all__opinions)

