# app.py

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from app.routes.RewriteForm import bp as RewriteForm_bp
from app.routes.XiaohongshuGenerator import xiaohongshu_bp
from app.routes.repairs import repairs_bp
from app.routes.database import init_database
from app.routes.models import db
from app.routes.auth import auth_bp  # 新增导入语句

app = Flask(__name__)
CORS(app)

app.secret_key = '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'  # Replace 'your_secret_key' with a secure secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # 设置数据库URI
db.init_app(app)  # 初始化数据库

# 注册路由 Blueprint
app.register_blueprint(RewriteForm_bp)
app.register_blueprint(xiaohongshu_bp)
app.register_blueprint(repairs_bp)
app.register_blueprint(auth_bp, url_prefix='/auth')  # 新增注册蓝图语句

from app.routes.auth import auth_bp, create_default_users  # 导入语句
if __name__ == '__main__':
    with app.app_context():  # 确保在应用程序上下文中运行以下代码
        db.create_all()  # 创建所有数据库表
        create_default_users()  # 添加默认用户
        init_database()  # 初始化数据库
    app.run(host='0.0.0.0', port=5000)

