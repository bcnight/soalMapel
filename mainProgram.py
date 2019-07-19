#Author:Alwan Putra ft Gunawan Cipta
#VERSI 2.0
#MAU RECODE? TAU DIRI
#BUAT PEMBELAJARAN AJA

# Kode - Kode Warna yang digunakan
R = '\033[31m' # Red
N = '\033[1;37m' # White
G = '\033[32m' # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' # Blue

# Modul Modul Yang DiGunakan 
from getpass import getpass
import time
import mapel
from soal_develop_2 import kumpulan_soal

users = {
    "root": {
        "password": "bau-memec",
        "group": []
    }
}

def loginauth(username, password):
    if username in users:
        if password == users[username]["password"]:
            print("Login sukses")
            return True
    return False

def login():
    while True:
        username = input("Username: ")
        if not len(username) > 0:
            print("username ga bole kosong ajg,isi la bgst")
        else:
            break
    while True:
        password = getpass("Password: ")
        if not len(password) > 0:
            print("password ga boleh kosong anjg,isi la bgst")
        else:
            break

    if loginauth(username, password):
        return session(username)
    else:
        print("Invalid username or password,buat akun dlu ppq kalo blm buat")

def daftar():
    while True:
        username = input("New username: ")
        if not len(username) > 0:
            print("username ga bole kosong ajg,isi la bgst")
            continue
        else:
            break
    while True:
        password = getpass("New password: ")
        if not len(password) > 0:
            print("password ga bole kosong ajg,isi la bgst")
            continue
        else:
            break
    print("membuat akun ajg...")
    users[username] = {}
    users[username]["password"] = password
    users[username]["group"] = "user"
    time.sleep(1)
    print("akun sukses dibuat,login menggunakan yg dibuat tadi")

def session(username):
    time.sleep(1)
    print("-"*31)
    print("Welcome to system learning " + username)
    print("Options: [1.]Soal | [q.]Quit")
    while True:
        input_user = input(username + " > ")
        if input_user == "1":
            kumpulan_soal()

        elif input_user == "q":
            exit()

        else:
            print(input_user + "\nyg bener inputnya gblk")
            
def menu():
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+                    Welcome to the system learning                 +")
    print("+             Sebelum login untuk daftar terlebih dahulu            +")
    print("+       Options: [1].LOGIN | [2].DAFTAR | [3].MAPEL | [9].EXIT      +")
    print("+                        https://gataungoding.id/                   +")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    start = 0

    while start != 10:

        input_user = str(input('pilih angka > '))

        if input_user == "1":
            login()

        elif input_user == "2":
            daftar()

        elif input_user is "3":
            mapel.matapelajaran()

        elif input_user == "9":
            exit()

        else:
            print(input_user + "\nyg bener inputnya gblk")


menu()
