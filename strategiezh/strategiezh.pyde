#ANV AR C'HOARI


"""
    Da ober :
     * Kavout un typo (skritur) bravoc'h
     * Reiñ ur bonus difenn evit an uzinoù (1 poent difenn ouzhpenn)
     * Lakaat kemennoù sikour e plas skrid ar foñs.
        - tro 1: aloubit ur gellig eus ar vord
        - tro 2: talvoud pep kellig a zo skrivet warni
        - tro 3: klikit en diavaez m'ho peus c'hoant paseal ho tro hag espern poentoù
        - tro 4: Savit uzinoù evit gounid poentoù bep tro
        - tro 5: Un uzin a roioù bep tro kement a poentoù eget e dalvoud
        - tro 6: Distrujit uzinoù ar re all evit gounid ar partienn
        - tro 7:
     * Lakaat an destenn sikour da zirolliñ en traoñ nemetken (evel er skinwel)
     * Cheñch ar fonksion `draw_uzin` evit ma vefe kreizennet an tresadenn war an daveenoù roet e arguzenn.
     * Kavout efedoù son simpl.
     * Deplaseal an destenn skor
"""



from random import shuffle


N = 4 # Niver a c'hellig dre kostez
S = 44 # Ment pep kellig (e pixel)
NIVER_CHOARIERIEN = 3


kelligou = []
choarierien = []


def setup():
    size(600, 600)
    #fullScreen()
    
    # Kargañ ar stumm vektorel "home.svg"
    global svg
    svg = loadShape("home.svg")
    
    # Amañ e vez dibabet ment an tablez
    sevel_kael(N, S)
    
    # Klask an amezeien tro-dro pep kellig
    for k1 in kelligou:
        for k2 in kelligou:
            if dist(k1.pos.x, k1.pos.y, k2.pos.x, k2.pos.y) < 2*S+5 and k1 != k2:
                k1.amezeien.add(k2)
    
    #krouiñ a raer ar geriadur destenn_fons a tap tout an titouroù
    global testenn_fons #bezet destenn_fons, ar geriadur a tap tout an titouroù diwar benn an destenn
    testenn_fons = {}
    testenn_fons["x"] = random(500)
    testenn_fons["y"] = random(500)
    testenn_fons["testenn"] = "Demat"
    testenn_fons["ment"] = 50
    testenn_fons["finv x"] = (random(1,2)/5)
    testenn_fons["finv y"] = (random(1,2)/5)
    
    init_game()



