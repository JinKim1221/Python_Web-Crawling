import requests
from bs4 import BeautifulSoup
from selenium import webdriver
# 1. Today's weather
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"}

def create_soup(url):
    res = requests.get(url, headers = headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def scrape_weather():
    print("=============================================================================")
    print("===============================Today's Weather===============================")
    url = "https://www.google.com/search?q=weather&client=firefox-b-d&sxsrf=ALeKk02ydGsRv96OfIds5no3r62yS-cmwQ%3A1625591388208&ei=XI7kYK6QDKzGxgOdgYLgBg&oq=weather&gs_lcp=Cgdnd3Mtd2l6EAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAELADEEMyBwgAELADEENKBAhBGABQ2IcCWNiHAmCmigJoAnACeACAAZYBiAGWAZIBAzAuMZgBAKABAaoBB2d3cy13aXrIAQrAAQE&sclient=gws-wiz&ved=0ahUKEwiurvnp987xAhUso3EKHZ2AAGwQ4dUDCA0&uact=5"
    soup  = create_soup(url)
    # The weather is like <ex : rainy, cloudy and so on> mostly
    cast = soup.find("span", attrs = {"id" : "wob_dc"}).get_text().lower()
    # Present < >º (lowest < >º / highest < >º)
    current_temp = soup.find("span", attrs = {"id" : "wob_tm"}).get_text()
    
    temp = soup.find("div", attrs = {"class" : "wob_df wob_ds"})
    high_temp = temp.find_next("span", attrs={"class" : "wob_t"}).get_text()
    low_temp = temp.find_next("div", attrs={"class" : "QrNVmd ZXCv8e"}).find_next("span", attrs={"class" : "wob_t"}).get_text()
    # < > % chance of rain 
    precipitation = soup.find("span", attrs = {"id" : "wob_pp"}).get_text()
    
    # OUTPUT
    print(f"Today's weather is like {cast}")
    print(f"Current temperature is {current_temp}°C")
    print(f"The highest temperature is {high_temp}°C,The lowest is {low_temp}°C")
    print(f"Chance of rain : {precipitation}")

    print("============================================================================")

# 3. News Headline
def scrape_headline_news():
    print("=============================================================================")
    print("============================Today's headline news============================")
    url = "https://www.bbc.com/news/world"
    soup = create_soup(url)


    link = "https://www.bbc.com"

    top_headline = soup.find("a", attrs={"class" : "gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-paragon-bold gs-u-mt+ nw-o-link-split__anchor"})
    top_headline_link = top_headline["href"]
    print("<<<<<<TOP HEADLINES>>>>>>")
    print(top_headline.get_text())
    print("read more>>>>>"+link+top_headline_link +"\n")

    headlines_context = soup.find_all("div", attrs={"class" : "gs-c-promo-body gs-u-mt@xxs gs-u-mt@m gs-c-promo-body--flex gs-u-mt@xs gs-u-mt0@xs gs-u-mt--@s gs-u-mt--@m gel-1/2@xs gel-1/1@s"})
    for headlines in headlines_context: 
        headline = headlines.find("a", attrs = {"class" : "gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor"})
        headline_link = headline["href"]
        print(headline.get_text())
        print("read more>>>>>" + link + headline_link+"\n")

# 2. Today's stock that I invested

def scrape_stock_market():
    print("=============================================================================")
    print("============================Today's stock market=============================")
    url = "https://finance.yahoo.com/quote/APC.F?p=APC.F&.tsrc=fin-srch"
    stock_url = {"apple" : "/quote/APC.F?p=APC.F&.tsrc=fin-srch", 
                "ms" : "/quote/MSFT?p=MSFT&.tsrc=fin-srch",
                "ss" : "/quote/XSDG.F?p=XSDG.F&.tsrc=fin-srch"}
    for idx, stock in enumerate(stock_url):
        stock_link = stock_url.get(stock)
        soup  = create_soup(url+stock_link)

        if stock == "apple" : 
            print("<<<<<<<<<< APPLE >>>>>>>>>>")
            
        elif stock == "ms" :
            print("<<<<<<<<<< Microsoft >>>>>>>>>>")
        else:
            print("<<<<<<<<<< Samsung SDI >>>>>>>>>>")

    print("============================================================================")


if __name__ == "__main__" :
    # scrape_weather() # today's weather information
    # scrape_headline_news() # today's global news headlines
    scrape_stock_market()






# 4. 3 Basic Spanish sentences

