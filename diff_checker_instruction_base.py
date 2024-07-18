import re
def read_ir_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def tokenize_ir(ir_content):
    return set(re.findall(r'\b\w+\b', ir_content))

def compute_jaccard_similarity(set1, set2):
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection) / len(union)

ir1 = read_ir_file('out.ll')
ir2 = read_ir_file('code-llama.ll')

tokenized_ir1 = (tokenize_ir(ir1))
tokenized_ir2 =(tokenize_ir(ir2))

similarity = compute_jaccard_similarity(tokenized_ir1, tokenized_ir2)

print(f"Cosine Similarity: {similarity:.4f}")