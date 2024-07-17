import difflib
import tokenize
from io import BytesIO

def tokenize_code(code):
    tokens = []
    code_bytes = code.encode('utf-8')
    token_generator = tokenize.tokenize(BytesIO(code_bytes).readline)
    
    for token in token_generator:
        if token.type in [tokenize.COMMENT, tokenize.NL, tokenize.NEWLINE, tokenize.INDENT, tokenize.DEDENT, tokenize.ENDMARKER]:
            continue
        tokens.append(token.string)
    
    return tokens

def calculate_similarity(tokens1, tokens2):

    sequence_matcher = difflib.SequenceMatcher(a=tokens1, b=tokens2)
    return sequence_matcher.ratio()

def compare_code_snippets(code1, code2):
    tokens1 = tokenize_code(code1)
    tokens2 = tokenize_code(code2)
    similarity = calculate_similarity(tokens1, tokens2)
    return similarity

# Example code snippets
code_snippet_1 = """
HI
"""

code_snippet_2 = """
HI its
"""

# Compare the code snippets
similarity_score = compare_code_snippets(code_snippet_1, code_snippet_2)
print(f"Similarity score: {similarity_score:.2f}")