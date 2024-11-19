import sqlite3
import time
import random
import requests


class DataBase:
    def __init__(self):
        self.conn = sqlite3.connect("My_Factory.db")
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Productie(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nume_produs TEXT,
        cantitate INTEGER,
        pret INTEGER)''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Angajati(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nume TEXT,
        varsta INTEGER,
        ani_experienta INTEGER,
        departament TEXT,
        salariu INTEGER)''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Comenzi(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        produs TEXT,
        client TEXT,
        cantitate INTEGER)''')




    def add_product(self,nume_produs, cantitate, pret):
        self.cursor.execute('''INSERT INTO Productie(
        nume_produs, cantitate, pret)
        VALUES (?,?,?)
        ''', (nume_produs, cantitate, pret))
        self.conn.commit()
        print(f"Produsul {nume_produs} a fost adaugat cu succes.")

    def delete_product(self, nume_produs):
        try:
            self.cursor.execute('''
            DELETE FROM Productie
            WHERE nume_produs = ?
            ''', (nume_produs,))
            if self.cursor.rowcount > 0:
                self.conn.commit()
                print(f"Produsul {nume_produs} a fost sters cu succes.")
        except sqlite3.Error as e:
            print(f"O eroare a apărut la ștergerea produsului: {e}")




    def add_employee(self,nume, varsta, ani_experienta, departament, salariu):
        self.cursor.execute('''
        INSERT INTO Angajati(
        nume, varsta, ani_experienta, departament, salariu)
        VALUES (?,?,?,?,?)
        ''',(nume, varsta, ani_experienta, departament, salariu))
        self.conn.commit()
        print(f"Angajatul {nume} a fost adaugat cu succes.")


    def delete_employee(self,nume):
        self.cursor.execute('''
        DELETE FROM Angajati
         WHERE nume = ?
         ''',(nume,))
        if self.cursor.rowcount > 0:
            self.conn.commit()
            print(f"Angajatul {nume} a fost sters cu succes.")



    def add_order(self,produs, client, cantitate):
        self.cursor.execute('''
        INSERT INTO Comenzi(
        produs, client, cantitate)
        VALUES (?,?,?)
        ''',(produs, client, cantitate))
        self.conn.commit()
        print(f"Comanda {produs} a fost adaugata cu succes.")


    def dell_order(self,id):
        self.cursor.execute('''
        DELETE FROM Comenzi
        WHERE id = ?
        ''',(id,))
        if self.cursor.rowcount > 0:
            self.conn.commit()
            print(f"Comanda cu id-ul {id} a fost stearsa cu succes.")

    def view_products(self):
        self.cursor.execute("SELECT * FROM Productie")
        return self.cursor.fetchall()

    def view_employees(self):
        self.cursor.execute("SELECT * FROM Angajati")
        return self.cursor.fetchall()

    def view_orders(self):
        self.cursor.execute("SELECT * FROM Comenzi")
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()



class Production_Line:
    def __init__(self):
        self.products_made = 0

    def make_product(self):
        print("Simuleaza fabricarea unui produs")
        print("Productia incepe...")


        print("1.Asamblare...")
        time.sleep(2)

        print("Verificare...")
        time.sleep(2)

        if random.random() < 0.1:
            print("Produsul are un defect")
            return False

        print("3.Finalizare...")
        time.sleep(1)
        self.products_made+=1
        print(f"Produsul {self.products_made} a fost finalizat cu succes.")
        return True







def main():
    line = Production_Line()
    db = DataBase()

    while True:
        print("\n=== MENIU ===")
        print("1. Produce un produs")
        print("2. Adaugă produs")
        print("3. Șterge produs")
        print("4. Adaugă angajat")
        print("5. Șterge angajat")
        print("6. Adaugă comandă")
        print("7. Șterge comandă")
        print("8. Arată prețul materialelor din API")
        print("9. Afișează produsele")
        print("10. Afișează angajații")
        print("11. Afișează comenzile")
        print("12. Ieșire")

        choice = input("\nAlege o opțiune (1-12): ")

        if choice == '1':
            line.make_product()

        elif choice == '2':
            nume = input("Numele produsului de adaugat: ")
            cantitate = int(input("Cantitatea: "))
            pret = int(input("Pretul: "))
            db.add_product(nume,cantitate,pret)

        elif choice == '3':

            nume = input("Numele produsului de sters: ")
            db.delete_product(nume)

        elif choice == '4':
            nume = input("Nume angajat: ")
            varsta = int(input("Vârsta: "))
            ani_experienta = int(input("Ani experiență: "))
            departament = input("Departament: ")
            salariu = int(input("Salariu: "))
            db.add_employee(nume, varsta, ani_experienta, departament, salariu)

        elif choice == '5':
            nume = input("Introduceți numele angajatului de șters: ")
            db.delete_employee(nume)

        elif choice == '6':
            produs = input("Produs comandat: ")
            client = input("Numele clientului: ")
            cantitate = int(input("Cantitate: "))
            db.add_order(produs, client, cantitate)

        elif choice == '7':
            id_comanda = int(input("Introduceți ID-ul comenzii de șters: "))
            db.dell_order(id_comanda)

        elif choice == '8':
            material_name = input("Introdu numele materiei prime: ")
            response = requests.get(f"http://127.0.0.1:5000/materials?name={material_name}")
            if response.status_code == 200:
                material = response.json()
                print(f"Nume: {material['name']}, Preț: {material['price']} {material['currency']}")
            else:
                print("Materia primă nu a fost găsită.")

        elif choice == '9':
            db.cursor.execute('SELECT * FROM Productie')
            rows = db.cursor.fetchall()
            if rows:
                print("\nProduse în stoc:")
                for row in rows:
                    print(f"ID: {row[0]}, Nume: {row[1]}, Cantitate: {row[2]}, Preț: {row[3]}")
            else:
                print("Nu există produse în baza de date.")

        elif choice == '10':
            db.cursor.execute('SELECT * FROM Angajati')
            rows = db.cursor.fetchall()
            if rows:
                print("\nAngajați:")
                for row in rows:
                    print(
                        f"ID: {row[0]}, Nume: {row[1]}, Vârstă: {row[2]}, Experiență: {row[3]}, Departament: {row[4]}, Salariu: {row[5]}")
            else:
                print("Nu există angajați în baza de date.")

        elif choice == '11':
            db.cursor.execute('SELECT * FROM Comenzi')
            rows = db.cursor.fetchall()
            if rows:
                print("\nComenzi:")
                for row in rows:
                    print(f"ID: {row[0]}, Produs: {row[1]}, Client: {row[2]}, Cantitate: {row[3]}")
            else:
                print("Nu există comenzi în baza de date.")


        elif choice == '12':
            print("La revedere!")
            db.close()
            break
        else:
            print("Opțiune invalidă")


if __name__ == "__main__":
    main()