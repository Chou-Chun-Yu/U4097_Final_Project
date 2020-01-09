from __future__ import unicode_literals
from datetime import timedelta, datetime
from pymongo import MongoClient
from imgurpython import ImgurClient
from flask import Flask, request, abort
from linebot import (
	LineBotApi, WebhookHandler
)
from linebot.exceptions import (
	InvalidSignatureError
)
from linebot.models import *
import twstock, random, time, matplotlib, bot
import matplotlib.pyplot as plt
import pandas as pd
matplotlib.use('Agg')

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('2xKVmBADbCqgHkTah4XjfrZ8GL01xFN1pV6BxB9tlbEkyeGyPWbPv7IE8iJlSbgc/9UDkNqEXoAYY193w1ED6I2EEJcdgFBQJcrnujJYEDj3UmQn1CpwgknsY7xSc3LYDaW2G9MDDAP44ch1E7fCGwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('696fbdfbd93968f7f833125cc0b6f456')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
	# get X-Line-Signature header value
	signature = request.headers['X-Line-Signature']
	# get request body as text
	body = request.get_data(as_text=True)
	app.logger.info("Request body: " + body)
	# handle webhook body
	try:
		handler.handle(body, signature)
	except InvalidSignatureError:
		abort(400)
	return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
	if event.message.text.lower()=='me':
		message = str(event.source.user_id)
	elif (event.message.text.lower() == 'profile'):
		profile = line_bot_api.get_profile(event.source.user_id)
		message = bot.user(profile)
	elif (event.message.text.lower() == "help"):
		help_log = "完整的查詢天氣，請輸入[縣市名][天氣] e.g. '新北市天氣如何?'"
		message = TextSendMessage(help_log)
	else:
		invalidSentence = "無法辨識的內容，輸入[help]獲得更多資訊"
		message = TextSendMessage(invalidSentence)
	line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)