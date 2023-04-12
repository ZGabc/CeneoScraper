import requests
import json
from bs4 import BeautifulSoup

def extract_tag(ancestor, selector, attribute=None, return_list=False):
    try:
        if return_list:
            return [tag.text.strip() for tag in ancestor.select(selector)]
        if not selector and attribute:
            return ancestor[attribute]
        if attribute :
            return ancestor.select_one(selector)[attribute].strip()
        return ancestor.select_one(selector).text.strip()
    except (AttributeError, TypeError):
        return None 

#product_code =input("podaj kod produktu: ")
product_code=96693065
url=f"https://www.ceneo.pl/{product_code}#tab=reviews"
response = requests.get(url)
page_dom = BeautifulSoup(response.text, "html.parser")
opinions = page_dom.select("div.js_product-review")
all_opinions = []
for opionion in opinions:
    single_opinion = {
        "opinion_id": extract_tag(opionion, None, "data-entry-id"),
        "author": extract_tag(opionion, "span.user__post-name"),
        "recomendation":extract_tag(opionion,"span.user-post_author.recomendation>em"),
        "rating":extract_tag(opionion,"span.user-post__score-count"),
        "verified":extract_tag(opionion,"div.review-pz"),
        "post_date":extract_tag(opionion,"span.user-post__published>time:nth-child(1)","datetime"),
        "purchase_date":extract_tag(opionion,"span.user-post__published>time:nth-child(2)","datetime"),
        "vote_up":extract_tag(opionion,"button.vote-yes","data-total-vote"),
        "vote_down":extract_tag(opionion,"button.vote-no","data-total-vote"),
        "content":extract_tag(opionion,"div.user-post__text"),
        "pros":extract_tag(opionion,"div.review-feature__titles—positives~div.review-feature-item",None, True),
        "cons":extract_tag(opionion,"div.review-feature__titles—negatives~div.review-feature-item",None, True)
    }
    all_opinions.append(single_opinion)
with open("./opinions/{product_code}.json", "w", encoding="UTF-8") as jf:
    json.dump(all_opinions, jf, indent=4, ensure_ascii=False)
