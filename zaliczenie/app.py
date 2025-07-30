from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from do_api_gmap import attractions

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Attraction.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Definicja modelu
class Attraction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)


# Pobieranie atrakcji z API
attractions = attractions

# Dodawanie atrakcji do bazy danych
with app.app_context():
    db.create_all()
    # Sprawdź czy atrakcje już istnieją
    existing_attractions = Attraction.query.all()
    if not existing_attractions:
        for name, address in attractions:
            new_attraction = Attraction(name=name, address=address or "Brak adresu")
            db.session.add(new_attraction)
        db.session.commit()
        print(f"Dodano {len(attractions)} atrakcji do bazy danych")
    else:
        print("Atrakcje już istnieją w bazie danych")

if __name__ == '__main__':
    app.run(debug=True)
