import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'stats\MyStats_Data_Daily_2021_5-2022_5.csv'

with open(filename,encoding='utf-8') as f:
	reader =csv.reader(f)
	stats_title = next(reader)
	header_row = next(reader)

	# for row in reader:
	# 	print(row)

	# for index,column_header in enumerate(header_row):
	# 	print(index,column_header)



	dates,weights = [],[]
	for row in reader:
		current_date = datetime.strptime(row[0], '%Y/%m/%d')
		current_weight = row[1]

		# print(current_date,current_weight)

		# if current_weight is None:

		try:
			w = float(current_weight)

		except ValueError:
			print(f"Missing data for {current_date}")
		
		else:

			weights.append(w)
			dates.append(current_date)

			print(w)

	print(dates,weights)




	# for index , column_header in enumerate(header_row):
 	# 	print(index,column_header)


plt.style.use('seaborn')
fig,ax = plt.subplots()
# ax.plot(dates,highs,c='red')
# ax.plot(dates,lows,c='blue')
plt.fill_between(dates,weights,facecolor='blue')

plt.title("stats_title",fontsize = 24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()