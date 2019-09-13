#prog to count frequency of words in a file
from collections import Counter
def wordCounter(lyrics):
	with open(lyrics) as f:
		return Counter(f.read().split())
		
print("No. of words in the file :",wordCounter("highonlife.txt"))

*****
output:
No. of words in the file : Counter({'day': 4, 'the': 4, 'die': 4, 'High': 3, "'til": 3, 'on': 3, 'we': 3, 'life': 3, 'see': 1, "I'd": 1, 'to': 1, 'I': 1, 'million': 1, 'walk': 1, 'And': 1, 'miles,': 1, "'Til": 1, 'just': 1, 'a': 1, 'you': 1, 'smile': 1})

