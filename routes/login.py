from flask import Blueprint,request,render_template
from database import conexao

login_bp = Blueprint('login', __name__)


@login_bp.route("/entrar", methods=["POST"])
def enviar():
    Usuario = request.form.get("usuario")
    Senha = request.form.get("senha")

    if not Usuario or not Senha:
        return render_template("cadastro.html", erro2 = "preencha este campo")

    conectar = conexao()
    cursor = conectar.cursor(dictionary=True)

    cursor.execute("SELECT senha FROM usuarios WHERE usuario = %s" , (Usuario,))
    resultado = cursor.fetchone()

    if not resultado:     
        return render_template("cadastro.html", erro2 = "Usuario não encontrado")
    
    if resultado['senha'] != Senha:
        return render_template("cadastro.html" , erro2 = "senha incorreta")
        
    conectar.close()
    return render_template("inicial.html")

