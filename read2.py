data = []
with open ('reviews.txt', 'r') as f:
	count = 0
	for line in f:
		data.append(line)
		count += 1
		#if count % 1000 == 0:
			#print(len(data))

print('finish file reading, and there is', len(data), 'data in total' )

sum_len = 0
for d in data:
	sum_len += len(d)
	

len_avg = sum_len/len(data)
print('the average length of the review is:', len_avg)

print(data[0])