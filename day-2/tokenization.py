import nltk
from nltk.tokenize import word_tokenize
#nltk.download('punkt')
text="tokenization using genai"
tokens=word_tokenize(text)
print("length of the tokens:",len(tokens))
print("num of token:",tokens)    