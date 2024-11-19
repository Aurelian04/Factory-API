from flask import Flask, jsonify, request

app = Flask(__name__)

materials = [

    {"id": 1, "name": "Otel", "price": 700, "currency": "USD", "unit": "kg"},
    {"id": 2, "name": "Cupru", "price": 9300, "currency": "USD", "unit": "kg"},
    {"id": 3, "name": "Lemn", "price": 150, "currency": "USD", "unit": "kg"},
    {"id": 4, "name": "Aluminiu", "price": 2500, "currency": "USD", "unit": "kg"},
    {"id": 5, "name": "Aur", "price": 58000, "currency": "USD", "unit": "kg"},
    {"id": 6, "name": "Argint", "price": 800, "currency": "USD", "unit": "kg"},
    {"id": 7, "name": "Plumb", "price": 250, "currency": "USD", "unit": "kg"},
    {"id": 8, "name": "Zinc", "price": 2500, "currency": "USD", "unit": "kg"},
    {"id": 9, "name": "Titan", "price": 4500, "currency": "USD", "unit": "kg"},
    {"id": 10, "name": "Nickel", "price": 20000, "currency": "USD", "unit": "kg"},
    {"id": 11, "name": "Litiu", "price": 12000, "currency": "USD", "unit": "kg"},
    {"id": 12, "name": "Gaur", "price": 800, "currency": "USD", "unit": "kg"},
    {"id": 13, "name": "Plexiglas", "price": 2500, "currency": "USD", "unit": "kg"},
    {"id": 14, "name": "Polietilena", "price": 1500, "currency": "USD", "unit": "kg"},
    {"id": 15, "name": "PVC", "price": 1000, "currency": "USD", "unit": "kg"},
    {"id": 16, "name": "Guma", "price": 1200, "currency": "USD", "unit": "kg"},
    {"id": 17, "name": "Silicon", "price": 15000, "currency": "USD", "unit": "kg"},
    {"id": 18, "name": "Carbune activ", "price": 3000, "currency": "USD", "unit": "kg"},
    {"id": 19, "name": "Cobalt", "price": 35000, "currency": "USD", "unit": "kg"},
    {"id": 20, "name": "Vanadiu", "price": 10000, "currency": "USD", "unit": "kg"},
    {"id": 21, "name": "Bismut", "price": 4200, "currency": "USD", "unit": "kg"},
    {"id": 22, "name": "Magnesiu", "price": 3600, "currency": "USD", "unit": "kg"},
    {"id": 23, "name": "Indiu", "price": 6000, "currency": "USD", "unit": "kg"},
    {"id": 24, "name": "Gadoliniu", "price": 2400, "currency": "USD", "unit": "kg"},
    {"id": 25, "name": "Terbiu", "price": 11000, "currency": "USD", "unit": "kg"},
    {"id": 26, "name": "Ceriu", "price": 45000, "currency": "USD", "unit": "kg"},
    {"id": 27, "name": "Eritiu", "price": 54000, "currency": "USD", "unit": "kg"},
    {"id": 28, "name": "Dizavantaj", "price": 12000, "currency": "USD", "unit": "kg"},
    {"id": 29, "name": "Staniu", "price": 9800, "currency": "USD", "unit": "kg"},
    {"id": 30, "name": "Rutheniu", "price": 7800, "currency": "USD", "unit": "kg"},
    {"id": 31, "name": "Ruteniu", "price": 50000, "currency": "USD", "unit": "kg"},
    {"id": 32, "name": "Iridiu", "price": 120000, "currency": "USD", "unit": "kg"},
    {"id": 33, "name": "Platină", "price": 54000, "currency": "USD", "unit": "kg"},
    {"id": 34, "name": "Palladium", "price": 45000, "currency": "USD", "unit": "kg"},
    {"id": 35, "name": "Rhodiu", "price": 60000, "currency": "USD", "unit": "kg"},
    {"id": 36, "name": "Tantal", "price": 180000, "currency": "USD", "unit": "kg"},
    {"id": 37, "name": "Diamant", "price": 350000, "currency": "USD", "unit": "kg"},
    {"id": 38, "name": "Vitamini", "price": 24000, "currency": "USD", "unit": "kg"},
    {"id": 39, "name": "Zahăr", "price": 450, "currency": "USD", "unit": "kg"},
    {"id": 40, "name": "Sare", "price": 200, "currency": "USD", "unit": "kg"},
    {"id": 41, "name": "Făină", "price": 400, "currency": "USD", "unit": "kg"},
    {"id": 42, "name": "Fructe", "price": 300, "currency": "USD", "unit": "kg"},
    {"id": 43, "name": "Legume", "price": 350, "currency": "USD", "unit": "kg"},
    {"id": 44, "name": "Lapte", "price": 700, "currency": "USD", "unit": "kg"},
    {"id": 45, "name": "Brânză", "price": 1200, "currency": "USD", "unit": "kg"},
    {"id": 46, "name": "Carne", "price": 800, "currency": "USD", "unit": "kg"},
    {"id": 47, "name": "Ouă", "price": 200, "currency": "USD", "unit": "kg"},
    {"id": 48, "name": "Lână", "price": 1500, "currency": "USD", "unit": "kg"},
    {"id": 49, "name": "Catifea", "price": 3000, "currency": "USD", "unit": "kg"},
    {"id": 50, "name": "Satin", "price": 3500, "currency": "USD", "unit": "kg"},
    {"id": 51, "name": "Lână Merino", "price": 2200, "currency": "USD", "unit": "kg"},
    {"id": 52, "name": "Matase", "price": 6000, "currency": "USD", "unit": "kg"},
    {"id": 53, "name": "Bumbac", "price": 900, "currency": "USD", "unit": "kg"},
    {"id": 54, "name": "Păpușoi", "price": 550, "currency": "USD", "unit": "kg"},
    {"id": 55, "name": "Hârtie", "price": 200, "currency": "USD", "unit": "kg"},
    {"id": 56, "name": "Ciment", "price": 120, "currency": "USD", "unit": "kg"},
    {"id": 57, "name": "Caramida", "price": 450, "currency": "USD", "unit": "kg"},
    {"id": 58, "name": "Piatră", "price": 350, "currency": "USD", "unit": "kg"},
    {"id": 59, "name": "Marmură", "price": 5000, "currency": "USD", "unit": "kg"},
    {"id": 60, "name": "Gips", "price": 400, "currency": "USD", "unit": "kg"},
    {"id": 61, "name": "Vată de sticlă", "price": 3000, "currency": "USD", "unit": "kg"},
    {"id": 62, "name": "Fibra de carbon", "price": 20000, "currency": "USD", "unit": "kg"},
    {"id": 63, "name": "Plexiglas", "price": 12000, "currency": "USD", "unit": "kg"},
    {"id": 64, "name": "Fibra de sticlă", "price": 3000, "currency": "USD", "unit": "kg"},
    {"id": 65, "name": "Laminat", "price": 1800, "currency": "USD", "unit": "kg"},
    {"id": 66, "name": "Cauciuc", "price": 1600, "currency": "USD", "unit": "kg"},
    {"id": 67, "name": "Laiton", "price": 4500, "currency": "USD", "unit": "kg"},
    {"id": 68, "name": "Bronz", "price": 6000, "currency": "USD", "unit": "kg"},
    {"id": 69, "name": "Aliaje", "price": 3500, "currency": "USD", "unit": "kg"},
    {"id": 70, "name": "Negru de fum", "price": 3000, "currency": "USD", "unit": "kg"},
    {"id": 71, "name": "Amestecuri de metal", "price": 5000, "currency": "USD", "unit": "kg"},
    {"id": 72, "name": "Îngrășăminte", "price": 1500, "currency": "USD", "unit": "kg"},
    {"id": 73, "name": "Cărbune", "price": 200, "currency": "USD", "unit": "kg"},
    {"id": 74, "name": "Lemn de esență tare", "price": 2000, "currency": "USD", "unit": "kg"},
    {"id": 75, "name": "Lemn de esență moale", "price": 800, "currency": "USD", "unit": "kg"},
    {"id": 76, "name": "Rășină epoxidică", "price": 3000, "currency": "USD", "unit": "kg"},
    {"id": 77, "name": "Gel de silicon", "price": 1000, "currency": "USD", "unit": "kg"},
    {"id": 78, "name": "Lime de calcar", "price": 1500, "currency": "USD", "unit": "kg"},
    {"id": 79, "name": "Piatra ponce", "price": 1800, "currency": "USD", "unit": "kg"},
    {"id": 80, "name": "Glas", "price": 1000, "currency": "USD", "unit": "kg"},
    {"id": 81, "name": "Chihlimbar", "price": 12000, "currency": "USD", "unit": "kg"},
    {"id": 82, "name": "Aditivi pentru plastic", "price": 2500, "currency": "USD", "unit": "kg"},
    {"id": 83, "name": "Metale rare", "price": 100000, "currency": "USD", "unit": "kg"},
    {"id": 84, "name": "Plastice reciclate", "price": 500, "currency": "USD", "unit": "kg"},
    {"id": 85, "name": "Piele", "price": 3500, "currency": "USD", "unit": "kg"},
    {"id": 86, "name": "Poliester", "price": 1000, "currency": "USD", "unit": "kg"},
    {"id": 87, "name": "Cărbune activ", "price": 7000, "currency": "USD", "unit": "kg"},
    {"id": 88, "name": "Alge", "price": 4000, "currency": "USD", "unit": "kg"},
    {"id": 89, "name": "Perle", "price": 5000, "currency": "USD", "unit": "kg"},
    {"id": 90, "name": "Gălbenuș de ou", "price": 400, "currency": "USD", "unit": "kg"},
    {"id": 91, "name": "Glicerină", "price": 1000, "currency": "USD", "unit": "kg"},
    {"id": 92, "name": "Supralină", "price": 800, "currency": "USD", "unit": "kg"},
    {"id": 93, "name": "Acid citric", "price": 5000, "currency": "USD", "unit": "kg"},
    {"id": 94, "name": "Bicarbonat de sodiu", "price": 1200, "currency": "USD", "unit": "kg"},
    {"id": 95, "name": "Uleiuri esențiale", "price": 30000, "currency": "USD", "unit": "kg"},
    {"id": 96, "name": "Plante medicinale", "price": 8000, "currency": "USD", "unit": "kg"},
    {"id": 97, "name": "Cofeină", "price": 7000, "currency": "USD", "unit": "kg"},
    {"id": 98, "name": "Pectina", "price": 5000, "currency": "USD", "unit": "kg"},
    {"id": 99, "name": "Gelatină", "price": 2000, "currency": "USD", "unit": "kg"},
    {"id": 100, "name": "Glucosamina", "price": 2500, "currency": "USD", "unit": "kg"}

]


@app.route('/materials', methods=['GET'])
def get_material_by_name():
    material_name = request.args.get('name')
    if material_name:
        material = next((m for m in materials if m["name"].lower() == material_name.lower()), None)
        if material:
            return jsonify(material)
        else:
            return jsonify({"error": "Materia primă nu a fost găsită"}), 404
    else:
        return jsonify({"error": "Numele materiei prime este necesar"}), 400


app.run(debug=True)