from coronavirus.covid19api import Coronavirusapi

# Authenticate - Generate Token
covid = Coronavirusapi("public_user", "public_pass")


# Get May 2021 Data
response = covid.getTimeSeries("may2021")
print(response)


# Get Time Series Data
response = covid.getTimeSeries("time_series_recovered_global")
print(response)


