sentence = "The Quick Brown Fox Jumps Over The Lazy Dog"
words=sentence.split()
word_frequency = {}
word = 0
for word in words:
    if word in word_frequency:
        word+=1
    else:
        word=1
print(word_frequency)
