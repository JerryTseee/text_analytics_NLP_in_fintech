"""
Docstring for code_base.code-transformers-imdbThis code demonstrates fine-tuning 
a BERT-based model for sentiment analysis on the IMDb movie review dataset.
The code trains a DistilBERT model to classify movie reviews as positive or negative sentiment.
"""

import numpy as np
import evaluate
from transformers import (
    AutoTokenizer, 
    AutoModelForSequenceClassification, 
    TrainingArguments, 
    Trainer)
from datasets import load_dataset

bert_model = 'distilbert-base-uncased'

# Load the IMDb dataset.
dataset = load_dataset('imdb')
dataset['train'] = dataset['train'].select(range(1000))
dataset['test'] = dataset['test'].select(range(200))

tokenizer = AutoTokenizer.from_pretrained(bert_model)

def tokenize_function(example):
    return \
        tokenizer(
            example['text'],
            padding='max_length',
            truncation=True,
            max_length=32)
# Apply tokenization on `dataset` by applying the tokenization
# function to each element of `dataset`.
tokenized_datasets = \
    dataset.\
    map(
        tokenize_function,
        batched=True)

tokenized_datasets = \
    tokenized_datasets.\
    rename_column(
        'label',
        'labels')   # Necessary for comatibility with `Trainer` class.
tokenized_datasets.\
    set_format(
        'torch',
        columns=['input_ids', 'attention_mask', 'labels'])


model = \
    AutoModelForSequenceClassification.\
    from_pretrained(
        bert_model,
        num_labels=2)

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    accuracy = evaluate.load("accuracy")
    return accuracy.compute(predictions=predictions, references=labels)

# Initialize the `Trainer`, which is a training and eval loop for
trainer = \
    Trainer(
        model=model,
        args=TrainingArguments(
            output_dir='./data-NLP-teaching', # Can be deleted later.
            eval_strategy='epoch',
            per_device_train_batch_size=8, # batch size of 8
            per_device_eval_batch_size=8, # batch size of 8
            num_train_epochs=2, # two epochs
            weight_decay=0.01),
        train_dataset=tokenized_datasets['train'],
        eval_dataset=tokenized_datasets['test'],
        compute_metrics=compute_metrics)

# Train the model
print("Training the model...")
trainer.train()

# Evaluate the model.
print("Evaluating the model...")
results = trainer.evaluate()
print(results)
