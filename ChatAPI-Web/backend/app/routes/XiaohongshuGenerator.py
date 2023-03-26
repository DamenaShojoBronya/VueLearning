from flask import Blueprint, request, jsonify
import openai
import json

openai.api_key = "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"
# 创建一个蓝图对象
xiaohongshu_bp = Blueprint('xiaohongshu', __name__)

@xiaohongshu_bp.route('/api/xiaohongshu', methods=['POST'])
def generate_text():
    data = request.json
    input_text = data.get('input')

    if not input_text:
        return jsonify({'error': '请输入要夸奖的食物或产品名称'}), 400

    # 调用ChatGPT API的逻辑
    # print("input_text:",input_text)
    # response = openai.Completion.create(
    #     model="text-davinci-002",
    #     prompt=f"用小红书的笔记风格写一段夸奖{input_text}非常美味的文案，“小红书笔记风格”的重点是要使用Emoji表情，以及使用一些“女大学生词”，如:'绝绝子'。",
    #     temperature=0.9,
    #     max_tokens=2048,
    #     top_p=1,
    #     frequency_penalty=0,
    #     presence_penalty=0.6,
    #     stop=None
    # )
    
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "回答中要加入emoji表情"},
        {"role": "user", "content": f"用小红书的笔记风格写一段夸奖{input_text}非常美味的文案，“小红书笔记风格”的重点是要使用Emoji表情，以及使用一些“女大学生词”，如:'绝绝子'。"}
        ],
        temperature = 0.8,
    )
    print("completion:",completion)

    # 从返回结果中提取文本
    generated_text = completion.choices[0].message.content.strip()

    return jsonify({'generated_text': generated_text}), 200
