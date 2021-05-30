from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# delete stopwords in example sentence
example = "Family is not an important thing.It's Everything"
stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(example)

result = []
for token in word_tokens:
    if token not in stop_words:
        result.append(token)

print(word_tokens)
print(result)
