# three_charts.py

#import packages
import plotly
import plotly.graph_objs as go

labels = []
values = []

labels1 = []
values1 = []

labels2 = []
values2 = []

#
# CHART 1 (PIE)
#

pie_data = [
    {"company": "Company X", "market_share": 0.55},
    {"company": "Company Y", "market_share": 0.30},
    {"company": "Company Z", "market_share": 0.15}
]

for p in pie_data:
    labels.append(p["company"])
    values.append(p["market_share"])



print("----------------")
print("GENERATING PIE CHART...")
trace = go.Pie(labels=labels, values=values)

plotly.offline.plot([trace], filename="basic_pie_chart.html", auto_open=True)

#
# CHART 2 (LINE)
#

line_data = [
    {"date": "2019-01-01", "stock_price_usd": 100.00},
    {"date": "2019-01-02", "stock_price_usd": 101.01},
    {"date": "2019-01-03", "stock_price_usd": 120.20},
    {"date": "2019-01-04", "stock_price_usd": 107.07},
    {"date": "2019-01-05", "stock_price_usd": 142.42},
    {"date": "2019-01-06", "stock_price_usd": 135.35},
    {"date": "2019-01-07", "stock_price_usd": 160.60},
    {"date": "2019-01-08", "stock_price_usd": 162.62},
]

for p in line_data:
    labels1.append(p["date"])
    values1.append(p["stock_price_usd"])


print("----------------")
print("GENERATING LINE GRAPH...")
plotly.offline.plot({
    "data": [go.Scatter(x=labels1, y=values1)],
    "layout": go.Layout(title="Date vs. Stock Price")
}, auto_open=True)

#
# CHART 3 (HORIZONTAL BAR)
#

bar_data = [
    {"genre": "Thriller", "viewers": 123456},
    {"genre": "Mystery", "viewers": 234567},
    {"genre": "Sci-Fi", "viewers": 987654},
    {"genre": "Fantasy", "viewers": 876543},
    {"genre": "Documentary", "viewers": 283105},
    {"genre": "Action", "viewers": 544099},
    {"genre": "Romantic Comedy", "viewers": 121212}
]

for p in bar_data:
    labels2.append(p["genre"])
    values2.append(p["viewers"])

print("----------------")
print("GENERATING BAR CHART...")

trace = go.Bar(x = labels2, y = values2)

plotly.offline.plot([trace], filename="basic_bar_chart.html", auto_open=True)


