# object ayant pour vocation de contenir d autres
# differentes categories de conteneur
#	subscriptables : operateur []
		# indexables : indexable
		# sliceables : avec des slice
		# on parle de sequence

# L'operateur in est definit dans la methode __contains__()

if 3 in (1, 2, 3): # true
	print ("Good : 3 in (1, 2, 3)")
if 4 not in (1, 2, 3): # true
	print ("Good : 4 not in (1, 2, 3)")

if '0' in 'd0m00re':
	print ("Good : 0 in 'd0m00re'")

if 'd0m00re'.__contains__('0'):
	print ("Good : 'd0m00re'.__contains__('0')")


# test avec une classe
class MyContainer:
	def __contains__(self, value):
		return value is not None # contien tout sauf none

class MySize:
	def __len__(self):
		return (18)

if 'salut' in MyContainer():
	print ("Good class : 'salut' in MyContainer()")

#les conteneurs possede une taille
# len call methode __len__
print ("Container test len([1, 2, 3]) : " + str(len([1, 2, 3])))
print ("Container test class str(len(MySize()))  : " + str(len(MySize())))
