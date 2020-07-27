from rest_framework import permissions



class IsStudent(object):
	"""Only Student allowed"""
	def __init__(self ):
		# super(IsStudent, self).__init__()
		# self.arg = arg

		# return bool(True)
		pass

	def has_permission(self, request, view):
		""" Global permission check for blacklisted IPs."""
		# print(">>>>>>", view.UserViewSet)
		# print(">>>>>>", request.user.profile.is_student)
		return True
		# return False
		pass

	def has_object_permission(self, request, view, obj):
		return True
		pass
		