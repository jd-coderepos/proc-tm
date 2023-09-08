from rouge_score import rouge_scorer

def read_files_into_list(filenames):
    """
    Read the contents of multiple files into a list.

    Parameters:
    - filenames (list): List of file paths to be read.

    Returns:
    - List of strings where each string is the content of a file.
    """
    contents = []
    for filename in filenames:
        with open(filename, 'r', encoding="utf8") as file:
            contents.append(file.read())
    return contents

# Example usage:
filenames = ["./agriculture/type1 - list prompts/ontology/"+"goldstd-response-example4.txt"]
references = read_files_into_list(filenames)

filenames = ["./agriculture/type1 - list prompts/ontology+2shot/"+"chatgpt-response.txt"]
predictions = read_files_into_list(filenames)

scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL', 'rougeLsum'])

cumulative_scores = {
    'rouge1': {'precision': 0, 'recall': 0, 'fmeasure': 0},
    'rouge2': {'precision': 0, 'recall': 0, 'fmeasure': 0},
    'rougeL': {'precision': 0, 'recall': 0, 'fmeasure': 0},
    'rougeLsum': {'precision': 0, 'recall': 0, 'fmeasure': 0}
}

# Calculate ROUGE scores and accumulate
num_samples = len(predictions)
for prediction, reference in zip(predictions, references):
    scores = scorer.score(reference, prediction)
    for metric, values in scores.items():
        cumulative_scores[metric]['precision'] += values.precision
        cumulative_scores[metric]['recall'] += values.recall
        cumulative_scores[metric]['fmeasure'] += values.fmeasure

# Average the scores
for metric, values in cumulative_scores.items():
    cumulative_scores[metric]['precision'] /= num_samples
    cumulative_scores[metric]['recall'] /= num_samples
    cumulative_scores[metric]['fmeasure'] /= num_samples

print(cumulative_scores)

