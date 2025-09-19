from server.utils.fetch import get_data_soup, get_table, get_date, extract_data_from_html

# these data will soon fetch from db
NFL_STATS_URL = "https://www.teamrankings.com/nfl/stat/"
offense_stats_list = [
    "points-per-game",  
    "passing-yards-per-game",
    "rushing-yards-per-game",
    "yards-per-game",
    "red-zone-scoring-pct"
]

defense_stats_list = [
    "opponent-points-per-game", 
    "opponent-passing-yards-per-game",
    "opponent-rushing-yards-per-game",
    "opponent-yards-per-game",
    "opponent-red-zone-scoring-pct"
]

def get_offense(): 
    data_per_category = {}
    for link in offense_stats_list: 
        soup = get_data_soup(NFL_STATS_URL + link)
        raw_table = get_table(soup)
        data_date = get_date(soup)
        extracted_data = extract_data_from_html(raw_table)
        data_per_category[link] = extracted_data
    print(data_per_category)
    return data_per_category

def get_deffense():
    data_per_category = {}
    for link in defense_stats_list: 
        soup = get_data_soup(NFL_STATS_URL + link)
        raw_table = get_table(soup)
        data_date = get_date(soup)
        extracted_data = extract_data_from_html(raw_table)
        data_per_category[link] = extracted_data
    return data_per_category

if __name__ == '__main__':
    get_offense()