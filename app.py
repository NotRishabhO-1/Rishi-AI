from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# --- CONFIGURATION ---
NVIDIA_API_KEY = "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" 
client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = NVIDIA_API_KEY
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    
    try:
        completion = client.chat.completions.create(
            model="microsoft/phi-3.5-mini-instruct",
            messages=[
                {"role": "system", "content": "You are Rishi AI, a brilliant, witty, and helpful mentor. Keep responses concise and engaging."},
                {"role": "user", "content": user_input}
            ],
            temperature=0.2,
            max_tokens=1024,
            stream=False # Stream False for easier initial setup
        )
        
        reply = completion.choices[0].message.content
        return jsonify({"reply": reply})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

