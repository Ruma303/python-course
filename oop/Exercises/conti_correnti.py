"""
Creare un conto corrente basilare con possibilità di deposito, prelievo e visualizzazione del saldo
Creare un secondo conto corrente più evoluto aggiungendo il calcolo degli interessi
"""

class ContoCorrente:
    def __init__(self, saldo_iniziale=0):
        self.saldo = saldo_iniziale
        self.tipo_conto = type(self).__name__
        print(f"\nNuovo {self.tipo_conto} creato correttamente\n")
        self.visualizza_saldo()

    def deposita(self, ammontare):
        self.saldo += ammontare
        print(f"Hai depositato {ammontare}")
        self.visualizza_saldo()

    def preleva(self, ammontare):
        if self.saldo >= ammontare:
            self.saldo -= ammontare
            print(f"Hai prelevato {ammontare}.")
        else:
            print(f"Non è possibile prelevare {ammontare}: fondi insufficienti")
        self.visualizza_saldo()

    def visualizza_saldo(self):
        print(f"Il tuo saldo attuale è: {self.saldo}\n")


class ContoCorrenteInteressi(ContoCorrente):
    def __init__(self, saldo_iniziale=0, tasso_interesse=0.05):
        # Normalizza il tasso se fornito come intero (es: 10 -> 0.10)
        if tasso_interesse > 1:
            tasso_interesse = tasso_interesse / 100
        self.tasso_interesse = tasso_interesse
        super().__init__(saldo_iniziale)

    def calcolo_interessi(self):
        interessi = self.saldo * self.tasso_interesse
        print(f"Interessi maturati: {interessi}")
        self.deposita(interessi)

conto_corrente_basilare = ContoCorrente(100)
conto_corrente_basilare.deposita(50)
conto_corrente_basilare.preleva(200)
conto_corrente_basilare.preleva(70)

conto_corrente_con_interessi_1 = ContoCorrenteInteressi()
conto_corrente_con_interessi_1.deposita(1000)
conto_corrente_con_interessi_1.preleva(400)
conto_corrente_con_interessi_1.calcolo_interessi()
conto_corrente_con_interessi_1.visualizza_saldo()

conto_corrente_con_interessi_2 = ContoCorrenteInteressi(saldo_iniziale=500)
conto_corrente_con_interessi_2.calcolo_interessi()

conto_corrente_con_interessi_3 = ContoCorrenteInteressi(saldo_iniziale=200, tasso_interesse=10)
conto_corrente_con_interessi_3.calcolo_interessi()