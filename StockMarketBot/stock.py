if(text.startswith('#')):
	text = text[1:]
	content = ''
	stock_rt = twstock.realtime.get(text)
	my_datetime = datetime.fromtimestamp(stock_rt['timestamp']+8*60*60)
	my_time = my_datetime.strftime('%H:%M:%S')
	content += '%s (%s) %s\n' %(
		stock_rt['info']['name'],
		stock_rt['info']['code'],
		my_time)
	content += '現價: %s / 開盤: %s\n'%(
		stock_rt['realtime']['latest_trade_price'],
		stock_rt['realtime']['open'])
	content += '最高: %s / 最低: %s\n' %(
		stock_rt['realtime']['high'],
		stock_rt['realtime']['low'])
	content += '量: %s\n' %(stock_rt['realtime']['accumulate_trade_volume'])
	stock = twstock.Stock(text)#twstock.Stock('2330')
	content += '-----\n'
	content += '最近五日價格: \n'
	price5 = stock.price[-5:][::-1]
	date5 = stock.date[-5:][::-1]
	for i in range(len(price5)):
		#content += '[%s] %s\n' %(date5[i].strftime("%Y-%m-%d %H:%M:%S"), price5[i])
		content += '[%s] %s\n' %(date5[i].strftime("%Y-%m-%d"), price5[i])
	line_bot_api_8.reply_message(
		event.reply_token,
		TextSendMessage(text=content)
	)
elif(text.startswith('/')):
	text = text[1:]
	fn = '%s.png' %(text)
	stock = twstock.Stock(text)
	my_data = {'close':stock.close, 'date':stock.date, 'open':stock.open}
	df1 = pd.DataFrame.from_dict(my_data)
	df1.plot(x='date', y='close')
	plt.title('[%s]' %(stock.sid))
	plt.savefig(fn)
	plt.close()
	# -- upload
	# imgur with account: your.mail@gmail.com
	client_id = 'your imgur client_id'
	client_secret = 'your imgur client_secret'
	client = ImgurClient(client_id, client_secret)
	print("Uploading image... ")
	image = client.upload_from_path(fn, anon=True)
	print("Done")
	url = image['link']
	image_message = ImageSendMessage(
		original_content_url=url,
		preview_image_url=url
	)
	line_bot_api_8.reply_message(
		event.reply_token,
		image_message
	)