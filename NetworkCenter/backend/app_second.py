import openai
from flask import Flask, request, jsonify
from flask_cors import CORS
from langdetect import detect
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

app = Flask(__name__)
CORS(app)  # 允许跨域请求

openai.api_key = "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"

@app.route('/api/change_style', methods=['POST'])
def change_style():
    data = request.get_json()
    original_text = data.get('original_text')
    selected_style = data.get('style')

    # 请求改写风格
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"请将以下文字改写成{selected_style}风格：'{original_text}'"},
        ]
    )

    rewritten_text = completion.choices[0].message.content.strip()

    # 检查文本语言，如果是英文，则翻译成中文
    if detect(rewritten_text) == 'en':
        translation_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Translate the following text into Chinese：'{rewritten_text}'"},
            ]
        )


        translated_text = translation_completion.choices[0].message.content.strip()
        return jsonify({'changed_text': translated_text})
    else:
        return jsonify({'changed_text': rewritten_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)