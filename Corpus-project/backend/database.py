import sqlite3

def init_db():
    conn = sqlite3.connect('data/corpus.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS submissions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT,
        language TEXT,
        text TEXT,
        audio_path TEXT,
        image_path TEXT,
        caption TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )''')
    conn.commit()
    conn.close()

def insert_submission(data):
    conn = sqlite3.connect('data/corpus.db')
    c = conn.cursor()
    c.execute('''INSERT INTO submissions (type, language, text, audio_path, image_path, caption)
                 VALUES (?, ?, ?, ?, ?, ?)''', data)
    conn.commit()
    conn.close()
