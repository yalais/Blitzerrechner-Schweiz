from flask import Flask, request, render_template, session, redirect, url_for
from flask_session import Session

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['SESSION_TYPE'] = 'filesystem'

Session(app)

# öffnet das html mit Landesauswahl
@app.route('/')
def land():
    return render_template('land.html')

# Landesauswahl wird überprüft und zu geschwindigkeits eingabe weitergeleitet
@app.route('/land_weiterleitung', methods=['POST'])
def land_weiterleitung():
    land = request.form.get('land')
    if land == 'schweiz':
        return redirect(url_for('index'))
    elif land == 'ausland':
        return render_template('ausland.html')

# weiterleitung geschwindigkeits eingabe
@app.route('/eingabe')
def index():
    return render_template('eingabe.html')

# speichern der Geschwindigkeitsangaben in Session
@app.route('/kategorie', methods=['POST'])
def kategorie():
    gefahrene = int(request.form.get('gefahren'))
    erlaubte = int(request.form.get('erlaubt'))
    radar = request.form.get('radar')
    session['gefahrene'] = gefahrene
    session['erlaubte'] = erlaubte

    if radar == 'laser':
        result = gefahrene - erlaubte - 1
    elif radar == 'mobil':
        result = gefahrene - erlaubte - 3
    elif radar == 'stationaer':
        result = gefahrene - erlaubte - 5

    session['result'] = result
    return render_template('kategorie.html')


# Auswahl des starssentyps und weiterleitung an das Resultat
@app.route('/ergebnis', methods=['POST'])
def ergebnis():
    answer = request.form.get('kategorie')
    result = session['result']

    if answer == '30':
        return render_template('ergebnis1.html', result=result)
    elif answer == '50':
        return render_template('ergebnis2.html', result=result)
    elif answer == '80':
        return render_template('ergebnis3.html', result=result)
    elif answer == '120':
        return render_template('ergebnis4.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)



# abzüge kontrollieren pro Radartyp immer gleich?