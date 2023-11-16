import urllib.request
import numpy as np
import sys
import csv
import os

### Reference
# https://collaboration.cmc.ec.gc.ca/cmc/climate/Get_More_Data_Plus_de_donnees/Command_Lines_EN.txt

# Variables to change
stationID = 1207
dayData = 14 # Only change if you are actually downloading for one day, otherwise keep it since the url requires it.
stationName = 'sparwood5'
startYear = 1990
endYear = 1991
timeframe = 1 # 1: Hourly, 2: Daily, 3: Montly

# Create list of all months
startMonth = 1
endMonth = 12
monthData = [int(x) for x in np.linspace(startMonth,endMonth,endMonth).tolist()]
nYears = (endYear-startYear)

# Create list of all years
yearData = [int(x) for x in np.linspace(startYear,endYear,nYears).tolist()]

for year in yearData:
	for month in monthData:
		print(f'{year}-{month}')
		url = 'https://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&time=utc&stationID='+str(stationID)+'&Year='+str(year)+'&Month='+str(month)+'&Day='+str(dayData)+'&timeframe='+str(timeframe)+'&submit=Download+Data'
		# Add option to do UTC or LST
		source = urllib.request.urlopen(url).read()

		filename = 'data/'+stationName+'/stationID_'+str(stationID)+'year_'+str(year)+'allMonths.csv'
		with open(filename,'wb') as f:
			f.write(source)

# Combine all data into one Excel file

# Grab name of all fines in directory
fList = []
for root, directories, files in os.walk('data/'+stationName):
	for name in files:
		fList.append(os.path.join(root, name))


# Create empty list to store results
allData = []
for fIdx,fName in enumerate(fList):
	with open(fName,newline='') as csvFile:
		file = csv.reader(csvFile,delimiter=',')
		if fIdx != 0:
			next(file)
		for row in file:
			allData.append(row)




with open('data/'+stationName+'/compilledResults.csv', 'w', newline="") as f:
	writer = csv.writer(f)
	writer.writerows(allData)

print('Done!')
