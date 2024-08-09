from flask import Blueprint, render_template, redirect, request, url_for, abort, jsonify
from Application.Services import AnotacaoService
from Domain.Entities.Anotacao import Anotacao

caderno_controller = Blueprint("main", __name__)

@caderno_controller.route("/Anotacao")
def index():
    return render_template("Caderno/index.html", anotacoes=AnotacaoService.GetAnotacaoByQtd(10))

@caderno_controller.route("/Anotacao/Create", methods=["GET", "POST"])
def Create():
    if request.method == "GET":
        return render_template("Caderno/Create.html", anotacoes=AnotacaoService.GetAnotacaoByQtd(10))
    elif request.method == "POST":
        titulo = request.form.get("titulo")
        anotacao = request.form.get("anotacao")

        AnotacaoService.Add(Anotacao( Titulo = titulo, Anotacao = anotacao ))
        return redirect(url_for('main.index'))
    
@caderno_controller.route("/Anotacao/Update/<int:id>", methods=["GET", "POST"])
def Update(id):
    if request.method == "GET":
        anotacao = AnotacaoService.GetAnotacaoById(id)
        if anotacao is None: abort(404)
        return render_template("Caderno/Update.html",
                               anotacoes=AnotacaoService.GetAnotacaoByQtd(10),
                               anotacao=anotacao)
    elif request.method == "POST":
        titulo = request.form.get("titulo")
        anotacao = request.form.get("anotacao")
        AnotacaoService.Update(Anotacao(Id=id,Titulo=titulo, Anotacao=anotacao))

        anotacao_atualizada = AnotacaoService.GetAnotacaoById(id)
        return redirect(url_for("main.Update", id=id))
    
@caderno_controller.route("/Anotacao/Delete", methods=["POST"])
def Delete():
    try:
        anotacao_id = request.form.get("AnotacaoId")
        AnotacaoService.Delete(anotacao_id)
        return redirect(url_for("main.index"))
    except:
        abort(500)