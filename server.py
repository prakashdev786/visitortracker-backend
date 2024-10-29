import os



from app import create_app 
app = create_app(os.getenv("CONFIG_MODE"))



if __name__ == "__main__":
    # To Run the Server in Terminal => flask run -h localhost -p 5000
    # To Run the Server with Automatic Restart When Changes Occurred => FLASK_DEBUG=1 flask run -h localhost -p 5000
    app.run()
    