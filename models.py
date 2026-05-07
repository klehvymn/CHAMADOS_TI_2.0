from datetime import datetime
from extensions import db  # Importa a instância centralizada

class User(db.Model):
    __tablename__ = 'users' # Boa prática: definir nome da tabela explicitamente

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    role = db.Column(db.String(20)) # Gestor, Supervisor, Tecnico, Cliente
    phone = db.Column(db.String(20))

    # Relacionamentos (Opcional, mas ajuda muito em consultas)
    tickets_assigned = db.relationship('Ticket', foreign_keys='Ticket.tech_primary_id', backref='primary_tech')

    def __repr__(self):
        return f'<User {self.name}>'


class Ticket(db.Model):
    __tablename__ = 'tickets'

    id = db.Column(db.Integer, primary_key=True)
    google_id = db.Column(db.String(50)) 
    client_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(20), default='Aberto') 
    priority = db.Column(db.String(20)) 
    
    # Chaves Estrangeiras
    tech_primary_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    tech_secondary_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    solution_report = db.Column(db.Text)
    rating = db.Column(db.Integer) 
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Ticket {self.id} - {self.status}>'
