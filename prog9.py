#prog to count frequency of words in a file
from collections import Counter
def wordCounter(lyrics):
	with open(lyrics) as f:
		return Counter(f.read().split())
		
print("No. of words in the file :",wordCounter("highonlife.txt"))
