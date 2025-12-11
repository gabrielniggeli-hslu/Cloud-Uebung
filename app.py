"""
This module contains the main application logic for the Flask app.

It defines the routes and handlers for the different URL paths in the application.

Functions:
    home: Shows the home page.
    structure: Shows the outline of the structure to be created.
    style: Shows the styled outline with example pictures.
    movies: Shows a search mask with a form linked to '/search'.
    movies_js: Shows a search mask with a form linked to '/search_js'.
    search: Shows the result of the search performed against the OMDB API.
    search_js: Shows the result of the search performed against the OMDB API with a dynamic user interface using JavaScript.
"""
from flask import Flask, render_template, request
from requests import get

app = Flask(__name__)
API_KEY = "" # Add API Key here

@app.route('/')
def home():
    """
    The home route
    """
    return render_template('simple.html')

@app.route('/structure')
def structure():
    """
    The structure route
    """
    return render_template('structure.html')

@app.route('/style')
def style():
    """
    The style route
    """
    return render_template('style.html')

@app.route('/movies')
def movies():
    """
    The movies route that is linked to the static results page.
    """
    return render_template('movies.html')

@app.route('/movies_js')
def movies_js():
    """
    The movies route that is linked to the dynamic results page.
    """
    return render_template('movies_js.html')

@app.route('/search')
def search():
    """
    The search route showing a static result page.
    """
    return do_api_search("")


@app.route('/search_js')
def search_js():
    """
    The search route showing a dynamic result page.
    """
    return do_api_search("_js")

def do_api_search(suffix):
    """
    A function that performs an API search for movies.
    The suffix is used to switch templates (static/dynamic)

    Args:
        suffix (str): The suffix to be added to the template name.

    Returns:
        str: The rendered template with the movie search results.
    """

    template_name = f"movies{suffix}.html"
    title = request.args.get("title")

    api_results = None  # Add request code here
    json = api_results.json()
    if json["Response"] == "True":
        return render_template(template_name, error=None, movies=json["Search"], title=title)

    return  render_template(template_name, error=json["Error"], movies=[], title=title)
