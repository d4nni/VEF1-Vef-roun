from flask import Flask, json

# Skilgreinum breytuna bekkur sem geymir dict (json hlut)
bekkur = {'nemandi':[{'nafn':'Daniel','braut':'tfb'},{'nafn':'Hilmir','braut':'gdr'}]}

# Skoðum innihald bekkur breytunnar - debug
print(bekkur)

# Lúppum i gegnum "allann bekkinn"

# dict key value 'nemandi' inniheldur lista
for i in bekkur['nemandi']:
    print("Nafn :", i['nafn'])# hver i er i raun gildi í listanum 'nemandi', getum hér notað key value 'nafn'

# auð lína
print()

# Bætum við nemandi..
bekkur['nemandi'].append({'nafn':'Alex','braut':'pfr'})

# Prentum aftur lista með nýjum nemanda
for i in bekkur['nemandi']:
    print("Nafn :", i['nafn'])

# Skrifum i skrána bekkur.json, er ekkert að pæla í íslenskum stöfum en það er hægt.
with open("bekkur.json","w") as skra:
    # dump er fyrir skrár, dumps fyrir strengi
    json.dump(bekkur,skra)
    skra.close() 
