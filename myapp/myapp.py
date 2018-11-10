from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

'''
# Try adding an about page.
#  1. In this file, create a route to '/about' with a matching function definition below it
#  2. Have the function return the about.html template
#  3. Create an about.html file in the templates folder that extends layout.html
#  4. Add a link to it in navbar.html
#  5. Restart your application and refresh the page at localhost to see you updates.
'''


if __name__ == '__main__':
    app.run(debug=True)