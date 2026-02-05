# The Hugging Face `datasets` library provides access to a wide range
# of real-world datasets. Here's a quick example of how to explore and
# use a dataset. The AG News dataset, also known as "AG's News
# Corpus," is a widely used benchmark dataset for text classification
# tasks. It is constructed from news articles and focuses on four main
# categories: World, Sports, Business, and Science/Technology.

# Import the `load_dataset` function that loads a dataset from the
# Hugging Face Hub, or a local dataset. For details type
# `help(load_dataset)` after the import.
from datasets import load_dataset # need to pip install datasets

dataset = load_dataset('ag_news')
print("Dataset loaded successfully.")
print(dataset)

# Access the first training example. You can see it has a text and an
# integer label representing the news category.
print("First training example:")
print(dataset['train'][0])

# Show the category label and text content of the first seven news
# articles.
label_names = dataset['train'].features['label'].names
for example in dataset['train'].select(range(0, 7)):
    label = label_names[example['label']]
    text = example['text']
    print(f'Category: {label}\nText: {text}\n')
