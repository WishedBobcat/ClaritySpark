async function generateClarity() {
    const topic = document.getElementById('topicInput').value;
    if (!topic) {
        alert('Please enter a topic!');
        return;
    }

    const response = await fetch('http://127.0.0.1:5000/get_clarity?topic=' + encodeURIComponent(topic));
    const data = await response.json();

    document.getElementById('output').innerHTML = `
        <h2>${data.topic}</h2>
        <p><strong>Key Takeaway:</strong> ${data.takeaway}</p>
        <p><strong>Why It Matters:</strong> ${data.why_matters}</p>
        <p><strong>How to Apply:</strong> ${data.how_to_apply}</p>
    `;
}