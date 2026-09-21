from flask import Flask, render_template
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "db"),
        user=os.getenv("DB_USER", "crochet"),
        password=os.getenv("DB_PASSWORD", "crochet123"),
        database=os.getenv("DB_NAME", "crochet_db")
    )

@app.route("/")
def home():
    products = []

    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT id, name, description, price, image_url
            FROM products
        """)

        products = cursor.fetchall()

        cursor.close()
        conn.close()

    except Exception as e:
        print("Database error:", e)

    return render_template("index.html", products=products)


@app.route("/health")
def health():
    return "Crochet Flask Application is healthy!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
