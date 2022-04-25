from turtle import clear
from website import create_web
app = create_web()

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")