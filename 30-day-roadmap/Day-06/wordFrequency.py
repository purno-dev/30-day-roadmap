sentence = "The Quick Brown Fox Jumps Over The Lazy Dog"
words=sentence.split()
word_frequency = {}
word_count=0
for word in words:
    if (word in word_frequency):
        word_count+=1
    else:
        word_count=1
    word_frequency[word]=word_count
print(word_frequency)