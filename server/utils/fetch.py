import requests 
from bs4 import BeautifulSoup

from datetime import datetime 
from pathlib import Path



# get the whole page in html
def get_data_soup(link): 
    data = requests.get(link).text
    soup = BeautifulSoup(data, 'html.parser')
    return soup

def get_date(soup): 
   date_html = soup.find('input', class_='custom-date')
   found_date = date_html["value"]
   return found_date

def get_table(soup):
    found_table = soup.find('table', class_='tr-table datatable scrollable')
    return found_table

# raw data to a dictionary
def extract_data_from_html(raw_table):
   headers = [header.text.strip() for header in raw_table.find_all('th')]
   rows = raw_table.find_all("tr")
   clean_rows = []
   for row in rows: 
      cols = row.find_all('td')
      cols = [ele.text.strip() for ele in cols]
      if len(cols) > 0:
         clean_rows.append(cols)
   return {"headers": headers, "rows": clean_rows}

# write data to html 
# file_name need to be the whole file path for s3
def create_raw_html(soup, file_name):
   html_dir = Path("data/tmp")
   html_dir.mkdir(parents=True, exist_ok=True)

   file_path = html_dir/ file_name

   with open(file_path, "w", encoding="utf-8") as f:
      f.write(soup.prettify())
   return str(file_path)

def generate_data_filename(type, metric, scrape_date):
   if(scrape_date) is None: 
        scrape_date = datetime.now()
   date_str = scrape_date.strftime("%Y%m%d")
   if type is "raw":
       return f"{metric}_{date_str}.html"
   else:
      return f"{metric}_{date_str}.csv"

def generate_data_filepath(type, sport, tournament, season, source_type, filename):
   if type is "raw":
      return f"raw/{sport}/{tournament}/{season}/{source_type}/{filename}"
   else:
      return f"processed/{sport}/{tournament}/{season}/{source_type}/{filename}"


NFL_STATS_URL = "https://www.teamrankings.com/nfl/stat/"
offense_stats_list = [
    "points-per-game",  
    "passing-yards-per-game",
    "rushing-yards-per-game",
    "yards-per-game",
    "red-zone-scoring-pct"
]

def get_offense(): 
    data_per_category = {}
    for link in offense_stats_list: 
        soup = get_data_soup(NFL_STATS_URL + link)
        raw_table = get_table(soup)
         # store the raw table 
        extracted_data = extract_data_from_html(raw_table)
         #  parsed data to csv + name file + file path
        data_per_category[link] = extracted_data
    print(data_per_category)
    return data_per_category

if __name__ == '__main__':
    get_offense()