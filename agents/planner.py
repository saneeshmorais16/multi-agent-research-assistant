import re


def plan_research(question: str) -> dict:
    clean = question.strip().rstrip("?")
    focus_terms = [term for term in re.findall(r"\b[a-zA-Z][a-zA-Z/-]{2,}\b", clean.lower()) if term not in {"what", "when", "where", "which", "should", "could", "would", "with", "from", "how", "can", "the"}]
    sub_questions = [
        f"What evidence explains {clean}?",
        f"What risks or limitations relate to {clean}?",
        f"What implementation practices are relevant to {clean}?",
    ]
    if focus_terms:
        sub_questions.append(f"Which sources mention {', '.join(focus_terms[:4])}?")
    return {"question": question, "sub_questions": sub_questions[:4], "focus_terms": focus_terms[:8]}
