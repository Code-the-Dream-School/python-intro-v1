import sqlite3

def add_publisher(cursor, name):
    try:
        cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")


def add_magazine(cursor, name, publisher_id):
    try:
        cursor.execute(
            "INSERT INTO magazines (name, publisher_id) VALUES (?, ?)",
            (name, publisher_id)
        )
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")


def add_subscriber(cursor, name, address):
    try:
        cursor.execute(
            "SELECT * FROM subscribers WHERE name = ? AND address = ?",
            (name, address)
        )
        results = cursor.fetchall()

        if len(results) > 0:
            print(f"{name} at {address} is already in the database.")
            return

        cursor.execute(
            "INSERT INTO subscribers (name, address) VALUES (?, ?)",
            (name, address)
        )
    except sqlite3.Error as e:
        print("Database error:", e)

def add_subscription(cursor, subscriber_id, magazine_id, expiration_date):
    try:
        cursor.execute(
            "SELECT * FROM subscriptions WHERE subscriber_id = ? AND magazine_id = ?",
            (subscriber_id, magazine_id)
        )
        results = cursor.fetchall()

        if len(results) > 0:
            print(f"Subscription already exists for subscriber {subscriber_id} and magazine {magazine_id}.")
            return

        cursor.execute(
            "INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)",
            (subscriber_id, magazine_id, expiration_date)
        )
    except sqlite3.Error as e:
        print("Database error:", e)

try:
    with sqlite3.connect("../db/magazines.db") as conn:
        conn.execute("PRAGMA foreign_keys = 1")

        cursor = conn.cursor()

# Create publishers table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            publisher_id INTEGER PRIMARY KEY,
            name TEXT UNIQUE NOT NULL
        )
        """)
# Create magazines table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            magazine_id INTEGER PRIMARY KEY,
            name TEXT UNIQUE NOT NULL,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
        )
        """)
# Create subscribers table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            subscriber_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        )
        """)
# Create subscription table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            subscription_id INTEGER PRIMARY KEY,
            subscriber_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES subscribers(subscriber_id),
            FOREIGN KEY (magazine_id) REFERENCES magazines(magazine_id)
        )
        """)

        add_publisher(cursor, "Time")
        add_publisher(cursor, "National Geographic")
        add_publisher(cursor, "Condé Nast")

        add_magazine(cursor, "Time Magazine", 1)
        add_magazine(cursor, "National Geographic", 2)
        add_magazine(cursor, "The New Yorker", 3)

        add_subscriber(cursor, "Ricardo Santiz", "100 Main Street")
        add_subscriber(cursor, "Maria Lopez", "200 Oak Avenue")
        add_subscriber(cursor, "John Smith", "300 Pine Road")

        add_subscription(cursor, 1, 1, "2026-12-31")
        add_subscription(cursor, 1, 2, "2026-11-30")
        add_subscription(cursor, 2, 3, "2026-10-31")
        add_subscription(cursor, 3, 1, "2026-09-30")

        print("\nPublishers:")
        cursor.execute("SELECT * FROM publishers")
        for row in cursor.fetchall():
            print(row)
      
        print("\nMagazines sorted by name:")
        cursor.execute("SELECT * FROM magazines ORDER BY name")

        for row in cursor.fetchall():
            print(row)

        print("\nMagazines by publisher:")

        cursor.execute("""
        SELECT magazines.name, publishers.name
        FROM magazines
        JOIN publishers ON magazines.publisher_id
         = publishers.publisher_id
        WHERE publishers.name = "Time"
        """)
        for row in cursor.fetchall():
            print(row)
    
        conn.commit()
        print("Connected to magazines.db")
        print("Tables created successfully.")

except sqlite3.Error as e:
    print("Database error:", e)