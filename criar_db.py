from app import create_app, db

app = create_app()

# Criar as tabelas no banco de dados
with app.app_context():
    db.create_all()
    print("✅ Banco de dados e tabelas criados com sucesso!")
