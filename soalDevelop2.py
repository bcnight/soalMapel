import time

point = 0

def soal1():
    correct_answer = "e"
    print('-'*30)
    print("[1]. Linux dibuat oleh ...")
    print("  a. Mark Zuckerberg")
    print("  b. Bill Gates")
    print("  c. Tim Berners Lee")
    print("  d. Atta Halilintar")
    print("  e. Linus Torvalds")
    print()
    jawaban1 = str(input("Jawaban > "))

    global point
    if jawaban1 == correct_answer:
        time.sleep(1)
        print("> Jawaban Benar, Kamu mendapatkan 10 Point")
        point += 10
    else:
        time.sleep(1)
        print("> Jawaban Salah, Jawaban yang benar adalah", correct_answer)

    time.sleep(1)
    print("Point kamu sekarang: ", point)
    print()
    time.sleep(1)


def soal2():
    correct_answer = "a"
    print("[2]. Siapa Founder Bahasa Pemrograman Python ?")
    print("  a. Guido Van Russom")
    print("  b. Tim Berners Lee")
    print("  c. Julian Assange")
    print("  d. Snowden")
    print("  e. Benjamin Engel")
    print()
    jawaban2 = str(input("Jawaban > "))

    global point
    if jawaban2 is correct_answer:
        time.sleep(1)
        print("> Jawaban Benar, Kamu mendapatkan 10 Point")
        point += 10
    else:
        time.sleep(1)
        print("> Jawaban Salah, Jawaban yang benar adalah", correct_answer)

    time.sleep(1)
    print("Point kamu sekarang: ", point)
    print()
    time.sleep(1)


def soal3():
    correct_answer = "c"
    print("[3]. Siapa Founder Sistem Operasi Microsoft ?")
    print("  a. Julian Assange")
    print("  b. Ria Ricis")
    print("  c. Bill Gates")
    print("  d. Tukang Pijat Nurhadi")
    print("  e. Tukang Sampah")
    print()
    jawaban3 = str(input("Jawaban > "))

    global point
    if jawaban3 is correct_answer:
        time.sleep(1)
        print("> Jawaban Benar, Kamu mendapatkan 10 Point")
        point += 10
    else:
        time.sleep(1)
        print("> Jawaban Salah, Jawaban yang benar adalah", correct_answer)

    time.sleep(1)
    print("Point kamu sekarang: ", point)
    print()
    time.sleep(1)


def soal4():
    correct_answer = "b"
    print("[4]. Nama Karakter utama di film Who Am I ?")
    print("  a. Kang Urut")
    print("  b. Benjamin Engel")
    print("  c. Bill Gates")
    print("  d. Zilong")
    print("  e. Aldo")
    print()
    jawaban4 = str(input("Jawaban > "))

    global point
    if jawaban4 is correct_answer:
        time.sleep(1)
        print("> Jawaban Benar, Kamu mendapatkan 10 Point")
        point += 10
    else:
        time.sleep(1)
        print("> Jawaban Salah, Jawaban yang benar adalah", correct_answer)

    time.sleep(1)
    print("Point kamu sekarang: ", point)
    print()
    time.sleep(1)


def soal5():
    correct_answer = "b"
    print("[5]. Siapa Founder Apple ?")
    print("  a. Orang Kaya")
    print("  b. Steve Jobs")
    print("  c. Orang Missqueen")
    print("  d. Tukang Kebon")
    print("  e. Penulis Kode ini wkwk")
    print()
    jawaban5 = str(input("Jawaban > "))

    global point
    if jawaban5 is correct_answer:
        time.sleep(1)
        print("> Jawaban Benar, Kamu mendapatkan 10 Point")
        point += 10
    else:
        time.sleep(1)
        print("> Jawaban Salah, Jawaban yang benar adalah", correct_answer)

    time.sleep(1)
    print("Point kamu sekarang: ", point)
    print()
    time.sleep(1)

def total_point():
    global point
    totalpoint = point
    print("Total Point Kamu Adalah: ", totalpoint)


def kumpulan_soal():
    soal1();
    soal2();
    soal3();
    soal4();
    soal5();
    total_point();

