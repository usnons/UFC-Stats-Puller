import requests  # import the requests library to send HTTP requests
from bs4 import BeautifulSoup  # import the BeautifulSoup library to parse HTML

BASE_URL = "http://ufcstats.com/statistics/fighters"  # set the base URL
CHARACTERS = "abcdefghijklmnopqrstuvwxyz"  # set the characters to loop through
PAGE_ALL = "?char=a&page=all"  # set the page parameter to retrieve all pages

headers = ["First", "Last", "Nickname", "Ht.", "Wt.", "Reach", "Stance", "W", "L", "D", "Belt"]  # set the table headers
print("|".join(headers))  # print the headers with a pipe delimiter

for character in CHARACTERS:  # loop through the characters
    url = f"{BASE_URL}?char={character}{PAGE_ALL}"  # create the URL for the current character and page parameter
    response = requests.get(url)  # send an HTTP GET request to the URL and store the response
    soup = BeautifulSoup(response.content, "html.parser")  # parse the HTML content of the response using BeautifulSoup

    table = soup.find("table")  # find the table element in the HTML using BeautifulSoup
    rows = table.find_all("tr")[1:]  # find all the rows in the table, except the first row which contains the headers

    for row in rows:  # loop through the rows
        cells = row.find_all("td")  # find all the cells in the row
        if len(cells) >= 11:  # check if the row contains sufficient data
            name = cells[1].find("a").text.strip()  # extract the fighter's name
            height = cells[2].text.strip()  # extract the fighter's height
            weight = cells[3].text.strip()  # extract the fighter's weight
            reach = cells[4].text.strip()  # extract the fighter's reach
            stance = cells[5].text.strip()  # extract the fighter's stance
            wins = cells[6].text.strip()  # extract the fighter's number of wins
            losses = cells[7].text.strip()  # extract the fighter's number of losses
            draws = cells[8].text.strip()  # extract the fighter's number of draws
            belt = cells[10].text.strip()  # extract the fighter's belt

            print(f"{name}|{height}|{weight}|{reach}|{stance}|{wins}|{losses}|{draws}|{belt}")  # print the fighter's data with a pipe delimiter
        else:
            print("Skipping row with insufficient data")  # print a message if the row contains insufficient data
