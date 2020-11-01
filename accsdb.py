import sqlite3


def create_db():
    conn = sqlite3.connect('accounts.db')
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS accs(
       id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
       email TEXT,
       emailpassword TEXT,
       token TEXT,
       vk TEXT,
       vkpassword TEXT,
       vkworks INT,
       insta TEXT,
       instapassword TEXT,
       instaworks INT
       );
    """)
    conn.commit()

def update_account(vk_new = '-', vk_pass = '-', vk_old = '-', insta_new='-', insta_pass ='-', insta_old ='-'):
    conn = sqlite3.connect('accounts.db')
    cur = conn.cursor()
    if vk_new !='-':
        sql = """UPDATE accs SET vk= '{}' WHERE vk='{}' """.format(vk_new, vk_old)
        cur.execute(sql)
        sql = """UPDATE accs SET vkpass= '{}' WHERE vk='{}' """.format(vk_pass, vk_new)
        cur.execute(sql)
        conn.commit()
    if insta_new != '-':
        sql = """UPDATE accs SET insta '{}' WHERE insta='{}' """.format(insta_new, insta_old)
        cur.execute(sql)
        sql = """UPDATE accs SET instapass= '{}' WHERE insta='{}' """.format(insta_pass, insta_new)
        cur.execute(sql)
        conn.commit()

def add_account(email, emailpass, token, vk='-', vkpass='-', insta='-', instapass='-'):
    conn = sqlite3.connect('accounts.db')
    cur = conn.cursor()
    note = (None, email, emailpass, token, vk, vkpass, 1, insta, instapass, 1)
    cmd = """
    INSERT into accs VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """
    cur.execute(cmd, note)
    conn.commit()

def delete_account(vk ='-', insta='-'):
    conn = sqlite3.connect('accounts.db')
    cur = conn.cursor()
    if vk != '-':
        sql = """UPDATE accs  SET vkpass = '-' WHERE vk = '{}' """.format(vk)
        cur.execute(sql)
        sql = """UPDATE accs SET vkworks = 0 WHERE vk = '{}' """.format(vk)
        cur.execute(sql)
        sql = """UPDATE accs SET vk = '-' WHERE vk = '{}' """.format(vk)
        cur.execute(sql)
        conn.commit()
    if insta != '-':
        sql = """UPDATE accs SET instaworks = 0  WHERE insta = '{}'""".format(insta)
        cur.execute(sql)
        sql = """UPDATE accs SET instapass = '-' WHERE insta = '{}' """.format(insta)
        cur.execute(sql)
        sql = """UPDATE accs   SET insta = '-'  WHERE insta = '{}' """.format(insta)
        cur.execute(sql)
        conn.commit()

def get_account(id):
    conn = sqlite3.connect('accounts.db')
    cur =conn.cursor()
    #sql = 'SELECT * FROM accs; '
    sql = 'SELECT * FROM accs WHERE id = {}'.format(id)
    cur.execute(sql)
    return cur.fetchone()

