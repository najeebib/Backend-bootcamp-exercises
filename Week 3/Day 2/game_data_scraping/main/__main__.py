import asyncio
from bs4 import BeautifulSoup
from modules.data_handling import get_data, count_genres
from modules.ploting import plot_data

url = f"https://store.steampowered.com/"
loop = asyncio.get_event_loop()
# get the data from the website
data = loop.run_until_complete(get_data(url))
soup = BeautifulSoup(data, "html.parser")
# find the tab that has the top selling games
results = soup.find(id="tab_topsellers_content")
# find the top 10 games
first_10_a_tags = results.find_all("a", limit=10)
names = []
genres = []
# get the names and genres of the games
for game in first_10_a_tags:
    genre = game.find_all("span", class_="top_tag", limit=1)
    if genre:
        genres.append(genre[0].get_text())
        game_name_div = game.find("div", class_="tab_item_name")
        if game_name_div:
            names.append(game_name_div.get_text())
# count the how many games are in each genre and put it in a dict
genres_count = count_genres(genres)
# plot the data
plot_data(genres_count)