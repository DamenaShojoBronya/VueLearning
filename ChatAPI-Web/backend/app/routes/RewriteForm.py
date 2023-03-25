from flask import Blueprint, request, jsonify
from langdetect import detect
import openai

openai.api_key = "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"

# 创建一个 Blueprint 对象，用于定义路由
bp = Blueprint('rewrite', __name__)

# 定义路由函数
@bp.route('/api/change_style', methods=['POST'])
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
