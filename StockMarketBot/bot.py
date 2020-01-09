def user(profile):
	status = '-' if not userStatus else profile.status_message
	'''
	my_status_message = profile.status_message
	if not my_status_message:
		my_status_message = '-'
	'''
	response = [TextSendMessage('Display name: ' + profile.display_name),
				TextSendMessage('picture url: ' + profile.picture_url),
				TextSendMessage('status_message: ' + my_status_message),
				]
	return response