from flask import Flask
from flask_cors import CORS
from app.routes.RewriteForm import bp as RewriteForm_bp

app = Flask(__name__)
CORS(app)

# 注册路由 Blueprint
app.register_blueprint(RewriteForm_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
