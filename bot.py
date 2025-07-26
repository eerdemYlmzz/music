import tkinter as tk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Eğitim verim
egitim_cumleleri = [
    "Bugün çok mutluyum harika hissediyorum",
    "Hayat çok güzel her şey yolunda",
    "Kendimi enerjik ve iyi hissediyorum",
    "Çok üzgünüm, moralim bozuk",
    "Hayal kırıklığına uğradım, kötü hissediyorum",
    "Yalnızım ve canım sıkkın",
    "Heyecanlıyım yeni şeyler oluyor",
    "Stresliyim işler yolunda gitmiyor",
    "Şaşkınım böyle bir şey beklemiyordum",
    "Aşırı yorgunum, bitkin hissediyorum",
    "Bugün bok gibi hissediyorum",
    "Hava çok güzel",
    "Çok yoğun bir gündü",
    "İnanılmaz yoruldum",
    "İnanılmaz eğlenceliydi",
    "Allah belasını versin bu günün",
    "Arkadaşlarla takıldık",
    "Dışarı çıktım hava baya güzeldi",
    "Hava yağmurluydu ve kapalıydı pek iyi hissetmiyorum",
    "En mutlu günüm",
    "En mutsuz günüm",
    "Sevgilimden ayrıldım",
    "Sevgili yaptım , oldu",
    "Ne yapıcam bilmiyorum",
    "Elim ayağım titriyo",
    "Şaka gibi gerçekten",
    "Gözlerime inanamadım",
    "Yarın büyük gün",
    "Ne olacak bilmiyorum",
    "Olacak",
    "Gidicem",
    "Yorucu",
    "Kendimi çok huzurlu hissediyorum",
    "Her şey yolunda, harika bir gün geçirdim",
    "İyi hissediyorum, çok enerjiğim",
    "Herkes beni takdir ediyor, çok mutluyum",
    "Bugün hiç iyi hissetmedim",
    "Çok üzgünüm, canım sıkılıyor",
    "üzgünüm genel olarak","mutlu değilim gibi","bilmiyorum"
]

duygular = [
    "mutlu", "mutlu", "mutlu", "üzgün", "üzgün", "üzgün", "heyecanlı", "stresli", 
    "şaşkın", "yorgun", "üzgün", "mutlu", "yorgun", "yorgun", "mutlu", "üzgün", 
    "mutlu", "mutlu", "üzgün", "mutlu", "üzgün", "üzgün", "üzgün", "mutlu", 
    "stresli", "stresli", "şaşkın", "şaşkın", "heyecanlı", "yorgun", "mutlu", 
    "mutlu", "mutlu", "mutlu", "mutlu", "üzgün", "mutlu", "mutlu","üzgün","üzgün","stresli"
]

vectorizer = CountVectorizer(lowercase=True)
X = vectorizer.fit_transform(egitim_cumleleri)
model = MultinomialNB()
model.fit(X, duygular)

def tahmin_et():
    hikaye = entry.get()  
    hikaye_vec = vectorizer.transform([hikaye]) 
    tahmin = model.predict(hikaye_vec) 
    
    sarki_onerileri = {
        "mutlu": ["Dua Lipa - Levitating", "Micheal Jackson - Smooth Criminal"],
        "üzgün": ["Dua Lipa - French Exit", "Billie Eilish - Wildflower"],
        "heyecanlı": ["Sean Paul, Dua Lipa - No Lie", "Queen - Don't Stop Me Now"],
        "stresli": ["Billie Eilish - Blue", "Dua Lipa - Maria"],
        "şaşkın": ["Lana Del Rey - West Coast", "Elton John - Where is the Shoorah?..."],
        "yorgun": ["Gotye - Somebody That I Used To Know", "ABBA - Dancing Queen","Dua Lipa - Love Again"]
    }

    öneri = sarki_onerileri.get(tahmin[0], ["Ruh haline uygun şarkı bulamadım."])
    sonuc_label.config(text=f"Senin ruh halin: {tahmin[0]}\nÖnerilen şarkılar: {', '.join(öneri)}", fg="blue")

def exit_program():
    root.quit()  

# Pencereyi oluşturu
root = tk.Tk()
root.title("Duygu Durumu ve Şarkı Önerisi")
root.config(bg="lightblue")  

# Küçültme fonksiyonu
def kucult():
    root.attributes("-fullscreen", False)  
    root.geometry("400x300") 

# Büyütme fonksiyonu
def buyut():
    root.attributes("-fullscreen", True)  

label = tk.Label(root, text="Bugün nasılsın? Biraz anlat ", bg="lightblue", font=("Helvetica", 12))
label.grid(row=0, column=0, padx=10, pady=10)

entry = tk.Entry(root, width=50)
entry.grid(row=1, column=0, padx=10, pady=10)

tahmin_button = tk.Button(root, text="Ruh Halini Tahmin Et ve Şarkı Öner", command=tahmin_et, bg= "cyan")
tahmin_button.grid(row=2, column=0, padx=10, pady=10)

sonuc_label = tk.Label(root, text="", width=50, height=6, bg="lightblue", font=("Helvetica", 10))
sonuc_label.grid(row=3, column=0, padx=10, pady=10)

exit_button = tk.Button(root, text="Çıkış Yap", command=exit_program, bg="red")
exit_button.grid(row=5, column=0, padx=40, pady=20)

kucult_button = tk.Button(root, text="Küçült", bg="salmon", command=kucult)
kucult_button.grid(row=6, column=0, padx=10, pady=10)

buyut_button = tk.Button(root, text="Büyüt", bg="salmon", command=buyut)
buyut_button.grid(row=7, column=0, padx=10, pady=10)

root.mainloop()
