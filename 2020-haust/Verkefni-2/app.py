from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/a-hluti')
def ahluti():
    return render_template('kennitala.html')

@app.route('/k-tala/<kt>')
def ktalan(kt):
    summa=0
    for item in kt:
        summa = summa + int(item)
    return render_template('ktsum.html',kt = kt,summa = summa)

frettir = [
    ["0","Fyrsti 100% hreini rafbíllinn frá Mazda","Mazda MX-30, fyrsti 100% hreini rafbíll Mazda, er nú á leiðinni til Íslands og mun Brimborg bjóða hann með ríkulegum staðalbúnaði, víðtækri ábyrgð og innbyggðri varmadælu á verði frá 3.980.000 kr.Forpöntun á Mazda MX-30 hefst í Vefsýningarsal Brimborgar á miðnætti 4. september. Sýningar- og reynsluakstursbílar koma til Íslands í október og afhendingar til viðskiptavina hefjast í lok árs.","Kristinn Ásgeir Gylfason"],
    ["1","Kristófer Acox rýfur þögnina um fé­laga­skiptin","Kristófer Acox segir að breytingarnar, að skipta KR út fyrir Val, hafi verið nauðsynlegar því hann hafi vitað að hann yrði ekki ánægður í Vesturbænum yrði hann þar áfram.Kristófer skrifaði í gær undir samning við Val eftir að hann yfirgaf herbúðir uppeldisfélagsins KR.Kristófer yfirgaf herbúðir KR vegna ágreinings sem ekki náðist að leysa. Samkvæmt heimildum Vísis snýst þessi ágreiningur um laun sem Kristófer telur sig eiga inni hjá KR.","Anton Ingi Leifsson"],
    ["2","Segir að börnunum verði hugsan­lega rænt af yfir­völdum við komuna til Egypta­lands","Fyrrverandi formaður félags múlima á Íslandi sem bjó um árabil í Eygyptalandi segir að egypsku börnunum sem vísa á úr landi verði hugsanlega rænt af yfirvöldum við komuna til landsins og fjölskyldufaðirinn pyntaður og fangelsaður. Hann tekur nú saman sviðsmynd sem hann ætlar að senda þar til bærum yfirvöldum á Íslandi. Fjölskyldan er enn í felum. Egypska fjölskyldan sem átti að vísa úr landi á miðvikudag er ófundin og ekki hefur verið tekin ákvörðun um að lýsa eftir henni. Þá er engin formleg leit hafi samkvæmt upplýsingum frá embætti Ríkislögreglustjóra.","Nadine Guðrún Yaghi"],
    ["3","Allir sem fóru í ræktina á Akranesi þurfa að fara í sóttkví","Einstaklingur sem greindist með kórónuveiruna á Akranesi hafði stundað líkamsrækt í líkamsræktarsalnum á Jaðarbökkum þriðjudaginn 15. september.Smitrakningarteymi almannavarna hefur vegna þessa gefið út fyrirmæli til þeirra sem sóttu líkamsræktarstöðina sem iðkendur umræddan dag um að fara tafarlaust í sóttkví. Viðkomandi losnar úr sóttkví um leið og hann hefur farið í skimun og fengið neikvæða niðurstöðu.Líkamsræktarsalnum hefur verið lokað frá og með deginum í dag, 18. september í óákveðinn tíma.","Margrét Helga Erlingsdóttir"]
]

@app.route('/b-hluti')
def bhluti():
    return render_template('frettir.html', frettir=frettir)

@app.route('/frett/<int:id>')
def news(id):
    return render_template('frett.html', frett=frettir[id], nr=id)

@app.errorhandler(404)
def pagenotfound(error):
    return render_template("pagenotfound.html"), 404

@app.errorhandler(500)
def servernotfound(error):
    return render_template("servererror.html"), 500

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'Hæ %s' % escape(username)

if __name__ == '__main__':
    app.run(debug=True,use_reloader=True)