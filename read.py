data = []
count = 0
with open("reviews.txt","r") as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 100000 == 0:
			print(len(data))
print("总共有", len(data), "条留言.")

print(data[0])

wc = {}
for d in data:
	words = d.split(" ")
	for word in words:
		if word in wc:
			 wc[word] += 1
		else:
			wc[word] = 1
for word in wc:
	if wc[word] > 7000:
		print(word, wc[word])
print(len(wc))


while True:
	word = input("请问你要查哪个字的字数?(输入q停止程序)")
	if word == "q":
		break
	elif word not in wc:
		print("请重新输入!")
		continue
	else:
		print("你要查的字数", wc[word])	
	 
#sun_len = 0
#for message in data:
	#sun_len=sun_len + len(message)
#print("流言的平均长度是: ", sun_len/len(data))


#new = []
#for d in data:
	#if len(new_m) < 100:
		#new.append(new_m)
#print("一共有", len(new), "个留言长度少于100.")
#print(new[1]) 

#good = []
#for good_m in data:
	#if "good" in good_m:
		#good.append(good_m)
#print("一共有", len(good), "个留言提到good.")