import requests
from bs4 import BeautifulSoup
# 1. Today's weather
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"}

def scrape_weather():
    url = "https://www.google.com/search?q=weather&client=firefox-b-d&sxsrf=ALeKk02ydGsRv96OfIds5no3r62yS-cmwQ%3A1625591388208&ei=XI7kYK6QDKzGxgOdgYLgBg&oq=weather&gs_lcp=Cgdnd3Mtd2l6EAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAELADEEMyBwgAELADEENKBAhBGABQ2IcCWNiHAmCmigJoAnACeACAAZYBiAGWAZIBAzAuMZgBAKABAaoBB2d3cy13aXrIAQrAAQE&sclient=gws-wiz&ved=0ahUKEwiurvnp987xAhUso3EKHZ2AAGwQ4dUDCA0&uact=5"
    res = requests.get(url, headers = headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    print("=============================================================================")
    print("===============================Today's Weather===============================")
    # The weather is like <ex : rainy, cloudy and so on> mostly
    cast = soup.find("span", attrs = {"id" : "wob_dc"}).get_text()
    # Present < >º (lowest < >º / highest < >º)
    current_temp = soup.find("span", attrs = {"id" : "wob_tm"}).get_text()
    high_temp = soup.find("div", attrs = {"class" : "wob_df wob_ds"}).find_next("span", attrs={"class" : "wob_t"}).get_text()
    low_temp = soup.find("div", attrs = {"class" : "wob_df wob_ds"}).find_next("div", attrs={"class" : "QrNVmd ZXCv8e"}).find_next("span", attrs={"class" : "wob_t"}).get_text()
    # < > % chance of rain 
    precipitation = soup.find("span", attrs = {"id" : "wob_pp"}).get_text()
    
    # OUTPUT
    print(f"Today's weather is like {cast}")
    print(f"Current temperature is {current_temp}°C")
    print(f"The highest temperature is {high_temp}°C,The lowest is {low_temp}°C")
    print(f"Chance of rain : {precipitation}")

    print("============================================================================")

if __name__ == "__main__" :
    scrape_weather() # today's weather information

# 2. Today's stock that I invested

# 3. News Headline

# 4. 3 Basic Spanish sentences

