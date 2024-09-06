import sqlite3
from datetime import date


def connect_db():
    return sqlite3.connect('corporate_phones.db')

def create_user(localidade, setor, linha, chip, perfil, nome, email, modelo_aparelho, data_entrega):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO usuarios (localidade, setor, linha, chip, perfil, nome, email, modelo_aparelho, data_entrega)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (localidade, setor, linha, chip, perfil, nome, email, modelo_aparelho, data_entrega))
    conn.commit()
    conn.close()


def read_users():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios')
    users = cursor.fetchall()
    conn.close()
    return users


def update_user(user_id, localidade, setor, linha, chip, perfil, nome, email, modelo_aparelho, data_entrega):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE usuarios
        SET localidade = ?, setor = ?, linha = ?, chip = ?, perfil = ?, nome = ?, email = ?, modelo_aparelho = ?, data_entrega = ?
        WHERE id = ?
    ''', (localidade, setor, linha, chip, perfil, nome, email, modelo_aparelho, data_entrega, user_id))
    conn.commit()
    conn.close()


def delete_user(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM usuarios WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    
    create_user('São Paulo', 'TI', '123456789', '987654321', 'Corporativo', 'João Silva', 'joao.silva@empresa.com', 'iPhone 12', date.today())

   
    users = read_users()
    for user in users:
        print(user)

    
    update_user(1, 'São Paulo', 'TI', '123456789', '987654321', 'Corporativo', 'João Silva', 'joao.silva@empresa.com', 'iPhone 13', date.today())

   
    delete_user(1)
