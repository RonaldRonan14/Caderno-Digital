from flask import Flask, redirect
import os

### Controladores
from Presentation.Controllers.CadernoController import caderno_controller

### Views
views_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Presentation', 'Views')
static = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Presentation', 'wwwroot')

app = Flask(__name__, template_folder=views_dir, static_folder=static)

app.register_blueprint(caderno_controller)

@app.route("/")
def init():
    return redirect("/Anotacao")

if __name__ == '__main__':
    app.run()