import hashlib
import math
import re


def tokenize(text: str) -> list[str]:
    return re.findall(r"\b[a-z0-9][a-z0-9/-]*\b", text.lower())


def embed_text(text: str, dimensions: int = 256) -> list[float]:
    vector = [0.0] * dimensions
    for token in tokenize(text):
        digest = hashlib.sha256(token.encode("utf-8")).hexdigest()
        index = int(digest[:8], 16) % dimensions
        vector[index] += 1.0
    norm = math.sqrt(sum(value * value for value in vector)) or 1.0
    return [value / norm for value in vector]


def cosine_similarity(left: list[float], right: list[float]) -> float:
    return sum(a * b for a, b in zip(left, right))
