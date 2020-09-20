import math

triples = []
ab_dif = [[] for x in range(0,10)]
curr_triples = [[] for x in range(0,10)]
multiplied_triples = [[] for x in range(0,10)]
multiplied_triples_with_ab_ba = [[] for x in range(0,10)]
similar = [[] for x in range(0,10)]
triple_dif = [[] for x in range(0,10)]
k=0

def get_curr_triples(a,b):

	curr_triples = []

	for triple in triples:
		if a == triple[0] or b == triple[0]:
			curr_triples.append(triple)

	print("Triples containing <a,b> or <b,a>: ")
	print(curr_triples)
	print(len(curr_triples))
	print("\n\n")
	return curr_triples

def multiply(curr_triples):

	multiplied_triples = []
	
	curr_triples_length = len(curr_triples)

	for i in range(curr_triples_length):
		for j in range(curr_triples_length):
			if j<=i:
				continue
			triple1 = curr_triples[i]
			triple2 = curr_triples[j]
			t1 = "<" + triple1[0] + "," + triple2[0] + ">"
			t2 = "<" + triple1[1] + "," + triple2[1] + ">"
			t3 = "<" + triple1[2] + "," + triple2[2] + ">"
			multiplied_triples.append(t1+","+t2+","+t3)

	print("Triples after multiplication: ")
	print(len(multiplied_triples))
	print(multiplied_triples)
	print("\n\n")
	return multiplied_triples


def get_ab_ba(a,b):
	
	ab = "<" + a + "," + b + ">"
	ba = "<" + b + "," + a + ">"

	return ab,ba

def get_multiplied_triples_with_ab_ba(multiplied_triples):

	multiplied_triples_with_ab_ba = []

	for triple in multiplied_triples:
		if ab in triple or ba in triple:
			multiplied_triples_with_ab_ba.append(triple)

	print("Triples after filtering out <a,a> and <b,b>:")
	print(multiplied_triples_with_ab_ba)
	print(len(multiplied_triples_with_ab_ba))
	print("\n\n")
	return multiplied_triples_with_ab_ba




a = ""
b = ""

with open("input_triples.txt") as inputfile:

	for line in inputfile:

		line = line.replace("<","")
		line = line.replace(">","")
		line = line.replace("\n","")
		line = line.split(",")
		triples.append(line)

print("Given Triples:")
print(triples)
print("\n\n")

with open("input_ab.txt") as abfile:

	for line in abfile:

		line = line.split()
		a = line[0]
		b = line[1]

print("Current a and b:")
print(a,b)
print("\n\n")

curr_triples.insert(k,get_curr_triples(a,b))

multiplied_triples.insert(k,multiply(curr_triples[k]))

ab,ba = get_ab_ba(a,b)

multiplied_triples_with_ab_ba.insert(k,get_multiplied_triples_with_ab_ba(multiplied_triples[k]))

similar[k] = []

triple_dif[k] = []
ab_dif[k] = []

for triple in multiplied_triples_with_ab_ba[k]:
	aux = triple
	aux = aux.replace("<","")
	aux = aux.replace(">","")
	aux = aux.replace("\n","")
	aux = aux.split(",")
	if aux[2] == aux[3]:
		if aux[4] == aux[5]:
			similar[k].append(triple)
		else:
			ab_aux = []
			ab_aux.append(aux[4])
			ab_aux.append(aux[5])
			ab_dif[k].append(ab_aux)
			triple_dif[k].append(triple)


print("First level similarity:")
for triple in similar[k]:
	print(triple)
print("\n\n")

for y in range(0,10):
	print("New a and b's: ")
	print(ab_dif[k])
	print("\n\n")


	similar[k+1] = []
	triple_dif[k+1] = []
	ab_dif[k+1] = []

	for i in range(len(ab_dif[k])):
		xy = ab_dif[k][i]
		a = xy[0]
		b = xy[1]
		print(a,b)

		curr_triples.insert(k+1,get_curr_triples(a,b))

		multiplied_triples.insert(k+1,multiply(curr_triples[k+1]))

		ab,ba = get_ab_ba(a,b)

		multiplied_triples_with_ab_ba.insert(k+1,get_multiplied_triples_with_ab_ba(multiplied_triples[k+1]))

		for triple in multiplied_triples_with_ab_ba[k+1]:
		
			aux = triple
			aux = aux.replace("<","")
			aux = aux.replace(">","")
			aux = aux.replace("\n","")
			aux = aux.split(",")
			if aux[2] == aux[3]:
				if aux[4] == aux[5]:
					similar_aux = []
					similar_aux.append(triple_dif[k][i])
					similar_aux.append(triple)
					similar[k+1].append(similar_aux)
				else:
					ab_aux = []
					ab_aux.append(aux[4])
					ab_aux.append(aux[5])
					ab_dif[k+1].append(ab_aux)
					triple_dif[k+1].append(triple)
			else:
				ab_aux = []
				ab_aux.append(aux[4])
				ab_aux.append(aux[5])
				ab_dif[k+1].append(ab_aux)
				triple_dif[k+1].append(triple)

	if len(similar[k+1])==0:
		print("No more similarity")
		exit()
	print("Additional/Auxillary similarity:")
	for triple in similar[k+1]:
		print(triple)
	print("\n\n")
	k=k+1