def draw():
    global tostan
    global t_choarier
    choarier = choarierien[n_choarier]
    t_choarier += 1  # An amzer o tremen abaoe penn-kentañ tro ar c'hoarier (e 1/30 eilenn)
    
    # Livañ ar foñs
    background(0)
    fill(choarier.liv, 150)
    rect(0, 0, width, height)
    
    #skrivañ a raer an titl a-dreñv
    textSize(testenn_fons["ment"])#renkañ ment an destenn
    if ((testenn_fons["x"] <= 1) or (testenn_fons["x"] >= 499)):  
        testenn_fons["finv x"] = 0-testenn_fons["finv x"]
    if ((testenn_fons["y"] <= 30)or (testenn_fons["y"] >= 499)):
        testenn_fons["finv y"] = 0-testenn_fons["finv y"]
    testenn_fons["x"] += testenn_fons["finv x"]
    testenn_fons["y"] += testenn_fons["finv y"]
    text(testenn_fons["testenn"],testenn_fons["x"],testenn_fons["y"])
        
    # Klask ar c'hellig an tostañ eus ar logodenn
    min_dist = 999.0
    tostan = None
    for k in kelligou:
        d = dist(mouseX, mouseY, k.pos.x, k.pos.y)
        if d < Kellig.rad and d < min_dist:
            min_dist = d
            tostan = k
    
    # Tresañ ar gael a-bezh
    noStroke()
    for k in kelligou:
        k.draw()
    for k in choarier.taoliou_aloubin:
        # Livañ ar c'helligoù a c'hell bezañ aloubet gant ar c'hoarier
        fill(80, 255, 80, ((1.4+sin(t_choarier * 0.08 - PI*0.25)) * 50))
        draw_hex(k.pos.x, k.pos.y, k.rad)
    for k in choarier.taoliou_sevel:
        # Livañ ar c'helligoù lec'h ma c'hell ar c'hoarier sevel un uzin
        fill(180, 250, 40, ((1.4+sin(t_choarier * 0.08)) * 50))
        draw_hex(k.pos.x, k.pos.y, k.rad)
    for k in choarier.taoliou_tagan:
        # Livañ ar c'helligou a c'hell bezañ taget
        fill(255, 80, 80, ((1.4+sin(t_choarier * 0.08 - HALF_PI)) * 50))
        draw_hex(k.pos.x, k.pos.y, k.rad)
    for k in kelligou:
        k.draw_above()
    
    # Ad-tresañ an hini dindan al logodenn met ruz ha damdreuzwelus
    if tostan:
        noStroke()
        fill(250, 60)
        draw_hex(tostan.pos.x, tostan.pos.y, tostan.rad)
    
    # Skrivañ ar feurioù tagan a-us d'ar gelligoù
    textSize(18)
    fill(255, 180, 110)
    for k in choarier.feuriou_tagan:
        fg = choarier.feuriou_tagan[k]
        txt = str(int(round(fg))) + '%'
        tw = textWidth(txt)
        text(txt, k.pos.x - tw*0.5, k.pos.y + S*0.7)
    
    # HUD ar c'hoarier
    noStroke()
    # Adtreset e vez div wech ar c'helc'h poentoù,
    # Ur wech kentañ e du, evit kuzat ar pezh zo a-dreñv (an destenn o tremen)
    # Hag un eil wech, damtreuzwelus, evit kaout ul liv un tamm sklaeroc'h eget ar foñs
    fill(0)
    circle(40, 30, 180)
    fill(choarier.liv, 190)
    circle(40, 30, 180)
    fill(255, 250)
    textSize(70)
    text(choarier.poentou, 28, 80)
    fill(255, 190)
    textSize(25)
    text(choarier.anv, 150, 34)
    textSize(25)
    text("Tro: " + str(n_taol), width-110, 30)



def mousePressed(): 
    choarier = choarierien[n_choarier]
    
    end_turn = False
    
    if tostan:
        # Kliket eo bet war ur gellig
        if tostan in choarier.taoliou_aloubin:
            tostan.aloubet_gant = choarier
            choarier.poentou -= tostan.talvoud
            if n_taol == 1:
                tostan.aloubet_gant = choarier
                #choarier.uzinou.append(tostan)
                tostan.is_uzin = True
            choarier.update()
        elif tostan in choarier.taoliou_tagan:
            feur_gounid = choarier.feuriou_tagan[tostan]
            if random(0, 100) < feur_gounid :
                tostan.is_uzin = False
                tostan.aloubet_gant = choarier
                # Distrujañ tiriadoù ar c'hoarier taget
                enebour = tostan.aloubet_gant
                enebour.trochan()
                
            # Paeañ priz an tagadenn
            choarier.poentou -= tostan.talvoud * 2
            choarier.update()
        elif tostan in choarier.taoliou_sevel:
            tostan.is_uzin = True
            #choarier.uzinou.append(tostan)
            choarier.poentou -= tostan.talvoud * 2
            choarier.update()
    else:
        # Kliket eo bet e diavaez ar gael
        if n_taol > 1 or len(choarier.uzinou) >= 1:
            end_turn = True
    
    n_taol_posubl = len(choarier.taoliou_aloubin) + len(choarier.taoliou_tagan) + len(choarier.taoliou_sevel)
    if end_turn or n_taol_posubl == 0:
            # Dizoloiñ ar c'helligoù tro-dro
            #for k in tostan.amezeien:
            #    k.dizoloet = True
            next_player()


