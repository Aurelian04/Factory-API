import tkinter as tk
from tkinter import messagebox
import requests
from Factory1 import DataBase

def create_gui():
    db = DataBase()

    def add_product_gui():
        def add_product():
            nume = entry_product_name.get()
            cantitate = int(entry_quantity.get())
            pret = int(entry_price.get())
            db.add_product(nume, cantitate, pret)
            messagebox.showinfo("Succes", f"Produsul {nume} a fost adăugat.")

        add_window = tk.Toplevel(window)
        add_window.title("Adaugă produs")
        tk.Label(add_window, text="Nume produs:").pack()
        entry_product_name = tk.Entry(add_window)
        entry_product_name.pack()
        tk.Label(add_window, text="Cantitate:").pack()
        entry_quantity = tk.Entry(add_window)
        entry_quantity.pack()
        tk.Label(add_window, text="Preț:").pack()
        entry_price = tk.Entry(add_window)
        entry_price.pack()
        tk.Button(add_window, text="Adaugă produs", command=add_product).pack()

    def delete_product_gui():
        def delete_product():
            nume = entry_product_delete.get()
            db.delete_product(nume)
            messagebox.showinfo("Succes", f"Produsul {nume} a fost șters.")

        delete_window = tk.Toplevel(window)
        delete_window.title("Șterge produs")
        tk.Label(delete_window, text="Nume produs de șters:").pack()
        entry_product_delete = tk.Entry(delete_window)
        entry_product_delete.pack()
        tk.Button(delete_window, text="Șterge produs", command=delete_product).pack()

    def add_employee_gui():
        def add_employee():
            nume = entry_employee_name.get()
            varsta = int(entry_age.get())
            ani_experienta = int(entry_experience.get())
            departament = entry_department.get()
            salariu = int(entry_salary.get())
            db.add_employee(nume, varsta, ani_experienta, departament, salariu)
            messagebox.showinfo("Succes", f"Angajatul {nume} a fost adăugat.")

        add_window = tk.Toplevel(window)
        add_window.title("Adaugă angajat")
        tk.Label(add_window, text="Nume angajat:").pack()
        entry_employee_name = tk.Entry(add_window)
        entry_employee_name.pack()
        tk.Label(add_window, text="Vârsta:").pack()
        entry_age = tk.Entry(add_window)
        entry_age.pack()
        tk.Label(add_window, text="Ani experiență:").pack()
        entry_experience = tk.Entry(add_window)
        entry_experience.pack()
        tk.Label(add_window, text="Departament:").pack()
        entry_department = tk.Entry(add_window)
        entry_department.pack()
        tk.Label(add_window, text="Salariu:").pack()
        entry_salary = tk.Entry(add_window)
        entry_salary.pack()
        tk.Button(add_window, text="Adaugă angajat", command=add_employee).pack()

    def delete_employee_gui():
        def delete_employee():
            nume = entry_employee_delete.get()
            db.delete_employee(nume)
            messagebox.showinfo("Succes", f"Angajatul {nume} a fost șters.")

        delete_window = tk.Toplevel(window)
        delete_window.title("Șterge angajat")
        tk.Label(delete_window, text="Nume angajat de șters:").pack()
        entry_employee_delete = tk.Entry(delete_window)
        entry_employee_delete.pack()
        tk.Button(delete_window, text="Șterge angajat", command=delete_employee).pack()

    def add_order_gui():
        def add_order():
            produs = entry_order_product.get()
            client = entry_order_client.get()
            cantitate = int(entry_order_quantity.get())
            db.add_order(produs, client, cantitate)
            messagebox.showinfo("Succes", f"Comanda pentru {produs} a fost adăugată.")

        order_window = tk.Toplevel(window)
        order_window.title("Adaugă comandă")
        tk.Label(order_window, text="Produs comandat:").pack()
        entry_order_product = tk.Entry(order_window)
        entry_order_product.pack()
        tk.Label(order_window, text="Client:").pack()
        entry_order_client = tk.Entry(order_window)
        entry_order_client.pack()
        tk.Label(order_window, text="Cantitate:").pack()
        entry_order_quantity = tk.Entry(order_window)
        entry_order_quantity.pack()
        tk.Button(order_window, text="Adaugă comandă", command=add_order).pack()

    def delete_order_gui():
        def delete_order():
            id_comanda = int(entry_order_id.get())
            db.delete_order(id_comanda)
            messagebox.showinfo("Succes", f"Comanda cu ID-ul {id_comanda} a fost ștearsă.")

        delete_window = tk.Toplevel(window)
        delete_window.title("Șterge comandă")
        tk.Label(delete_window, text="ID comandă de șters:").pack()
        entry_order_id = tk.Entry(delete_window)
        entry_order_id.pack()
        tk.Button(delete_window, text="Șterge comandă", command=delete_order).pack()

    def show_material_price():
        material_name = entry_material_name.get()
        response = requests.get(f"http://127.0.0.1:5000/materials?name={material_name}")
        if response.status_code == 200:
            material = response.json()
            messagebox.showinfo("Preț Material", f"Nume: {material['name']}, Preț: {material['price']} {material['currency']}")
        else:
            messagebox.showerror("Eroare", "Materia primă nu a fost găsită.")

    def view_products():
        products = db.view_products()
        view_window = tk.Toplevel(window)
        view_window.title("Produse")
        for product in products:
            tk.Label(view_window, text=f"Produs: {product[0]}, Cantitate: {product[1]}, Preț: {product[2]}").pack()

    def view_employees():
        employees = db.view_employees()
        view_window = tk.Toplevel(window)
        view_window.title("Angajați")
        for employee in employees:
            tk.Label(view_window, text=f"Angajat: {employee[0]}, Vârstă: {employee[1]}, Experiență: {employee[2]}, Departament: {employee[3]}, Salariu: {employee[4]}").pack()

    def view_orders():
        orders = db.view_orders()
        view_window = tk.Toplevel(window)
        view_window.title("Comenzi")
        for order in orders:
            tk.Label(view_window, text=f"Comandă ID: {order[0]}, Produs: {order[1]}, Client: {order[2]}, Cantitate: {order[3]}").pack()

    window = tk.Tk()
    window.title("Factory Management System")

    # Meniul principal
    tk.Button(window, text="Adaugă produs", command=add_product_gui).pack(pady=5)
    tk.Button(window, text="Șterge produs", command=delete_product_gui).pack(pady=5)
    tk.Button(window, text="Adaugă angajat", command=add_employee_gui).pack(pady=5)
    tk.Button(window, text="Șterge angajat", command=delete_employee_gui).pack(pady=5)
    tk.Button(window, text="Adaugă comandă", command=add_order_gui).pack(pady=5)
    tk.Button(window, text="Șterge comandă", command=delete_order_gui).pack(pady=5)

    tk.Label(window, text="Introduceți numele materialului:").pack()
    entry_material_name = tk.Entry(window)
    entry_material_name.pack(pady=5)
    tk.Button(window, text="Arată prețul materialului", command=show_material_price).pack(pady=5)

    tk.Button(window, text="Vizualizează produse", command=view_products).pack(pady=5)
    tk.Button(window, text="Vizualizează angajați", command=view_employees).pack(pady=5)
    tk.Button(window, text="Vizualizează comenzi", command=view_orders).pack(pady=5)

    window.mainloop()

if __name__ == "__main__":
    create_gui()


