## Bulk ECCC Station Download
This script downloads bulk data from an ECCC station using the station ID. Note that this is different than the climate ID found on the ECCC page. The station ID is found in the URL.

## Python libraries you need to install
- numpy
- urllib3

## Disclaimer
Use at your own discretion. You will need to make sure that you have a directory within the data directory that has the same name as the station name you set in the downloadData.py script. Otherwise, the script won't run.

## Description
In this example, the link below takes you to the Sparwood ECCC station page. Look at the URL and notice that the URL has a parameter called stationID followed by <i>=1207</i>. The 1207 is the station ID you need to enter below.

https://climate.weather.gc.ca/climate_data/hourly_data_e.html?hlyRange=1980-03-03%7C2014-10-02&dlyRange=1980-03-01%7C2020-02-22&mlyRange=1980-01-01%7C2007-02-01&StationID=1207&Prov=BC&urlExtension=_e.html&searchType=stnName&optLimit=yearRange&StartYear=1840&EndYear=2023&selRowPerPage=25&Line=0&searchMethod=contains&Month=10&Day=2&txtStationName=sparwood&timeframe=1&Year=2014

[click here to go to ECCC page] ("https://climate.weather.gc.ca/climate_data/hourly_data_e.html?hlyRange=1980-03-03%7C2014-10-02&dlyRange=1980-03-01%7C2020-02-22&mlyRange=1980-01-01%7C2007-02-01&StationID=1207&Prov=BC&urlExtension=_e.html&searchType=stnName&optLimit=yearRange&StartYear=1840&EndYear=2023&selRowPerPage=25&Line=0&searchMethod=contains&Month=10&Day=2&txtStationName=sparwood&timeframe=1&Year=2014" target="_blank">)

Depending on your data request, the script can take several minutes to process. Do not refresh or close the page, the csv file will automatically download when ready.