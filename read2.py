data = []
with open ('reviews.txt', 'r') as f:
	count = 0
	for line in f:
		data.append(line)
		count += 1
		#if count % 1000 == 0:
			#print(len(data))

print('Finish file reading, and there are', len(data), 'reviews' )

sum_len = 0
for d in data:
	sum_len += len(d)
	

len_avg = sum_len/len(data)
print('The average length of the review is:', len_avg)

new = []
for d in data:
	if len(d) < 100:
		new.append(d)

print('There are', len(new), 'reviews with less than 100 charactors')


good = []
for d in data:
	if 'good' in d:
		good.append(d)

print('There are', len(good), 'positive reviews')

print(good[0])

good2 = [d for d in data if 'good' in d]
#list comprehension 
good3 = [1 for d in data if 'good' in d]
#print(good3)

reviews = [d for d in data] 

bad = ['bad' in d for d in data]

bad2 = []
for d in data:
	bad2.append('bad' in d)

print(reviews)