def init_game():
    # (Ad)kregiñ ar partienn
    global choarierien
    global n_choarier
    global n_taol
    
    # Dasparzhañ talvoudoù ar gelligoù
    # Talvoudoù bras a vo raloc'h eget talvoudoù bihan
    for k in kelligou:
        k.aloubet_gant = None
        k.is_uzin = False
        if len(k.amezeien) < 6:
            k.talvoud = 1
            k.tliv = 1
            k.dizoloet = True
        else:
            r = random(100)
            if r < 50:
                k.talvoud = 1
                k.tliv = 1
            elif r < 70:
                k.talvoud = 2
                k.tliv = 5
            elif r < 81:
                k.talvoud = 3
                k.tliv = 10
            elif r < 93:
                k.talvoud = 4
                k.tliv = 18
            else:
                k.talvoud = 5
                k.tliv = 24
    
    # Krouiñ c'hoarierien
    liviou = [
              color(130, 180, 30),
              color(30, 240, 70),
              color(240, 30, 240),
              color(120, 127, 220),
              color(255, 90, 110),
              color(100, 240, 240)
            ]
    shuffle(liviou)    # Meskañ al livioù
    choarierien = []
    for i in range(NIVER_CHOARIERIEN):
        choarierien.append(Choarier("C'hoarier " + str(i+1), liviou[i]))
    n_choarier = -1
    n_taol = 1
    next_player()
    

def next_player():
    global n_choarier # Niverenn ar c'hoarier
    global n_taol
    global t_choarier # Amzer o tremen e kerz tro ar c'hoarier
    
    # Tremen d'ar c'hoarier da-heul
    n_choarier += 1
    if n_choarier >= len(choarierien):
        n_choarier = 0
        n_taol += 1
    
    choarier = choarierien[n_choarier]
    t_choarier = 0
    
    #Reiñ poentoù
    for k in kelligou:
        if k.aloubet_gant == choarier and k.is_uzin:
            choarier.poentou += k.talvoud

    choarier.update()
    if not choarier.bev:
        next_player()


class Choarier:
    def __init__(self, anv, liv):
        self.anv = anv
        self.liv = liv
        self.poentou = 1
        self.bev = True
    
    def trochan(self):
        # Mirout an tiriadoù liammet da uzinoù nemetken
        self.update()
            
        liammet = set()
        da_liamman = self.uzinou[:]
        while len(da_liamman) > 0:
            kellig = da_liamman.pop()
            liammet.add(kellig)
            for amezeg in kellig.amezeien:
                if amezeg.aloubet_gant == self and amezeg not in liammet:
                    da_liamman.append(amezeg)
        
        da_zieubin = set(self.kelligou_aloubet).difference(liammet)
        for k in da_zieubin:
            k.aloubet_gant = None
        
        self.update()
    
    
    def update(self):
        # Dizoloiñ an taolioù posupl e pep tro
        self.taoliou_aloubin = set()
        self.taoliou_tagan = set()
        self.taoliou_sevel = []
        self.kelligou_aloubet = []
        self.uzinou = []
        self.feuriou_tagan = dict()
        
        if n_taol == 1 and self.poentou == 1:
            # Kentañ taol, kelligoù ar vord a c'hell bezañ aloubet
            for k in kelligou:
                if len(k.amezeien) < 6 and k.aloubet_gant == None:
                    re_tost = False
                    for amezeg in k.amezeien:
                        if amezeg.aloubet_gant != None:
                            re_tost = True
                            break
                    if not re_tost:
                        self.taoliou_aloubin.add(k)
        else:
            for k in kelligou:
                if k.aloubet_gant == self:
                    self.kelligou_aloubet.append(k)
                    
                    if k.is_uzin:
                        self.uzinou.append(k)
                    elif self.poentou >= k.talvoud * 2:
                        self.taoliou_sevel.append(k)       
                                     
                    for amezeg in k.amezeien:
                        # Toud ar gelligoù a zo tro-dro d'ar c'hoarier
                        if amezeg.aloubet_gant == None:
                            if self.poentou >= amezeg.talvoud:
                                self.taoliou_aloubin.add(amezeg)                          
                        elif amezeg.aloubet_gant != self and self.poentou >= amezeg.talvoud * 2:
                            # A-walc'h a poentoù evit tagañ an amezeg-mañ
                            # Jedet e vo ar feur tagañ amañ ha lakaet er geriadur "taoliou_tagan"
                            enebour = amezeg.aloubet_gant
                            skor_tagan = 0
                            skor_difenn = 2 * amezeg.talvoud
                            for k in amezeg.amezeien:
                                if k.aloubet_gant == self:
                                    skor_tagan = skor_tagan + k.talvoud
                                elif k.aloubet_gant == enebour:
                                    skor_difenn = skor_difenn + k.talvoud
                            skor_hollek = (skor_tagan - skor_difenn)/9.0
                            skor_hollek = max(-0.48, min(skor_hollek, 0.48))
                            feur_gounid = (0.5 + skor_hollek)*100
                            self.feuriou_tagan[amezeg] = feur_gounid
                            self.taoliou_tagan.add(amezeg)
        if len(self.uzinou) == 0 and n_taol > 1:
            self.bev = False
        

