#from website import create_app
from website import app

#app = create_app()

if __name__ == '__main__':
    app.run(port=8008, debug=True)
    pass