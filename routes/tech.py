from flask import Blueprint, request, jsonify
from extensions import db
from models import Ticket
from services.notifications import enviar_notificacao_cliente

bp_tech = Blueprint('tech', __name__)

@bp_tech.route('/encerrar/<int:ticket_id>', methods=['POST'])
def encerrar_chamado(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    data = request.json
    
    ticket.solution_report = data.get('report')
    ticket.status = 'Concluído'
    db.session.commit()
    
    enviar_notificacao_cliente(ticket)
    
    return jsonify({"message": "Chamado encerrado e cliente notificado."})
