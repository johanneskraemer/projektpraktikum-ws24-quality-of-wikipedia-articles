"""Tokenizes the data

Authors: Emmanuelle Steenhof"""

def tokenizer_function(examples):
    """Is used to tokenize the articles"""
    return tokenizer(examples["text"], padding="max_length", truncation=True)


from datasets import load_dataset, concatenate_datasets

def tokenize_data(dataset_final, tokenizer_for_tokenization):
    global tokenizer
    tokenizer = tokenizer_for_tokenization
    """This function is used to tokenize the data"""
    tokenized_dataset = dataset_final.map(tokenizer_function, batched=True)
    tokenized_datasets = tokenized_dataset.remove_columns(["text"])
    tokenized_datasets.set_format("torch")
    return tokenized_datasets