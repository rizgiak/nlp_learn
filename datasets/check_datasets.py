from datasets import load_dataset, get_dataset_split_names

dataset = load_dataset("rotten_tomatoes", split="train")
# get_dataset_split_names("rotten_tomatoes")
# ['train', 'validation', 'test']

print(dataset[0])