NEGATIVE_MARKERS = {"not", "never", "avoid", "cannot", "insufficient", "weak"}
POSITIVE_MARKERS = {"should", "can", "recommended", "use", "supports", "improves"}


def check_contradictions(chunks: list[dict]) -> dict:
    findings = []
    grouped: dict[str, list[str]] = {}
    for chunk in chunks:
        grouped.setdefault(chunk["source_id"], []).append(chunk["text"].lower())
    combined = " ".join(" ".join(values) for values in grouped.values())
    has_negative = any(marker in combined for marker in NEGATIVE_MARKERS)
    has_positive = any(marker in combined for marker in POSITIVE_MARKERS)
    if has_negative and has_positive:
        findings.append("Retrieved evidence contains both recommendation and caution language; final answer should include limitations.")
    if len(grouped) < 2:
        findings.append("Evidence comes from fewer than two documents; contradiction coverage is limited.")
    return {"contradictions_found": findings, "evidence_strength": "moderate" if len(chunks) >= 3 else "weak"}
