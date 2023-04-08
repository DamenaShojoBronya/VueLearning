# app.py
from flask import Flask
from flask_cors import CORS
from app.routes.RewriteForm import bp as RewriteForm_bp
from app.routes.XiaohongshuGenerator import xiaohongshu_bp  # 新增导入语句
from app.routes.repairs import repairs_bp
from app.routes.database import init_database

app = Flask(__name__)
CORS(app)

# 注册路由 Blueprint
app.register_blueprint(RewriteForm_bp)
app.register_blueprint(xiaohongshu_bp)  # 新增注册蓝图语句
app.register_blueprint(repairs_bp)

if __name__ == '__main__':
    init_database()  # 初始化数据库
    app.run(host='0.0.0.0', port=5000)
