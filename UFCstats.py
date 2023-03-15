import requests
from bs4 import BeautifulSoup

BASE_URL = "http://ufcstats.com/statistics/fighters"
CHARACTERS = "abcdefghijklmnopqrstuvwxyz"
PAGE_ALL = "?char=a&page=all"

headers = ["First", "Last", "Nickname", "Ht.", "Wt.", "Reach", "Stance", "W", "L", "D", "Belt"]
print("|".join(headers))

for character in CHARACTERS:
    url = f"{BASE_URL}?char={character}{PAGE_ALL}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.find("table")
    rows = table.find_all("tr")[1:]

    for row in rows:
        cells = row.find_all("td")
        if len(cells) >= 11:
            name = cells[1].find("a").text.strip()
            height = cells[2].text.strip()
            weight = cells[3].text.strip()
            reach = cells[4].text.strip()
            stance = cells[5].text.strip()
            wins = cells[6].text.strip()
            losses = cells[7].text.strip()
            draws = cells[8].text.strip()
            belt = cells[10].text.strip()

            print(f"{name}|{height}|{weight}|{reach}|{stance}|{wins}|{losses}|{draws}|{belt}")
        else:
            print("Skipping row with insufficient data")
