from flask import Flask, render_template

app = Flask(__name__)

# Route to serve your homepage
@app.route('/')
def home():
    return render_template('homepage.html')  # Make sure 'index.html' is in the 'templates' folder

if __name__ == '__main__':
    app.run(debug=True)