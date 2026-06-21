import io

#% Streams

#, Tipi di streams

## Creazione manuale degli stream
# raw = io.FileIO("diamond.png", "r")
# buffered = io.BufferedReader(raw)
# text_stream = io.TextIOWrapper(buffered, encoding="utf-8")

# print(text_stream.read())
# print(type(text_stream))


# ## Stream Buffered Reader
# with open("diamond.png", "rb") as f:
#     dati_binari = f.read()
#     print(type(dati_binari))


#, Streams di memoria
from io import BytesIO, StringIO

bio = BytesIO()
bio.write(b"Dati binari")
bio.seek(0)
print(bio.read())

sio = StringIO()
sio.write("Testo in memoria")
sio.seek(0)
print(sio.read())


#, Streams custom

class UpperCaseStringIO(StringIO):
    def write(self, s):
        super().write(s.upper())

buffer = UpperCaseStringIO()
buffer.write("testo minuscolo")
buffer.seek(0)
print(buffer.read())  # Output: TESTO MINUSCOLO


#, Streams e gestione degli errori
try:
    with open("file_inesistente.txt") as f:
        dati = f.read()
except FileNotFoundError as e:
    print("File non trovato:", e)