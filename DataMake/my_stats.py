import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'stats\MyStats_Data_Daily_2021_5-2022_5.csv'
filename_nippou = 'stats\nippou\日報素データ_20220501_20220531.csv'


with open(filename,encoding='utf-8') as f:
	reader =csv.reader(f)
	stats_title = next(reader)[0]
	header_row = next(reader)

	dates,weights = [],[]
	for row in reader:
		current_date = datetime.strptime(row[0], '%Y/%m/%d')
		current_weight = row[1]

		try:
			w = float(current_weight)

		except ValueError:
			print(f"Missing data for {current_date}")
		
		else:

			weights.append(w)
			dates.append(current_date)

			print(w)

	print(dates,weights)








plt.style.use('seaborn')
fig,ax = plt.subplots()
# ax.plot(dates,highs,c='red')
# ax.plot(dates,lows,c='blue')
# plt.fill_between(dates,weights,facecolor='blue')
plt.plot(dates,weights,linewidth=3)

plt.title(stats_title,fontsize = 24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()