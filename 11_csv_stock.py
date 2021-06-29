import csv
from bs4.element import SoupStrainer
import requests
from bs4 import BeautifulSoup


filename = "stock_price1-200.csv"
f = open (filename, "w", encoding="utf8", newline="")
writer = csv.writer(f)

for page in range(0, 1) :

    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"}
    url = "https://finance.yahoo.com/screener/predefined/ms_technology?count=25&offset={}".format(page * 25)

    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    title = "Symbol, Name, Price (Intraday), Change,  % Change,  Volume, Avg Vol (3 month), Market Cap, PE Ratio (TTM)".split(", ")
    # ["Symbor Name" , Price(Intradaday), "Change", ...]
    writer.writerow(title)
    # print(type(title))

    data_rows = soup.find("table", attrs={"class" : "W(100%)"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        data = [column.get_text() for column in columns]
        # print(data)
        writer.writerow(data)