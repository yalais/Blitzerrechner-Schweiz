<p align="center">
  <img src="static/icons/flask.svg" alt="Flask Icon" width="200" height="200">
</p>

# Speeding ticket calculator for Switzerland
In this repository, you can run a Flask web application, which runs a speeding ticket calculator locally on your machine.

## Structure
The Application is structured in different Python, HTML and CSS files.

:file_folder: "static" -> Contains the CSS-Sytelsheet as well as images.<br />
:file_folder: "templates" -> Stores all the HTML-templates. The main structure is in the base.html file.<br />

### Important files
<img src="static/icons/css.svg" alt="Icon CSS" width="20" height="20"> "style.css" -> Stores all the CSS-style commands for all the HTML templates. <br />
<img src="static/icons/html.svg" alt="Icon HTML" width="20" height="20"> "base.html" -> Is the base template for all HTML files. It can be adjusted with different variables. <br />
<img src="static/icons/python.svg" alt="Icon Python" width="20" height="20"> "app.py" -> Is doing all the routing. <br />
<img src="static/icons/python.svg" alt="Icon Python" width="20" height="20"> "calculations.py" -> Stores all the functions to calculate the penalties. <br />
<img src="static/icons/python.svg" alt="Icon Python" width="20" height="20"> "test_app.py" -> Excecutes different testing functions. <br />

## Requirements
For this project, Python 3.10.4 and pip 22.0.4 was used.

To run the application with all libraries on the same version it is recommended to run install requirements.txt

```
pip install -r requirements.txt
```

## Execution
To start the application locally navigate in your terminal to the folder in which you have app.py stored and run the following command.

``` 
python app.py
``` 
