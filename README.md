# CeneoScraper

## Selektory składowych opinii w Ceneo.pl

| składowa | nazwa | selektor |
| --- | --- | --- |
| identyfikator opinii | opinion\_id | [data-entry-id] |
| autor | author | span.user-post\_\_author-name |
| rekomendacja | recommendation | span.user-post\_\_author-recomendation \> em |
| liczba gwiazdek | rating | span.user-post\_\_score-count |
| czy opinia jest potwierdzona zakupem | verified | div.review-pz |
| data wystawienia opinii | post\_date | user-post\_\_published \> time:nth-child(1)[datetime] |
| data zakupu produktu | purchase\_date | user-post\_\_published \> time:nth-child(2)[datetime] |
| ile osób uznało opinie za przydatna | vote\_up | buton.vote-yes[data-total-vote]button-bote-yes \> span |
| ile osób uznało opinie za nieprzydatna | vote\_down | buton.vote-no[data-total-vote]button-bote-no \> span |
| treść opinii | content | div.user-post\_\_text |
| lista wad | cons | div.review-feature\_\_title—negatives ~ div.review-feature\_\_item |
| lista zalet | pros | div.review-feature\_\_title—positives ~ div.review-feature\_\_item |

##wykorzystane biblioteki
-BeautifulSoup4
-Requests
