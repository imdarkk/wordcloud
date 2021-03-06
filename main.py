import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys
import re

def _upload():
    filename = "words.txt"
    global file_contents
    with open(filename) as f:
        content = f.readlines()
        file_contents = content

_upload()

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    words = {}
    for word in file_contents:
        if word in uninteresting_words:
            pass
        else:
            if word.isalpha():
                if word.lower() in words:
                    words[word.lower()] += 1
                elif word.lower() not in words:
                    words[word.lower()] = 1
            else:
                stripped = re.sub(r'\W+', '', word)
                stripped = stripped.lower()
                if stripped.lower() in words:
                    words[stripped.lower()] += 1
                else:
                    words[stripped.lower()] = 1
                
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(words)
    return cloud.to_array()

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()