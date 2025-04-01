from flask import Blueprint, request, jsonify
from app.services.operadora_service import buscar_operadoras

operadoras_bp = Blueprint('operadoras', __name__)

@operadoras_bp.route('/operadoras-saude', methods=['GET'])
def get_operadoras():
    nome_fantasia = request.args.get('nome_fantasia', '')
    try:
        dados = buscar_operadoras(nome_fantasia)
        return jsonify(dados)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
