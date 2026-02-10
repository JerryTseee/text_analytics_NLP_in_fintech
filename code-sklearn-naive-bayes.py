# This script illustrates how to use the naive Bayes classifier from
import numpy as np
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics     # To evaluate model performance.

# Load the 20 Newsgroups dataset with 3 categories for demo purposes.
categories = ['comp.graphics', 'sci.space', 'rec.sport.baseball']
data = fetch_20newsgroups(
        subset='all',
        categories=categories, 
        remove=('headers', 'footers', 'quotes'))

X_text = data.data              # Raw text data.
y = data.target # Labels (0: comp.graphics, 1: rec.sport.baseball, 2: sci.space)


vectorizer = CountVectorizer(max_features=100) 
X = vectorizer.fit_transform(X_text) # Shape: (n_samples, n_features)

# Split up the data into training and testing.
count_train, count_test, y_train, y_test = \
    train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42)

nb = MultinomialNB()            # MultinomialNB(alpha=0.5)

nb.fit(count_train, y_train)
# Get the class labels.
nb.classes_
# Log-probability of features occurring, given a class (in this case
# the first class, i.e. the class having 0-th index).
nb.feature_log_prob_[0]
# Make predictions of the label for test data.
pred = nb.predict(count_test)

# Test the accuracy of the predictions.
accuracy = metrics.accuracy_score(y_test, pred)
print(f"\n1. Model Accuracy: {accuracy:.4f} ({accuracy*100:.2f}%)")
# The confusion matrix shows correct and incorrect labels.
conf_matrix = metrics.confusion_matrix(
        y_test,               # Actual labels.
        pred,                 # Labels predicted by naive Bayes model.
        labels=[0, 1, 2])     # Reorder the resulting matrix.
print("\n2. Confusion Matrix:")
print(conf_matrix)
