import requests 
from bs4 import BeautifulSoup

NFL_STATS_URL = "https://www.teamrankings.com/nfl/stat/"
offense_stats_list = [
   "points-per-game",  
   "passing-yard-per-game",
   "rushing-yard-per-game",
   "yards-per-game"
]

def get_url_data():
    data = requests.get(NFL_STATS_URL + offense_stats_list[0]).text
    soup = BeautifulSoup(data, 'html.parser')
    found_table = soup.find('table', class_='tr-table datatable scrollable')
    print(found_table)
    return found_table
