data = []
with open("reviews.txt","r") as f:
	for line in f:
		data.append(line)
print(len(data))
print(data[0]+"\n")
print(data[1])
