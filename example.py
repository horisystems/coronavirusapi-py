from coronavirus.covid19api import Coronavirusapi

# Authenticate - Generate Token
covid = Coronavirusapi("public_user", "public_pass")

# Get July 2022 Data
response = covid.getDailyReport("/v2/jul/2022")
print(response)

# Get Time Series Data
# response = covid.getTimeSeries("/v2/time_series_recovered_global")
# print(response)
