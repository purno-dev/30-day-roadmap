sentence = "for the people by the people of the people"
words=sentence.split()
word_frequency = {}
word_count=0
for word in words:
    if (word in word_frequency):
        word_frequency[word]+=1
    else:
        word_frequency[word]=1
    
print(word_frequency)