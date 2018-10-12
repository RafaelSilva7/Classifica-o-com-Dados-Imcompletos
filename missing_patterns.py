
class MissingPatterns():
	d = None # Dataset
	mp = set() # Missing Patterns -> set de frozenset

	"""docstring for MissingPatterns"""
	def __init__(self, d):
		
		for instance in d.data:
			temp = set() # Set
			for i,feature in enumerate(instance, start=0):
				if feature is '?':
					temp.add(i)
			self.mp.add(frozenset(temp)) #set(map(frozenset, t))
			temp.clear()
