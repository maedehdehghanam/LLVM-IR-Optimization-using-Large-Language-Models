import torch
from transformers import RobertaTokenizer, RobertaModel
from sklearn.metrics.pairwise import cosine_similarity

model_name = "microsoft/codebert-base"
tokenizer = RobertaTokenizer.from_pretrained(model_name)
model = RobertaModel.from_pretrained(model_name)


def read_ir_file(file_path):
    with open(file_path, "r") as file:
        return file.read()


def embed_code(code_snippet):
    inputs = tokenizer(code_snippet, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        embeddings = model(**inputs).last_hidden_state.mean(dim=1)
    return embeddings


def calculate_similarity(code1, code2):
    embedding1 = embed_code(code1)
    embedding2 = embed_code(code2)
    similarity = cosine_similarity(embedding1, embedding2)
    return similarity[0][0]


ir1 = read_ir_file(".ll")
ir2 = read_ir_file("code-llama.ll")

similarity_score = calculate_similarity(ir1, ir2)
print(f"Similarity Score: {similarity_score:.4f}")
