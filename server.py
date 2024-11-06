import os


from waitress import serve
from app import create_app
app = create_app(os.getenv("CONFIG_MODE"))


if __name__ == "__main__":
    # To Run the Server in Terminal => flask run -h localhost -p 5000
    # To Run the Server with Automatic Restart When Changes Occurred => FLASK_DEBUG=1 flask run -h localhost -p 5000
    if os.getenv("CONFIG_MODE") == "production":
        serve(app, host="0.0.0.0", port=10000)
    else:
        app.run()
