import requests
from bs4 import BeautifulSoup


for year in range(2016, 2021) :

    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"}
    url = "https://www.google.com/search?q=movies+{}&sxsrf=ALeKk00LWCszIvQLPLxN0IOPub6UsxyQqg%3A1624741690419&source=hp&ei=OpfXYNzHF6OL1fAP9OKwmAI&iflsig=AINFCbYAAAAAYNelSuO9CU55VXgJv7n6ZulmbhQ4QfzZ&oq=movi&gs_lcp=Cgdnd3Mtd2l6EAMYADIECCMQJzIECCMQJzIECCMQJzIHCAAQsQMQQzIHCAAQsQMQQzIECAAQQzIECAAQQzIHCAAQsQMQQzIECAAQQzIECAAQQzoECC4QQ1D4FliuHGDBImgAcAB4AIABT4gBmwKSAQE0mAEAoAEBqgEHZ3dzLXdpeg&sclient=gws-wiz".format(year)

    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("div", attrs={"class" : "VbZgje"})
    # print(len(images))
    for idx, image in enumerate(images) :
        image_url = image["data-tu"]
        print(image_url)
        
        image_res = requests.get(image_url)
        image_res.raise_for_status()

        with open("movie_{}_{}.jpg".format(year, idx+1), "wb") as f :
            f.write(image_res.content) 

        if idx >= 4 : # first 5 movies
            break