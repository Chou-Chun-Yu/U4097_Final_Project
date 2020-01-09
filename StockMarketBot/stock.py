def stockRT(Snum): #Stock Number
	respon = ""
	stock_rt = twstock.realtime.get(Snum)
	cur_datetime = datetime.fromtimestamp(stock_rt["timestamp"]+8*60*60)
	cur_time = cur_datetime.strftime("%H:%M:%S")
	respon += "%s (%s) %s\n"%(stock_rt["info"]["name"],
							   stock_rt["info"]["code"],
							   cur_time)
	respon += "現價: %s / 開盤: %s\n"%(stock_rt["realtime"]["latest_trade_price"],
									   stock_rt["realtime"]["open"])
	respon += "最高: %s / 最低: %s\n"%(stock_rt["realtime"]["high"],
									   stock_rt["realtime"]["low"])
	respon += "量: %s\n" %(stock_rt["realtime"]["accumulate_trade_volume"])
	#stock = twstock.Stock("2330")
	stock = twstock.Stock(Snum)
	respon += "-----\n"
	respon += "最近五日價格: \n"
	price5 = stock.price[-5:][::-1]
	date5 = stock.date[-5:][::-1]
	for i in range(len(price5)):
		respon += "[%s] %s\n" %(date5[i].strftime("%Y-%m-%d"), price5[i])
	return respon
