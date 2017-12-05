input = """ """
arr = input.split('\n')

def check_line(line):
	words = []
	for j in range(len(line)):
		if line[j] in words:
			return 0 
		words.append(line[j])
	return 1

def check_anagrams(line):
	anagrams = []
	for j in range(len(line)):
		srt = ''.join(sorted(line[j]))
		if srt in anagrams:
			return 0 
		anagrams.append(srt)
	return 1

valid_words = 0
valid_anagrams = 0

for i in range(len(arr)):
	# Part 1
	valid_words += check_line(arr[i].split())
	# Part 2
	valid_anagrams += check_anagrams(arr[i].split())

print valid_words
print valid_anagrams