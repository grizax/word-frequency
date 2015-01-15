import re
import collections
import pprint

with open('sample.txt') as word_frequency:               #opens txt as dict using with
    m = collections.Counter(word.lower()                 #lowercases and counts
        for line in word_frequency
        for word in re.findall(r'\b[^\W\d_]+\b', line))  #ignores b.s. using powerful re.findall

    a = (m.most_common(20))                              #sorts by most common 20 words

    pprint.pprint(a, width=50)                           #set width to 50 to show large numbers
