import random

def vector_aleatorio():
	array=[0]

	for i in range(10):
		j = random.randint(0, 10)
		array.append(j)

	return array

print(vector_aleatorio())

