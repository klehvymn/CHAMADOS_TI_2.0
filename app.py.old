from flask import Flask, request, jsonify, render_template
from models import db, Ticket, User
import smtplib # Para envio de e-mail

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///helpdesk.db'
db.init_app(app)

# --- MÓDULO 2: ATRIBUIÇÃO (SUPERVISOR) ---
@app.route('/atribuir/<int:ticket_id>', methods=['POST'])
def atribuir_chamado(ticket_id):
    ticket = Ticket.query.get(ticket_id)
    data = request.json
    
    ticket.tech_primary_id = data.get('tech_id')
    ticket.tech_secondary_id = data.get('aux_id') # Opcional
    ticket.priority = data.get('priority') # Emergencial, Alta, etc.
    ticket.status = 'Atribuído'
    
    db.session.commit()
    return jsonify({"message": "Chamado atribuído com sucesso!"})

# --- MÓDULO 3: ENCERRAMENTO (TÉCNICO) ---
@app.route('/encerrar/<int:ticket_id>', methods=['POST'])
def encerrar_chamado(ticket_id):
    ticket = Ticket.query.get(ticket_id)
    data = request.json
    
    ticket.solution_report = data.get('report')
    ticket.status = 'Concluído'
    db.session.commit()
    
    # Simulação de envio de notificação
    enviar_notificacao_cliente(ticket)
    
    return jsonify({"message": "Chamado encerrado e cliente notificado."})

def enviar_notificacao_cliente(ticket):
    # Lógica para enviar E-mail ou integração com API de WhatsApp (ex: Twilio)
    print(f"Enviando e-mail para o cliente do chamado {ticket.id}...")
    print(f"Olá, seu chamado foi resolvido: {ticket.solution_report}")
    print("Por favor, avalie nosso serviço de 1 a 5 estrelas: http://seu-sistema.com/avaliar")

# --- MÓDULO 4: MANUTENÇÃO (ADMIN) ---
@app.route('/admin/usuario', methods=['POST'])
def criar_usuario():
    data = request.json
    novo_user = User(
        name=data['name'],
        email=data['email'],
        role=data['role'], # Técnico, Supervisor, Gestor
        phone=data['phone']
    )
    db.session.add(novo_user)
    db.session.commit()
    return jsonify({"message": "Usuário criado!"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all() # Cria o banco na primeira execução
    app.run(debug=True)
