class Universe:
	def __init__(self):
		self._name = None
		
	@property
	def name(self):
		return self._name
		
	@name.setter
	def name(self, value):
		self._name = value
		
  @name.deleter
  def name(self):
  	del self._name
