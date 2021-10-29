# Flask server template
> A template for a web based flask server.

## Introduction
This template is for people who want to use flask as their HTML/JS server or renderer.

## Usage
Download [Flask](https://flask.palletsprojects.com/en/2.0.x/) within your project,
```sh
pip install Flask
```
Start the python script.

## Linking Javascript or CSS
Linking Javascript or CSS files while using a Flask server is different then vanilla HTML. Now:

```html
<script src="{{ url_for('static', filename='<filename>')}}"></script>
```

or

```html
<link rel="stylesheet" href="{{ url_for('static', filename='<filename>')}}"/>
```

## Creating and linking more HTML files
Creating a multi-page Flask server is more complicated, you will need to have one route to both render the form on GET and handle the form submit on POST.
In your `main.py` file:
```python
@app.route('/cool_page', methods=['GET', 'POST'])
def cool_form():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('cool_page.html')
```
Now in your `templates/index.html` file:

```html

<p><a href="{{ url_for('cool_page') }}">Check out this new HTML page!</a></p>

```
And in your `templates/cool_page.html` file:
```html
<body>
    <form method="post">
        <button type="submit">Do it!</button>
    </form>
</html>
```

If you need to link to static files, put them in the `static` folder, then use:

```
url_for('static', filename='a_picture.png')
```

## Dividing the Flask app into multiple python files
You can create a sub-component of your app as a Blueprint in a seperate file:
```python
simple_page = Blueprint('simple_page', __name__, template_folder='templates')
@simple_page.route('/<page>')
def show(page):
    # stuff
```
And then use it in the main part:
```python
from yourapplication.simple_page import simple_page

app = Flask(__name__)
app.register_blueprint(simple_page)
```

## License
[MIT](https://github.com/LCordial/flask-server/blob/main/LICENSE)
