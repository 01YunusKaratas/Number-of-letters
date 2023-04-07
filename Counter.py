class HarfSayacı:
    
    def __init__(self):
        self.SesliHarf = "aeıioöuü"
        self.SessizHarf = "zyvtşsrpnrmlkhjğgdçcb"
        self.SayacSesli = 0
        self.SayacSessiz = 0

    def Kelime(self):
        self.kelime = input("Kelimeyi Giriniz: ")
    
    def Seslimi(self, harf):
        return harf in self.SesliHarf
    
    def Sessizmi(self, harf):
        return harf in self.SessizHarf
    
    def Saydırmak(self):
        for i in self.kelime:
            if self.Seslimi(i):
                self.SayacSesli +=1
            if self.Sessizmi(i):
                self.SayacSessiz +=1

        return (self.SayacSesli, self.SayacSessiz)
        
        
    def Göster(self):
        self.Saydırmak()
        mesaj = "{} kelimesinde {} tane sesli {} tane sessiz harf vardır."
        print(mesaj.format(self.kelime, self.SayacSesli, self.SayacSessiz))

    def çalıştır(self):
        self.Kelime()
        self.Göster()


if __name__ == '__main__':
    sayac = HarfSayacı()
    sayac.çalıştır()





