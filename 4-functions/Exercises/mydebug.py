"""
1. Definire diversi decoratori che aggiungano caratteri e formattazioni, prima e dopo dei messaggi, per standardizzare il debugging.

2. Utilizzare termcolor per colorare i debug.

3. Incapsulare i metodi in una classe e renderli statici.

4. Ai log aggiungere i timestamps tramite il modulo datetime, e salviamo tutto sul file debug.log.
"""
from termcolor import colored, cprint
from sys import exit, stderr
from datetime import datetime

# --- DECORATORI ---

class MyDebug:
  # Nome del file di log centralizzato
  LOG_FILE = "debug.log"

  @staticmethod
  def _scrivi_su_file(tag, messaggio):
      timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      # Costruiamo la riga pulita senza codici di colore ANSI
      riga_log = f"[{timestamp}] {tag} - {messaggio}\n"

      # Apriamo il file in modalità 'append' ('a'), così non sovrascriviamo i log precedenti
      with open(MyDebug.LOG_FILE, "a", encoding="utf-8") as f:
          f.write(riga_log)

  @staticmethod
  def infoprint(f):
      def wrapper(*args, **kwargs):
          # 1. Output colorato nel terminale
          output = colored("[INFO]", "blue", attrs=["reverse", "blink"])
          print(output)
          f(*args, **kwargs)
          print("\n")

          # 2. Salvataggio immediato sul file system
          msg = args[0] if args else ""
          MyDebug._scrivi_su_file("[INFO]", msg)
      return wrapper

  @staticmethod
  def okprint(f):
      def wrapper(*args, **kwargs):
          cprint("OK", "yellow", "on_green", attrs=["bold"])
          f(*args, **kwargs)
          print("\n")

          msg = args[0] if args else ""
          MyDebug._scrivi_su_file("[OK]", msg)
      return wrapper

  @staticmethod
  def errorprint(f):
      def wrapper(*args, **kwargs):
          cprint("\t=== ERRORE! ===", "red", attrs=["bold"], file=stderr)
          f(*args, **kwargs)
          print("\n")

          msg = args[0] if args else ""
          MyDebug._scrivi_su_file("[ERROR]", msg)
      return wrapper

  @staticmethod
  def quit(n):
    def dec(f):
        def wrapper(*args, **kwargs):
            if n > 4:
                raise KeyboardInterrupt("\nAnche no. Interrompiamo qui.\n")
            for _ in range(n):
              cprint("\n=============================================",
                    "light_red", "on_white", attrs=["concealed", "reverse"])
              print("\nGrazie per aver usato la nostra applicazione!")
              print("Alla prossima!\n")

              MyDebug._scrivi_su_file("[SYSTEM]", "Applicazione chiusa dall'utente.")
        return wrapper
    return dec

  @staticmethod
  def lower_ignorecase(f):
      def wrapper(*args, **kwargs):
          print("\n")
          # Eseguiamo input() e salviamo il risultato
          risultato = f(*args, **kwargs)
          print("\t> ", end="")
          # Restituiamo il testo pulito per poterlo usare nel main
          return risultato.strip().lower()
      return wrapper


# --- FUNZIONI DECORATE ---

# Uso di istanza Debug

@MyDebug.lower_ignorecase
def prendi_input(messaggio):
    return input(messaggio)

@MyDebug.infoprint
def stampa_info(testo):
    print(testo)

@MyDebug.okprint
def stampa_ok(testo):
    print(testo)

@MyDebug.errorprint
def stampa_errore(testo):
    print(testo)

@MyDebug.quit(2)
def quit_program():
    return


# --- MAIN ---

def main():

    while True:
      # Ora la funzione decorata restituisce correttamente la stringa formattata
      choice = prendi_input("Scrivi 'info', 'ok' o 'err' per testare il debug, 'q' per uscire: ")

      # Sintassi corretta del match-case in Python
      match choice:
          case "q" | "quit" | "exit":
              quit_program()
              break

          case "info" | "i":
              stampa_info("TEST INFO PRINT")

          case "ok" | "o":
              stampa_ok("TEST OK PRINT")

          case "error" | "err" | "e" | _: # L'underscore (_) gestisce il default
              stampa_errore("TEST ERROR PRINT")

    return 0


if __name__ == "__main__":
    exit(main())