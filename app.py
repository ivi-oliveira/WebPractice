
from flask import Flask
from routes.login import login_bp
from routes.cadastro import cadastro_bp

app = Flask(__name__)

app.register_blueprint(login_bp)
app.register_blueprint(cadastro_bp)

app.run(host="0.0.0.0", port=5000, debug=True)



