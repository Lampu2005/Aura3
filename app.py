from flask import Flask
import sqlite3, pytest

app = Flask(__name__)
DB = "database.db"

@app.route("/")
def hello():
    try: sqlite3.connect(DB); return "hello world"
    except sqlite3.Error: return "Errore DB"

@pytest.fixture
def client(): yield app.test_client()

def test_root(client):
    rv = client.get("/"); assert rv.status_code==200 and rv.data==b"hello world"

if __name__ == "__main__":
    app.run(debug=True)