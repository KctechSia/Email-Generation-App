async function generateEmail() {
  const prompt = document.getElementById("promptInput").value;
  const leaveType = document.getElementById("leaveType").value;

  const response = await fetch("/generate", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ type: leaveType, prompt: prompt })
  });

  const data = await response.json();
  document.getElementById("outputArea").textContent = data.generated_email;
}
