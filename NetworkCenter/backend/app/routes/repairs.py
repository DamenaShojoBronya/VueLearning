# repairs.py
from flask import Blueprint, jsonify, request

repairs_bp = Blueprint('repairs', __name__)

# 模拟数据库
repairs_data = []

# 获取报修列表
from app.routes.database import create_connection
@repairs_bp.route('/api/repairs', methods=['GET'])
def get_repairs():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM repairs")
    rows = cur.fetchall()

    repairs_data = [dict(zip([column[0] for column in cur.description], row)) for row in rows]

    return jsonify(repairs_data)

# 改变流程的状态State，分别绑定两个按钮 后续再优化
@repairs_bp.route('/api/repairs/<string:num>/approve', methods=['PUT'])
def approve_repair(num):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("UPDATE repairs SET State=? WHERE Num=?", (request.json['state'], num))
    conn.commit()

    if cur.rowcount == 1:
        return jsonify({"message": "Approve Repair successfully updated"})
    else:
        return jsonify({'error': 'Approve Repair not found'}), 404

@repairs_bp.route('/api/repairs/<string:num>/reject', methods=['PUT'])
def reject_repair(num):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("UPDATE repairs SET State=? WHERE Num=?", (request.json['state'], num))
    conn.commit()

    if cur.rowcount == 1:
        return jsonify({"message": "Reject Repair successfully updated"})
    else:
        return jsonify({'error': 'Reject Repair not found'}), 404

# 更新维修条目信息,判断移到前端去做
@repairs_bp.route('/api/repairs/<string:num>/update', methods=['PUT'])
def update_repair(num):
    conn = create_connection()
    cur = conn.cursor()
    update_fields = ['Solution', 'Stuff', 'Consumables', 'State']
    data = {field: request.json[field] for field in update_fields if field in request.json}

    if not data:
        return jsonify({'error': 'No valid fields to update'}), 400

    query = "UPDATE repairs SET " + ", ".join(f"{field}=?" for field in data.keys()) + " WHERE Num=?"
    params = tuple(data[field] for field in data.keys()) + (num,)
    cur.execute(query, params)
    conn.commit()

    if cur.rowcount == 1:
        return jsonify({"message": "Repair successfully updated"})
    else:
        return jsonify({'error': 'Repair not found'}), 404

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
    # 连接数据库
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO repairs (Num, Date, Location, Description, Reporter, Phonenum, Solution, Stuff, Consumables, State)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (repair_data['Num'], repair_data['Date'], repair_data['Location'], repair_data['Description'], repair_data['Reporter'], repair_data['Phonenum'], repair_data['Solution'], repair_data['Stuff'], repair_data['Consumables'], repair_data['State']))
    conn.commit()

    return jsonify(repair_data), 201

 