class Kellig:
    def __init__(self, x, y):
        self.pos = PVector(x, y)
        self.talvoud = 0
        self.tliv = 0
        self.dizoloet = True
        self.amezeien = set()
        self.aloubet_gant = None  # 'None' m'a n'eo ket bet aloubet, ar c'hoarier perc'hen mod-all (class Choarier)
        self.is_uzin = False
    
    def draw(self):
        # Fonksion galvet evit tresañ pep kellig
        
        if self.dizoloet:
            
            fill(110 - self.tliv * 1.2, 110 - self.tliv * 1, 130 - self.tliv * 3)
            draw_hex(self.pos.x, self.pos.y, self.rad)
            
            if self.aloubet_gant != None:
                # Tresañ merk liv ar c'hoarier 'n eus aloubet ar c'hellig mañ
                pushStyle()
                fill(self.aloubet_gant.liv)
                if self.is_uzin:
                    circle(self.pos.x, self.pos.y, S*1.4)
                else:
                    circle(self.pos.x, self.pos.y, S*1.0)
                stroke(self.aloubet_gant.liv)
                strokeWeight(S*0.5)
                for k in self.amezeien:
                    if self.aloubet_gant == k.aloubet_gant:
                        line(self.pos.x, self.pos.y, k.pos.x, k.pos.y)
                popStyle()
                
        else:
            n = noise(self.pos.x * 10, self.pos.y * 10) * 44
            fill(220-n, 230-n, 190-n)
            draw_hex(self.pos.x, self.pos.y, self.rad)

    def draw_above(self):
        # Skrivañ talvoud ar c'hellig above dezhi
        if self.dizoloet == True:
            if self.is_uzin:
                fill(30, 30, 0, 100)
                draw_uzin(int(self.pos.x - S*0.425), int(self.pos.y - S*0.425), S*0.85)
            fill(255)
            textSize(22)
            text(self.talvoud, self.pos.x-7, self.pos.y+7)



def draw_hex(posx, posy, rad):
    h = rad * sin(radians(60))
    beginShape();
    vertex(posx, posy - rad)
    vertex(posx + h, posy - rad*0.5)
    vertex(posx + h, posy + rad*0.5)
    vertex(posx, posy + rad)
    vertex(posx - h, posy + rad*0.5)
    vertex(posx - h, posy - rad*0.5)
    endShape(CLOSE);


def draw_uzin(posx, posy, h):
    a = h/4
    beginShape();
    vertex(posx, posy)             #0
    vertex(posx, posy + h)         #1
    vertex(posx + h, posy + h)     #2
    vertex(posx + h, posy + a)     #3
    vertex(posx + 3*a, posy + 2*a) #4
    vertex(posx + 3*a, posy + a)   #5
    vertex(posx + 2*a, posy + 2*a) #6
    vertex(posx + 2*a, posy + a)   #7
    vertex(posx + a, posy + 2*a)   #8
    vertex(posx + a, posy)         #9
    endShape(CLOSE);


def sevel_kael(n, rad):
    Kellig.rad = rad
    kreizX = width*0.5
    kreizY = height*0.5
    d = rad * sin(radians(60))
    d2 = 2 * d
    x0 = kreizX - (n-1) * d2
    y0 = kreizY
    
    for i in range(2*n - 1):
        kelligou.append(Kellig(x0 + i*d2, kreizY))
    
    for i in range(1, n):
        xi = x0 + i * d
        yi_down = y0 + i * (rad + 0.5 * d)
        yi_up = y0 - i * (rad + 0.5 * d)
        for j in range(2*n - 1 - i):
            kelligou.append(Kellig(xi + j*d2, yi_down))
            kelligou.append(Kellig(xi + j*d2, yi_up))
    
    
def keyPressed():
    if key == 'p':
        # Saveteet e vez ur poltred-skramm
        saveFrame("strategiezh_###.png")
        println("Poltred-scramm saveteet")
    elif key == 'r':
        # Adkregiñ ar c'hoari
        init_game()
