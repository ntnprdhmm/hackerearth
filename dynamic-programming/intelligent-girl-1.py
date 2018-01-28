# read the string and create a result array with 1 if even
result = [0 if int(v)%2 else 1 for v in input()]
# sum from right to left
for i in range(len(result)-2, -1, -1):
    result[i] += result[i+1]
# join and print result array
print(' '.join([str(v) for v in result]))
