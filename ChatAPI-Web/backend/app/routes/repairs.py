# repairs.py
from flask import Blueprint, jsonify, request

repairs_bp = Blueprint('repairs', __name__)

# 模拟数据库
repairs_data = []

# 获取报修列表
@repairs_bp.route('/api/repairs', methods=['GET'])
def get_repairs():
    return jsonify(repairs_data)

# 改变流程的状态State，分别绑定两个按钮 后续再优化
@repairs_bp.route('/api/repairs/<string:num>/approve', methods=['PUT'])
def approve_repair(num):
    for repair in repairs_data:
        if repair['Num'] == num:
            repair['State'] = request.json['state']
            return jsonify(repair)
    return jsonify({'error': 'Approve Repair not found'}), 404

@repairs_bp.route('/api/repairs/<string:num>/reject', methods=['PUT'])
def reject_repair(num):
    for repair in repairs_data:
        if repair['Num'] == num:
            repair['State'] = request.json['state']
            return jsonify(repair)
    return jsonify({'error': 'Reject Repair not found'}), 404

# 更新维修条目信息
@repairs_bp.route('/api/repairs/<string:num>/update', methods=['PUT'])
def update_repair(num):
    # 查找对应的维修条目
    repair = next((r for r in repairs_data if r['Num'] == num), None)
    if repair is None:
        return jsonify({'error': 'Repair not found'}), 404

    # 更新维修条目的相关字段
    update_fields = ['Solution', 'Stuff', 'Consumables']
    for field in update_fields:
        if field in request.json:
            repair[field] = request.json[field]

    return jsonify(repair)


# 提交报修表单
from datetime import datetime
from uuid import uuid4
@repairs_bp.route('/api/repairs', methods=['POST'])
def submit_repair():
    repair_data = request.json
    # 在控制台输出收到的字段
    print("Received repair_data1:", repair_data)

    # 自动获取当前时间
    repair_data['Date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # 自动生成编号,SBBX/SBBX-当前报修事件个数-UUID的前8位数
    if repair_data['Description'] == '开报告厅，调字幕':
        repair_data['Num'] = f"SBGT-{len(repairs_data)+1:04}-{uuid4().hex[:8]}"
    else:
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
    
    # 在控制台输出的字段
    print("Received repair_data2:", repair_data)
    # 返回修改的数据
    repairs_data.append(repair_data)
    return jsonify(repair_data), 201

 