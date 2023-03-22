from flask import Flask
app = Flask(__name__)

from flask import request, jsonify
import openai

openai.api_key = "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"

@app.route('/rewrite', methods=['POST'])
def rewrite_article():
    original_text = request.form['text']
    prompt = f"请将以下文章进行改写：\n\n{original_text}\n\n改写后的文章："

    response = openai.Completion.create(
        engine="text-davinci-002",  # 根据需求选择引擎
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    rewritten_text = response.choices[0].text.strip()
    return jsonify({"rewritten_text": rewritten_text})

if __name__ == '__main__':
    app.run(debug=True)
