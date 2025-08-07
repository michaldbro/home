from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from do_api_gmap import attractions, get_place_coordinates, get_local_attractions, API_KEY

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Attraction.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# tabela
class Attraction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)

# łącze z index.html
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form.get('city', 'Kraków, Polska')
        try:
            # pob. atrakcje
            lat, lng = get_place_coordinates(city, API_KEY)
            attractions_list = get_local_attractions(lat, lng, API_KEY)
            
            # update atrakcji, szukanie czy jest w bazie jak nie to dodanie
            with app.app_context():
                db.create_all()
                existing = {(a.name, a.address) for a in Attraction.query.all()}
                new_entries = [
                    (name, address or "Brak adresu")
                    for name, address in attractions_list
                    if (name, address or "Brak adresu") not in existing
                ]
                
                for name, address in new_entries:
                    new_attraction = Attraction(name=name, address=address)
                    db.session.add(new_attraction)
                
                if new_entries:
                    db.session.commit()
            
            return render_template('index.html', attractions=attractions_list, city=city, message=f"Znaleziono {len(attractions_list)} atrakcji w {city}")
        except Exception as e:
            return render_template('index.html', error=f"Błąd: {e}", city=city)
    
    return render_template('index.html')

# pobieranie  z google maps api
attractions = attractions

# kreowanie tabeli
with app.app_context():
    db.create_all()

    # sprawdza name + adres w bazie
    existing = {(a.name, a.address) for a in Attraction.query.all()}

    # tworzy new entry dla atrakcji, ktore nie sa znalezione w bazie
    new_entries = [
        (name, address or "Brak adresu")
        for name, address in attractions
        if (name, address or "Brak adresu") not in existing
    ]

    # petla dodaje atrakcje jak nie ma ich w bazie - new_attraction
    for name, address in new_entries:
        new_attraction = Attraction(name=name, address=address)
        db.session.add(new_attraction)

    if new_entries:
        db.session.commit()
        print(f"Dodano {len(new_entries)} nowych atrakcji")
    else:
        print("Atrakcje znajdują się w bazie danych")

if __name__ == '__main__':
    app.run(debug=True)
