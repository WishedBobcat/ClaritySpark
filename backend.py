import os
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_clarity(topic):
    insights = {
        "Productivity": {
            "takeaway": "Focus on the 80/20 rule.",
            "why_matters": "Most results come from 20% of your efforts.",
            "how_to_apply": "Prioritize tasks that have the highest impact."
        },
        "Health": {
            "takeaway": "Sleep is the foundation of health.",
            "why_matters": "Poor sleep leads to stress and low energy.",
            "how_to_apply": "Aim for 7-9 hours of quality sleep daily."
        }
    }
    return insights.get(topic, {
        "takeaway": "No data available.",
        "why_matters": "Try a different topic.",
        "how_to_apply": "Expand your search."
    })

@app.route('/get_clarity', methods=['GET'])
def clarity_endpoint():
    topic = request.args.get('topic', '')
    clarity = get_clarity(topic)
    return jsonify({"topic": topic, **clarity})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use Render's assigned port or default to 5000
    app.run(host='0.0.0.0', port=port)
