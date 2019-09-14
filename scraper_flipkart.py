from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

url = 'https://www.flipkart.com/search?q=iphone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_6&otracker1=AS_QueryStore_OrganicAutoSuggest_0_6&as-pos=0&as-type=RECENT&as-searchtext=iphone'

url_data = urlopen(url)
html = url_data.read()
url_data.close()
html_data= soup(html, "html.parser")

contents = html_data.findAll("div", {"class":"_3O0U0u"})
#print(len(contents))
#it gives us the number of items in the flipkart page

#print(soup.prettify(contents[0]))
content = contents[0]
#print(content.div.img["alt"])

price = content.findAll("div", {"class":"_1vC4OE _2rQ-NK"})
#print(price[0].text)

rating = content.findAll("div", {"class":"hGSR34"})
#print(rating[0].text)

fname = "Products_iphone.csv"
fh = open(fname , "w")

headers = "p_name, pricing, p_rating\n"
fh.write(headers)

for content in contents:
    product_name= content.div.img["alt"]
    product_price= content.findAll("div", {"class":"_1vC4OE _2rQ-NK"})
    product_rating= content.findAll("div", {"class":"hGSR34"})
   # print(product_name)
    p_price = product_price[0].text[1:]
   # print(product_rating[0].text)
   # print("\n")

    print(product_name.replace(",", "|") + "," + p_price.replace("," , "") + "," + product_rating[0].text + "\n")
    fh.write(product_name.replace(",", "|") + "," + p_price.replace("," , "") + "," + product_rating[0].text + "\n")

fh.close()