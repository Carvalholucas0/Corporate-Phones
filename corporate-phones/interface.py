import sqlite3
import tkinter as tk
from tkinter import messagebox


def create_phone():
    localidade = entry_localidade.get()
    setor = entry_setor.get()
    linha = entry_linha.get()
    chip = entry_chip.get()
    perfil = entry_perfil.get()
    nome_usuario = entry_nome_usuario.get()
    email = entry_email.get()
    modelo_aparelho = entry_modelo_aparelho.get()
    data_entrega = entry_data_entrega.get()

    conn = sqlite3.connect('corporate_phones.db')
    c = conn.cursor()
    c.execute("INSERT INTO phones (localidade, setor, linha, chip, perfil, nome_usuario, email, modelo_aparelho, data_entrega) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
              (localidade, setor, linha, chip, perfil, nome_usuario, email, modelo_aparelho, data_entrega))
    conn.commit()
    conn.close()
    messagebox.showinfo("Create", "Telefone inserido com sucesso!")

def read_phones():
    conn = sqlite3.connect('corporate_phones.db')
    c = conn.cursor()
    c.execute("SELECT * FROM phones")
    rows = c.fetchall()
    phones_list.delete(0, tk.END)
    for row in rows:
        phones_list.insert(tk.END, row)
    conn.close()

def delete_phone():
    phone_id = entry_id.get()
    conn = sqlite3.connect('corporate_phones.db')
    c = conn.cursor()
    c.execute("DELETE FROM phones WHERE id=?", (phone_id,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Delete", "Telefone deletado com sucesso!")


root = tk.Tk()
root.title("Corporate Phones Management")
root.geometry("600x400")


labels = ["Localidade", "Setor", "Linha", "Chip", "Perfil", "Nome do usuário", "Email", "Modelo do aparelho", "Data da entrega"]
entries = []

for label in labels:
    lbl = tk.Label(root, text=label)
    lbl.pack()
    entry = tk.Entry(root)
    entry.pack()
    entries.append(entry)

entry_localidade, entry_setor, entry_linha, entry_chip, entry_perfil, entry_nome_usuario, entry_email, entry_modelo_aparelho, entry_data_entrega = entries


lbl_id = tk.Label(root, text="ID")
lbl_id.pack()
entry_id = tk.Entry(root)
entry_id.pack()


btn_create = tk.Button(root, text="Inserir", command=create_phone)
btn_create.pack(pady=5)

btn_read = tk.Button(root, text="Ler", command=read_phones)
btn_read.pack(pady=5)

btn_delete = tk.Button(root, text="Deletar", command=delete_phone)
btn_delete.pack(pady=5)


phones_list = tk.Listbox(root)
phones_list.pack(pady=10)


root.mainloop()