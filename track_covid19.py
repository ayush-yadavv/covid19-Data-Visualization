import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import requests

url = "https://api.rootnet.in/covid19-in/stats/latest"
response = requests.get(url)
data = response.json()
regions = data["data"]["regional"]
df = pd.DataFrame(regions)
print(df)
df = df.sort_values("totalConfirmed", ascending=False)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
fig.canvas.set_window_title('COVID19 DATA')

ax1.bar(df["loc"], df["totalConfirmed"])
ax1.set_title('COVID-19 Total Confirmed Cases In India')
ax1.set_ylabel('Total Confirmed Cases')
ax1.tick_params(axis='x', rotation=90)

ax2.bar(df["loc"], df["deaths"], color="red")
ax2.set_title('COVID-19 Deaths In India')
ax2.set_xlabel('States Of India')
ax2.set_ylabel('Deaths')
ax2.tick_params(axis='x', rotation=90)

formatter = ticker.StrMethodFormatter('{x:,.0f}')
ax1.yaxis.set_major_formatter(formatter)
ax2.yaxis.set_major_formatter(formatter)

plt.tight_layout()
plt.show()
