''' Code Description:
    This is the main file of the project. It contains all the routes and the logic of the application.
    The application is a speed camera calculator for Switzerland. 
    It calculates the fine and the driving ban for the driver.

    At first you have to input the country where you were speeding. If you were speeding in Switzerland, you will be redirected to the speed input page.
    Else you get some information about the speed law in the country you were speeding.

    Next you should estimate your speed and the speed limit. Then you have to choose the type of the speed camera.
    As well as you have to choose if you were speeding for the first time or not.

    If you had a ban in the last two years, you will be redirected to the page with the information about the repeat offender.
    Else you will be redirected to the page where you have to choose the street type you were caught.

    If your speed difference is 0 or negative, you will be redirected to the page with no fine.
    Else you will be redirected to the page with the fine and the eventually driving ban.
    
    The fines and the driving bans are calculated based on the Swiss law.
'''


#imports
from flask import Flask, request, render_template, session, redirect, url_for
from flask_session import Session
from calculations import speed_difference, penalty_30er_zone, penalty_innerorts, penalty_ausserorts, penalty_autobahn

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SSESSION_COOKIE_NAME'] = 'session'

Session(app)

# Opens the html file for the landing page == the country selection
@app.route('/')
def land():
    return render_template('land.html')

# if the country is Switzerland, the user is redirected to the speed input page
@app.route('/land_weiterleitung', methods=['POST'])
def land_weiterleitung():
    land = request.form.get('land')
    if land == 'schweiz':
        return redirect(url_for('index'))
    elif land == 'deutschland':
        return render_template('countries/deutschland.html')
    elif land == 'frankreich':
        return render_template('countries/frankreich.html')
    elif land == 'italien':
        return render_template('countries/italien.html')
    elif land == 'oesterreich':
        return render_template('countries/oesterreich.html')
    elif land == 'lichtenstein':
        return render_template('countries/lichtenstein.html')


# give the eingabe.html file the street types
@app.route('/eingabe')
def index():
    street_types = ['30er Zone', 'Innerorts', 'Ausserorts', 'Autobahn']
    return render_template('eingabe.html', street_types=street_types)

'''
calculating the speed difference and redirecting to the street type selection
If the difference is 0 or negative, the user is redirected to the page with no fine
'''
@app.route('/kategorie', methods=['POST'])
def kategorie():
    gefahrene = int(request.form.get('gefahren'))
    erlaubte = int(request.form.get('erlaubt'))
    wiederholung = request.form.get('wiederholung')
    radar = request.form.get('radar')
    strassentyp = request.form.get('strassentyp')

    #saving the values in the session
    session['gefahrene'] = gefahrene
    session['erlaubte'] = erlaubte
    session['wiederholung'] = wiederholung
    session['strassentyp'] = strassentyp 

    #calculating the speed difference
    result = speed_difference(gefahrene, erlaubte, radar)
    session['result'] = result

    # if the user is a repeat offender, he will be redirected to the page with the information about the repeat offender
    if wiederholung == 'ja':
        return render_template('ergebnisse/wiederholungstaeter.html', result=result)

    #Strafenkatalog für 30er-Zone
    if result <= 0:
        return render_template('ergebnisse/keine_strafe.html')
    else:
        if strassentyp == '30er Zone':
            #calculating the fine and the driving ban
            strafe, busse = penalty_30er_zone(result)
            return render_template('ergebnisse/ergebnis_30er_zone.html', result=result, strafe=strafe, busse=busse)
        
        #Strafenkatalog innerorts
        elif strassentyp == 'Innerorts':
            #calculating the fine and the driving ban
            strafe, busse = penalty_innerorts(result)
            return render_template('ergebnisse/ergebnis_innerorts.html', result=result, strafe=strafe, busse=busse)
        
        #Strafenkatalog Auserorts
        elif strassentyp == 'Ausserorts':
            strafe, busse = penalty_ausserorts(result)
            return render_template('ergebnisse/ergebnis_ausserorts.html', result=result, strafe=strafe, busse=busse)
        
        #Strafenkatalog Autobahn
        elif strassentyp == 'Autobahn':
            strafe, busse = penalty_autobahn(result)
            return render_template('ergebnisse/ergebnis_autobahn.html', result=result, strafe=strafe, busse=busse)


if __name__ == '__main__':
    app.run(debug=True)