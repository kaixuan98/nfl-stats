from flask import Flask, jsonify
from dotenv import load_dotenv
from src.fetch import get_data_soup, get_date, get_table, extract_data_from_html
from src.store import supabase

load_dotenv()
app = Flask(__name__)


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

@app.route('/nfl/offense')
def get_offense():
    # offense 
    data_per_category = {}
    for link in offense_stats_list: 
        soup = get_data_soup(NFL_STATS_URL + link)
        raw_table = get_table(soup)
        data_date = get_date(soup)
        extracted_data = extract_data_from_html(raw_table)
        data_per_category[link] = extracted_data
    return '<h1>Offense Data</h1>'

@app.route('/nfl/defense')
def get_deffense():
    for link in defense_stats_list: 
        soup = get_data_soup(NFL_STATS_URL + link)
        raw_table = get_table(soup)
        data_date = get_date(soup)
        extracted_data = extract_data_from_html(raw_table)
        print(extracted_data)
    return '<h1>Deffense Datas</h2>'

@app.route('/accessDB')
def get_data():
    try:
        response = supabase.table("sports").select("*").execute()
        return jsonify(response.data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)