from flask import Flask
from fetch import get_single_url_table, extract_data_from_html
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

@app.route('/')
def start():
    raw_table = get_single_url_table(NFL_STATS_URL + offense_stats_list[0])
    extracted_data = extract_data_from_html(raw_table)
    return '<h1>Hello from Flask & Docker</h2>'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)