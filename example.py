from coronavirus.covid19api import Coronavirusapi

# Authenticate - Generate Token
covid = Coronavirusapi("testapi1", "coronavirus19")


# Get January 2021 Data
# response = covid.getTimeSeries("jan2021")
# print(response)


# Get Time Series Data
response = covid.getTimeSeries("time_series_recovered_global")
print(response)


