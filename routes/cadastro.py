from flask import Blueprint, request, render_template
from database import conexao

cadastro_bp = Blueprint('cadastro' , __name__)

@cadastro_bp.route("/")
def home():
    return render_template("cadastro.html")

@cadastro_bp.route("/enviar", methods=["POST"])
def enviar():
    Usuario = request.form.get("usuario")
    Idade = request.form.get("idade")
    Senha = request.form.get("senha")

    if not Usuario or not Senha or not Idade:
        return render_template("cadastro.html", erro = "preencha este campo")

    conectar = conexao()
    cursor = conectar.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE usuario = %s" , (Usuario,))
    existe = cursor.fetchone()

    if existe:       
        return render_template("cadastro.html", erro = "usuario existente")

    comando = "INSERT INTO usuarios (usuario, senha, idade) VALUES (%s, %s,%s)"
    dados = (str(Usuario), str(Senha), str(Idade))
    cursor.execute(comando,dados)

    conectar.commit()
    
    return render_template("inicial.html")


