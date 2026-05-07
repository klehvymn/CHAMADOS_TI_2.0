from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    role = db.Column(db.String(20)) # Gestor, Supervisor, Tecnico, Cliente
    phone = db.Column(db.String(20))

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    google_id = db.Column(db.String(50)) # ID vindo do formulário
    client_name = db.Column(db.String(100))
    description = db.Column(db.Text)
    status = db.Column(db.String(20), default='Aberto') # Aberto, Atribuído, Concluído
    priority = db.Column(db.String(20)) # Emergencial, Alta, Média, Baixa, Rotina
    
    tech_primary_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    tech_secondary_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    solution_report = db.Column(db.Text)
    rating = db.Column(db.Integer) # 1 a 5
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
