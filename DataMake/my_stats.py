import csv
from datetime import datetime

import matplotlib.pyplot as plt

import glob



filename = 'stats\MyStats_Data_Daily_2021_5-2022_5.csv'
filename_nippou = r'stats\nippou\日報素データ_20220501_20220531.csv'

filename_nippou_dir = r'stats\nippou'



def dayTime(day_li,time_li):
	day_list = []
	time_list = []

	for i in range(len(day_li)):
		if day_li[i] in day_list:

			index = day_list.index(day_li[i])

			target = time_li[i] + time_list[index]
			time_list[index] = target

		else:
			day_list.append(day_li[i])
			time_list.append(time_li[i])

	return day_list,time_list



def list_make(dates,weights,n,reader):
	for row in reader:
		current_date = datetime.strptime(row[0], '%Y/%m/%d')
		current_weight = row[n]

		try:
			w = float(current_weight)

		except ValueError:
			print(f"Missing data for {current_date}")
		else:

			weights.append(w)
			dates.append(current_date)

with open(filename,encoding='utf-8') as f:
	reader =csv.reader(f)
	stats_title = next(reader)[0]
	header_row = next(reader)

	dates,weights = [],[]
	list_make(dates,weights,1,reader)

	# print("stats" ,dates,weights)


dates_n,weights_n = [],[]
for file in glob.glob("stats/nippou/*.csv"):
	

	with open(file) as f:
		reader =csv.reader(f)
		stats_title = next(reader)[0]
		header_row = next(reader)
		
		list_make(dates_n,weights_n,5,reader)


dates_n_t,weights_n_t = dayTime(dates_n,weights_n)

print(dates_n_t,weights_n_t)

# https://qiita.com/yuto_ohno/items/76e65af37d61c0eff403

# plt.style.use('seaborn')
fig,ax = plt.subplots()

# サブ軸用
nTime = ax.twinx()

# ax.plot(dates,highs,c='red')
# ax.plot(dates,lows,c='blue')
# plt.fill_between(dates,weights,facecolor='blue')
ax.plot(dates,weights,linewidth=3)


nTime.bar(dates_n_t,weights_n_t,linewidth=3,color='red',alpha=0.4)


plt.title(stats_title,fontsize = 24,fontname="MS Gothic")
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()

# ax.ylabel("Temperature (F)",fontsize=16)
# ax.tick_params(axis='both',which='major',labelsize=16)

plt.show()