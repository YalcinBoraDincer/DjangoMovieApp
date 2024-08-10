import sqlite3

# Veritabanına bağlan
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Tabloyu sil
cursor.execute('DROP TABLE mywebsite_comment')

# Değişiklikleri kaydet ve bağlantıyı kapat
conn.commit()
conn.close()
