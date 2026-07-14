from retrieval.embeddings import tokenize


def evaluate_grounding(question: str, evidence_summaries: list[dict], final_text: str = "") -> dict:
    if not evidence_summaries:
        return {"grounding_score": 0.0, "confidence": "low", "feedback": ["No retrieved evidence was available."]}

    question_terms = set(tokenize(question))
    evidence_text = " ".join(item["summary"] for item in evidence_summaries)
    evidence_terms = set(tokenize(evidence_text))
    overlap = len(question_terms & evidence_terms) / max(len(question_terms), 1)
    citation_factor = min(len(evidence_summaries) / 2, 1)
    score = round((overlap * 0.65 + citation_factor * 0.35) * 100, 2)
    feedback = []
    if score < 45:
        feedback.append("Evidence overlap is weak; answer should state uncertainty.")
    if len(evidence_summaries) < 2:
        feedback.append("Use more than one source chunk when possible.")
    if final_text and "[" not in final_text:
        feedback.append("Final answer should include citations.")
    confidence = "high" if score >= 75 else "medium" if score >= 45 else "low"
    return {"grounding_score": score, "confidence": confidence, "feedback": feedback or ["Answer appears grounded in retrieved chunks."]}
