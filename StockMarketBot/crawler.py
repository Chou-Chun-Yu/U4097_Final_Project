import requests
import pandas as pd

link = "http://api.opencube.tw/weather"
taiwan_cities = ["臺北市","台北市","新北市","桃園市","臺中市",
				 "台中市","臺南市","高雄市","基隆市","新竹市",
				 "嘉義市","新竹縣","苗栗縣","彰化縣","南投縣",
				 "雲林縣","嘉義縣","屏東縣","宜蘭縣","花蓮縣",
				 "臺東縣","台東縣","澎湖縣","金門縣","連江縣"]

def getLocation(question):
	for city in taiwan_cities:
		if city in question:
			if "臺" in city:
				city = city.replace("臺", "台");
			return city
	return "桃園市"
	'''
	if any(city in question for city in taiwan_cities):
		return city
	'''


def getReportWithAPI():
	res = requests.get(link)
	return res.json()

def getReport(sentence):
	report = getReportWithAPI()
	location = getLocation(sentence)
	response = getResponse(report, location)
	return response

def getResponse(report, location):
	df_temp = pd.DataFrame(report['data'])
	df_temp = df_temp.transpose()
	df_temp.set_index('city', inplace=True)
	print(df_temp)
	locWeather = df_temp.loc[location, "weather"]
	locNotice = df_temp.loc[location, "notice"]
	maxTem = df_temp.loc[location, "maxTemperature"]
	minTem = df_temp.loc[location, "minTemperature"]
	rain = df_temp.loc[location, "pop"]
	respon = "%s的天氣是%s，%s\n氣溫為%.1f~%.1f°C\n降雨機率為%.1f%%"%(location, locWeather, locNotice,minTem, maxTem, rain)
	return respon