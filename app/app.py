from flask import Flask

# Create the Flask application instance
app = Flask(__name__)

# Define the home route
@app.route('/')
def home():
    return "<h1>Welcome to the Simple Flask App!</h1><p>This is the home page.</p>"

# Define the about route
@app.route('/about')
def about():
    return "<h1>About Page</h1><p>This is a simple Flask application example.</p>"

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

