def user(profile):
	status = '-' if not userStatus else profile.status_message
	'''
	my_status_message = profile.status_message
	if not my_status_message:
		my_status_message = '-'
	'''
	response = [TextSendMessage(text='Display name: ' + profile.display_name),
				TextSendMessage(text='picture url: ' + profile.picture_url),
				TextSendMessage(text='status_message: ' + my_status_message),
				]