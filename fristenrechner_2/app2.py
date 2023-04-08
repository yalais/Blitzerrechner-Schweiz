from flask import Flask, render_template, request

app = Flask(__name__)

# Entscheidungsbaum-Struktur als Python-Dictionary
entscheidungsbaum = {
    'Frage 1': {
        'Antwort 1': {
            'Frage 2': {
                'Antwort 1': {
                    'Frage 3': {
                        'Antwort 1': 'Lösung A',
                        'Antwort 2': 'Lösung B',
                        'Antwort 3': 'Lösung C',
                        'Antwort 4': 'Lösung D',
                        'Antwort 5': 'Lösung E'
                    }
                },
                'Antwort 2': {...},
                'Antwort 3': {...},
                'Antwort 4': {...},
                'Antwort 5': {...}
            }
        },
        'Antwort 2': {...},
        'Antwort 3': {...},
        'Antwort 4': {...},
        'Antwort 5': {...}
    }
}

# Flask-Route für die Startseite
@app.route('/')
def index():
    return render_template('index.html', frage='Frage 1', antworten=entscheidungsbaum['Frage 1'])

# Flask-Route für die nächste Frage
@app.route('/frage', methods=['POST'])
def frage():
    antwort = request.form['antwort']
    neue_frage = request.form['neue_frage']
    neue_antworten = entscheidungsbaum[neue_frage]
    return render_template('index.html', frage=neue_frage, antworten=neue_antworten)

if __name__ == '__main__':
    app.run(debug=True)
