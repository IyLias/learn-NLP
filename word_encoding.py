from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

text = "A barber is a person. a barber is good person. a barber is huge person. he Knew A Secret! The Secret He Kept is huge secret. Huge secret. His barber kept his word.a barber kept his word. His barber kept his secret. But keeping and keeping such a huge secret to himself was driving the barber crazy. the barber went up a huge mountain."

text = sent_tokenize(text)
print(text)

vocab = {}
sentences = []
stop_words = set(stopwords.words('english'))

for i in text:
    sentence = word_tokenize(i)
    result = []

    for word in sentences:
        word = word.lower()
        if word not in stop_words:
            if len(word) > 2:
               result.append(word)
               if word not in vocab:
                   vocab[word] = 0
               vocab[word]+=1
    sentences.append(result)
print(sentences)


vocab_sorted = sorted(vocab.items(),key= lambda x:x[1], reverse =True)

word_to_index = {}
i=0
for (word,frequency) in vocab_sorted:
    if frequency > 1:
        i+=1
        word_to_index[word] = i
print(word_to_index)

