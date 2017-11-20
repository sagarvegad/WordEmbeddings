# WordEmbeddings

There have been many methods which can be used to convert words to vectors. The major two types of methods are - frequency based vectorisation and prediction based vectorisation. Frequency based vectorisation includes “Co-occurrence matrix method”.

Co-occurence Matrix Method:
Analysing context of a word in a text is a very sensitive issue. However, getting help from the neighbours of that word has helped make progress in this field. This type of method involves a parameter termed as ‘Window-size’, which indicates the number of words that need to be looked at, on both left-hand side and right-hand side while calculating the vector for that word. If window-size is equal to 1, we shall consider one neighbour from both right and left side of the word during the vectorisation process. I  have   considered   a   window-size   of   value   1.


Above table can filled in the following manner. For each pair of words, we can count the number of their co-occurrences the sentence with respect to window-size mentioned. For example - for the pair - love and I, we can observe that in the above sentence, love and I appear two times together in the window-size of value 1. Hence, the cell representing   these   two   words   has   a   value   of   2.

To obtain an equivalent vector for a word, we select all the values in the column corresponding to that column. For example - vector for IRS would be - (0, 1, 0, 0, 0, 0, 1) and for   Physics   -   (0,   0,   0,   0,   1,   0,   1).

Similarity between these vectors can be evaluated by using cosine similarity.


Hence, the similarity between vector for IRS and ML is 100%. Similarly, similarity between vector for love and I is 0%.
