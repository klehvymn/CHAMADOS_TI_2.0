import gspread
from oauth2client.service_account import ServiceAccountCredentials
from models import db, Ticket

def sync_google_forms():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)
    
    # Abre a planilha pelo link ou nome
    sheet = client.open_by_url('LINK_DA_SUA_PLANILHA_DE_RESPOSTAS').sheet1
    data = sheet.get_all_records()

    for row in data:
        # Verifica se o chamado já existe no banco para não duplicar
        exists = Ticket.query.filter_by(google_id=row['Carimbo de data/hora']).first()
        if not exists:
            novo_chamado = Ticket(
                google_id=row['Carimbo de data/hora'],
                client_name=row['Nome'],
                description=row['Descrição do Problema'],
                status='Aberto'
            )
            db.session.add(novo_chamado)
    db.session.commit()
