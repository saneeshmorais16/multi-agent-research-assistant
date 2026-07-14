const questionInput = document.getElementById("question");
const answerOutput = document.getElementById("answerOutput");
const traceOutput = document.getElementById("traceOutput");

document.getElementById("runResearch").addEventListener("click", async () => {
  answerOutput.textContent = "Running multi-agent workflow...";
  traceOutput.innerHTML = "";
  const response = await fetch("/research", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question: questionInput.value })
  });
  const data = await response.json();
  answerOutput.textContent = JSON.stringify({
    direct_answer: data.direct_answer,
    grounding_score: data.grounding_score,
    confidence: data.confidence,
    citations: data.citations,
    uncertainty_notes: data.uncertainty_notes
  }, null, 2);
  data.agent_trace.forEach((step) => {
    const wrapper = document.createElement("div");
    wrapper.className = "trace-step";
    wrapper.innerHTML = `<strong>${step.agent}</strong><pre>${JSON.stringify(step.output, null, 2)}</pre>`;
    traceOutput.appendChild(wrapper);
  });
});
