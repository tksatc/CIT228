import json
import datetime

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data
filename = "Chapter16/data/eq_significant_week.json"
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data["features"]

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    # Test date conversion
    """
    for date in dates:
        datetime.datetime.fromtimestamp(int(date)
            ).strftime('%Y-%m-%d %H:%M"%S')
        date = eq_dict["properties"]["time"]
        dates.append(date)
    """
    mag= eq_dict["properties"]["mag"]
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    title = eq_dict["properties"]["title"]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

# Map the earthquakes
data = [{
    "type": "scattergeo",
    #"time": dates,
    "lon": lons,
    "lat": lats,
    "text": hover_texts,
    "marker": {
        "size": [5*mag for mag in mags],
        "color": mags,
        "colorscale": "Viridis",
        "reversescale": True,
        "colorbar": {"title": "Magnitude"},
    },
}]
my_layout = Layout(title="Major Earthquakes\nMarch 3 - 10, 2021")

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="major_eq_2ndweek_March_2021.html")
