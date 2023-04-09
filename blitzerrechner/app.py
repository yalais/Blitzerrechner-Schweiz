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
# berechne die überschreitung
    if radar == 'laser':
        if gefahrene < 100:
            result = gefahrene - erlaubte - 3
        elif gefahrene <= 100 and gefahrene < 150:
            result = gefahrene - erlaubte - 4
        elif gefahrene >= 150:
            result = gefahrene - erlaubte - 5
    elif radar == 'mobil':
        if gefahrene < 100:
            result = gefahrene - erlaubte - 7
        elif gefahrene <= 100 and gefahrene < 150:
            result = gefahrene - erlaubte - 8
        elif gefahrene >= 150:
            result = gefahrene - erlaubte - 9
    elif radar == 'stationaer':
        if gefahrene < 100:
            result = gefahrene - erlaubte - 5
        elif gefahrene <= 100 and gefahrene < 150:
            result = gefahrene - erlaubte - 6
        elif gefahrene >= 150:
            result = gefahrene - erlaubte - 7

    session['result'] = result

    if result > 0:
        return render_template('kategorie.html')
    else:
        return render_template('keine_strafe.html')


# Auswahl des starssentyps und weiterleitung an das Resultat
@app.route('/ergebnis', methods=['POST'])
def ergebnis():
    answer = request.form.get('kategorie')
    result = session['result']
    strafe = 0
    busse = 0

    if answer == '30':
        if result <= 5:
            strafe = 'keine weitere Strafe'
            busse = 40
        elif result <= 10:
            strafe = 'keine weitere Strafe'
            busse = 120
        elif result <= 15:
            strafe = 'keine weitere Strafe'
            busse = 250
        elif result <= 17:
            strafe = 'keine weitere Strafe'
            busse = 400
        elif result <= 19:
            strafe = 'keine weitere Strafe'
            busse = 600
        elif result <= 20:
            strafe = 'keine weitere Strafe'
            busse = '30 Tagessätze'
        elif result <= 24:
            strafe = 'keine weitere Strafe'
            busse = '30 Tagessätze'
        elif result <= 25:
            strafe = 'keine weitere Strafe'
            busse = '30 Tagessätze'
        elif result <= 29:
            strafe = 'keine weitere Strafe'
            busse = '50 Tagessätze'
        elif result <= 34:
            strafe = 'keine weitere Strafe'
            busse = '90 Tagessätze'
        elif result <= 39:
            strafe = 'keine weitere Strafe'
            busse = '120 Tagessätze'
        else:
            strafe = 'mindestens 1 Jahr Freiheitsentzug'
            busse = 'mindestens 300'
        return render_template('ergebnis1.html', result=result, strafe=strafe, busse=busse)
    
    elif answer == '50':
        return render_template('ergebnis2.html', result=result)
    
    elif answer == '80':
        return render_template('ergebnis3.html', result=result)
    
    elif answer == '120':
        return render_template('ergebnis4.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)



# abzüge kontrollieren pro Radartyp immer gleich?
# Bild wird nicht angezeigt
# wiederholungstäter einbeziehen
# Dataframe zur auswahl der Straffen anstelle von unendlich vielen if else statements