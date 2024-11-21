from flask import Blueprint, jsonify, request
from models import atividade_model
from clients.pessoa_service_client import PessoaServiceClient


atividade_bp = Blueprint('atividade_bp', __name__)


@atividade_bp.route('/', methods=['GET'])
def listar_atividades():
    atividades = atividade_model.listar_atividades()
    return jsonify(atividades)


@atividade_bp.route('/<int:id_atividade>', methods=['GET'])
def obter_atividade(id_atividade):
    try:
        atividade = atividade_model.obter_atividade(id_atividade)
        return jsonify(atividade)
    except atividade_model.AtividadeNotFound:
        return jsonify({'erro': 'Atividade não encontrada'}), 404


@atividade_bp.route('/<int:id_atividade>/professor/<int:id_professor>', methods=['GET'])
def obter_atividade_para_professor(id_atividade, id_professor):
    try:
        atividade = atividade_model.obter_atividade(id_atividade)
        if not PessoaServiceClient.verificar_leciona(id_professor, atividade['id_disciplina']):
            atividade = atividade.copy()
            atividade.pop('respostas', None)
        return jsonify(atividade)
    except atividade_model.AtividadeNotFound:
        return jsonify({'erro': 'Atividade não encontrada'}), 404

@atividade_bp.route("/", methods=["POST"])
def criar_atividade():
    dict = request.json
    dict['id_atividade'] = int (dict['id_atividade'])
    atividade_model.criar_atividade(dict)
    atividades = atividade_model.listar_atividades()
    return jsonify(atividades)

@atividade_bp.route("/<int:id_atividade>/", methods=["PUT"])
def atualizar_atividade(id_atividade):
    dict = request.json
    atividade_model.atualizar_atividade(id_atividade, dict)
    atividades = atividade_model.listar_atividades()
    return jsonify(atividades)

@atividade_bp.route("/<int:id_atividade>/", methods=["DELETE"])
def deletar_atividade(id_atividade):
    try:
        atividade_model.excluir_atividade(id_atividade)
        return 'Atividade excluida com sucesso!', 204
    except atividade_model.AtividadeNotFound:
        return jsonify({'message': 'Atividade não encontrada'}), 404