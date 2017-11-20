
# coding: utf-8

#Implementing Co-occurence method
sentence = "I love IRS . I love ML . I hate Physics ."
#creating dictionary for the above sentence

dict = {}
for word in sentence.split():
    if dict.has_key(word):
        dict[word]+=1
    else:
        dict[word]=1

print dict

#dimension of co-occurence matrix
dimen = len(dict.keys())
print "Dimension of co-occurence matrix is ",dimen,"x",dimen

mat = [[0 for i in range(dimen)] for j in range(dimen)]

print mat

cols = dict.keys()
print cols

hash_pos = {}
pos = 0
for term in cols:
    hash_pos[term] = pos
    pos = pos+1
print hash_pos

sentence = sentence.split()

#setting window-size = 1
window_size = 1
for i in range(len(sentence)-1):
    if i!=0 and i!=len(sentence) - 1:
        #print sentence[i-window_size], sentence[i], sentence[i+window_size]
        #print mat
        mat[hash_pos[sentence[i]]][hash_pos[sentence[i-window_size]]] += 1
        mat[hash_pos[sentence[i]]][hash_pos[sentence[i+window_size]]] += 1

print mat

#printing vectors for all words
i = 0
for vector_word in mat:
    print cols[i], vector_word
    i+=1


