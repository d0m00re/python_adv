# https://fr.wikipedia.org/wiki/Proxy_(patron_de_conception)
# https://zestedesavoir.com/tutoriels/954/notions-de-python-avancees/1-starters/1-containers/

# un proxy a pour objectif a se subsister a un autre.
# Creation d un proxy a partir d une liste existante:

#En programmation, un proxy est un patron de conception.
#Un proxy est une classe se substituant à une autre classe. Par convention et simplicité, le proxy implémente la même interface que la classe à laquelle il se substitue1.
#L'utilisation de ce proxy ajoute une indirection à l'utilisation de la classe à substituer1.

class MyList:
	def __init__(self, value=()): # emulation du constructeur de list
		self.internal = list(value)

	def __len__(self):
		return len(self.internal)

	def __getitem__(self, key):
		return self.internal[key] # Equivalent a return self.internal.__getitem__(key)

	def __setitem__(self, key, value):
		self.internal[key] = value

	def __delitem__(self, key):
		del self.internal[key]

numbers = MyList('123456')
print (len(numbers))
print (numbers[1])
numbers[1] = '0'
print (numbers[1])
del numbers[1]
print (len(numbers))
