# repairs.py
from flask import Blueprint, jsonify, request

repairs_bp = Blueprint('repairs', __name__)

# 模拟数据库
repairs_data = []

# 获取报修列表
@repairs_bp.route('/api/repairs', methods=['GET'])
def get_repairs():
    return jsonify(repairs_data)

# 提交报修表单
from datetime import datetime
from uuid import uuid4
@repairs_bp.route('/api/repairs', methods=['POST'])
def submit_repair():
    repair_data = request.json

    # 自动获取当前时间
    repair_data['Date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # 自动生成编号,SBBX-当前报修事件个数-UUID的前8位数
    repair_data['Num'] = f"SBBX-{len(repairs_data)+1:04}-{uuid4().hex[:8]}"

    # 为缺失的可选字段添加默认值
    repair_data.setdefault('Solution', '正在出勤')
    repair_data.setdefault('Stuff', '正在出勤')
    repair_data.setdefault('Consumables', '暂无')
    repair_data.setdefault('State', '审批中')

    # 验证提交的数据是否包含所需字段
    required_fields = ['Num', 'Date', 'Location', 'Description', 'Reporter', 'Phonenum']
    if not all(field in repair_data for field in required_fields):
        return jsonify({'error': 'Missing required field(s)'}), 400
    
    # 返回修改的数据
    repairs_data.append(repair_data)
    return jsonify(repair_data), 201
