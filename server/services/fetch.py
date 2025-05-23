import requests 
from bs4 import BeautifulSoup

# {fetch date , found tables}

def get_data_soup(link): 
    data = requests.get(link).text
    soup = BeautifulSoup(data, 'html.parser')
    return soup

def get_date(soup): 
   date_html = soup.find('input', class_='custom-date')
   found_date = date_html["value"]
   return found_date

# link to raw data
# TODO get the date and season 
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

# write data to a json 
def write_data_to_csv(raw_data, data_name, location):
   return


# save json to postgres for record keeping
#file name conventions: sports type + sources + date