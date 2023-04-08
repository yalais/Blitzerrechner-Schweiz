from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    number = int(request.form['number'])
    if number < 0:
        message = 'Die Zahl ist negativ.'
    elif number == 0:
        message = 'Die Zahl ist null.'
    else:
        message = 'Die Zahl ist positiv.'
    return render_template('result.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)
