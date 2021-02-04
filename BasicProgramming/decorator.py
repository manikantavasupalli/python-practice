

def decorate_lowercase(function):
	def lowerfy():
		funcaa = function()
		string_lower = funcaa.lower()
		return string_lower
	return lowerfy

def splitfy(function):
	def splitt():
		s_value = function()
		str_list = s_value.split()
		return str_list
	return splitt

@splitfy
@decorate_lowercase
def hello():
	return "Hello World!"

print(hello())