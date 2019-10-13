data = []
count = 0
with open("reviews.txt","r") as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 100000 == 0:
			print(len(data))
print("总共有", len(data), "条留言.")
	
sun_len = 0
for message in data:
	sun_len=sun_len + len(message)
print("流言的平均长度是: ", sun_len/len(data))


new = []
for new_m in data:
	if len(new_m) < 100:
		new.append(new_m)
print("一共有", len(new), "个留言长度少于100.")
print(new[1])