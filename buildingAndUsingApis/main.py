import os
from dotenv import load_dotenv
import requests

load_dotenv()

class Forecast():
  API_TYPES = {
    "CITY_LOCATION_CODE": "cityLocationCode",
    "CITY_FORECAST": "cityForecast"
  }
  parameters = {}
  baseReq = os.getenv("API_URL")
  
  def getForecastForCity(self, cityName):
    cityCode = self.getCityCodeLocation(cityName)
    cityForecast = self.__constructApiCall(self.API_TYPES["CITY_FORECAST"], cityCode =  cityCode)
    r = requests.get(cityForecast)
    result = r.json()
    
    f = open("data.txt", "a")
    for data in result:
      write = cityName + ", " + data["DateTime"] + ", " + str(data["Temperature"]["Value"]) + ", " + data["IconPhrase"] + "\n"
      f.write(write)
    
    f.close()
    
    return r
    
  def getCityCodeLocation(self, cityName):
    r = requests.get(self.__constructApiCall(self.API_TYPES["CITY_LOCATION_CODE"], cityName = cityName))
    result = r.json()
    
    return result[0]["Key"]
    
    
    
  def __constructApiCall(self, request, **parameters):
    req = self.baseReq
    if (request == self.API_TYPES["CITY_LOCATION_CODE"]):
      req += 'locations/v1/cities/search/?q=' + parameters["cityName"]
    if (request == self.API_TYPES["CITY_FORECAST"]):
      req += 'forecasts/v1/hourly/12hour/' + parameters["cityCode"] + "?"
      
    req +=  "&apikey=" + os.getenv("API_KEY")
    
    return req
    
  def makeGetRequest(self, request):
    r = requests.get(request)
    
    return r.json()
      
weather = Forecast()

weather.getForecastForCity("botosani")