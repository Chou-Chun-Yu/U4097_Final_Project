def user(profile):
	status = profile.status_message
	if not status:
		status = '-'

	response = [TextSendMessage('Display name: ' + profile.display_name),
				TextSendMessage('picture url: ' + profile.picture_url),
				TextSendMessage('status_message: ' + status),
				]
	return response