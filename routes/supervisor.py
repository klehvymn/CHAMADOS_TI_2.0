from flask import Blueprint, request, jsonify
from extensions import db
from models import Ticket

bp_supervisor = Blueprint('supervisor', __name__)

@bp_supervisor.route('/atribuir/<int:ticket_id>', methods=['POST'])
def atribuir_chamado(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    data = request.json
    
    ticket.tech_primary_id = data.get('tech_id')
    ticket.tech_secondary_id = data.get('aux_id')
    ticket.priority = data.get('priority')
    ticket.status = 'Atribuído'
    
    db.session.commit()
    return jsonify({"message": "Chamado atribuído com sucesso!"})
