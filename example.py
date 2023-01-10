from coronavirus.covid19api import Coronavirusapi

# Authenticate - Generate Token
covid = Coronavirusapi("public_user", "public_pass")

# Retrieve January 2023 Data
response = covid.getDailyReport("/v2/jan/2023")
print(response)

# Retrieve Time Series Data
# response = covid.getTimeSeries("/v2/time_series_recovered_global/2023")
# print(response)
