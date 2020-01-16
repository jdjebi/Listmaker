from django.contrib import messages

MESSAGE_TAG_INFO = 'primary'
MESSAGE_TAG_SUCCESS = 'success'
MESSAGE_TAG_WARNING = 'warning'
MESSAGE_TAG_ERROR = 'danger'

class Notify:

	@classmethod
	def info(cls,request,msg):
		messages.info(request,msg,extra_tags=MESSAGE_TAG_INFO)

	@classmethod
	def success(cls,request,msg):
		messages.success(request,msg,extra_tags=MESSAGE_TAG_SUCCESS)

	@classmethod
	def warning(cls,request,msg):
		messages.warning(request,msg,extra_tags=MESSAGE_TAG_WARNING)

	@classmethod
	def error(cls,request,msg):
		messages.error(request,msg,extra_tags=MESSAGE_TAG_ERROR)