# Cosine similarity. 
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Let's assume we have two documents that have been converted to the vectors
# following vectors, e.g. by bag-of-words (BoW), tf-idf, or other
# means (potentially followed by dimensionality reduction such as
# SVD).
docA = np.array([9, 4, 8, 2, 7, 5, 0])
docB = np.array([0, 1, 2, 7, 0, 4, 4])

# We can now "manually" compute the cosine similarity. In the first
# example we compute the norm "by hand" whereas in the second example
# we use the `norm` function from numpy.
result1 = np.dot(docA, docB) / (np.sqrt(np.sum(docA ** 2)) * np.sqrt(np.sum(docB ** 2)))
result2 = np.dot(docA, docB) / (np.linalg.norm(docA) * np.linalg.norm(docB))


# Alternatively we can use the function `cosine_similarity` from the
# scikit-learn (sklearn) package. It has the advantage that it can be
# applied to two or more vectors at once and can compute the cosine
# similarity between all vector pairs.
result3 = cosine_similarity(np.vstack((docA, docB)))

print("result1: ", result1)
print("result2: ", result2)
print("result3: ", result3[0][1])