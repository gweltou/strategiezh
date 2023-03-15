#ANV AR C'HOARI

from random import shuffle


N = 5 # Niver a c'hellig dre kostez
S = 30 # Ment pep kellig (e pixel)


kelligou = []
choarierien = []

def setup():
    size(500, 500)
    
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
    
    # Dasparzhañ talvoudoù ar gelligoù
    # Talvoudoù bras a vo raloc'h eget talvoudoù bihan
    for k in kelligou:
        if len(k.amezeien) < 6:
            k.talvoud = 1
            k.dizoloet = True
        else:
            r = random(100)
            if r < 60:
                k.talvoud = 1
            elif r < 80:
                k.talvoud = 2
            elif r < 90:
                k.talvoud = 3
            elif r < 97:
                k.talvoud = 4
            else:
                k.talvoud = 5
    
    
    # Krouiñ c'hoarierien
    NIVER_CHOARIERIEN = 3
    liviou = [
              color(130, 180, 30),
              color(30, 240, 50),
              color(240, 30, 240),
              color(120, 127, 220),
              color(255, 90, 110),
              color(100, 240, 240)
            ]
    shuffle(liviou)    # Meskañ al livioù
    for i in range(NIVER_CHOARIERIEN):
        choarierien.append(Choarier("C'hoarier " + str(i+1), liviou[i]))
    global n_choarier
    n_choarier = -1
    next_player()


def draw():
    global tostan
    global t_choarier
    
    background(220 * 0.4, 230 * 0.4, 190 * 0.4)
    
    choarier = choarierien[n_choarier]
    t_choarier += 1
        
    # Klask ar c'hellig an tostañ eus ar logodenn
    min_dist = 999.0
    tostan = None
    for k in kelligou:
        d = dist(mouseX, mouseY, k.pos.x, k.pos.y)
        if d < Kellig.rad and d < min_dist:
            min_dist = d
            tostan = k
    
    # Tresañ ar c'hael a-bezh
    noStroke()
    for k in kelligou:
        k.draw()
    for k in choarier.taoliou_aloubin:
        # Livañ a-us d'ar c'helligoù a c'hell bezañ aloubet gant ar c'hoarier
        fill(choarier.liv, (1+cos(t_choarier * 0.1) * 60))
        draw_hex(k.pos.x, k.pos.y, k.rad)
    for k in kelligou:
        k.draw_talvoud()
    
    # Ad-tresañ an hini dindan al logodenn met ruz ha damdreuzwelus
    if tostan:
        stroke(0)
        fill(255, 0, 0, 100)
        draw_hex(tostan.pos.x, tostan.pos.y, tostan.rad)
    
    # HUD ar c'hoarier
    fill(choarier.liv)
    noStroke()
    circle(20, 20, 35)
    fill(255)
    textSize(20)
    text(choarier.anv, 40, 27)
    text(choarier.poentou, 14, 27)



def mousePressed(): 
    if tostan:
        # Kliket eo bet war ur c'hellig
        
        choarier = choarierien[n_choarier]
        is_valid_move = False
        if tostan in choarier.taoliou_aloubin:
            tostan.aloubet_gant = choarier
            choarier.poentou -= tostan.talvoud
            is_valid_move = True
        
        if is_valid_move:
            # Dizoloiñ ar c'helligoù tro-dro
            for k in tostan.amezeien:
                k.dizoloet = True
            
            choarier.n_taol += 1
            next_player()
    
    else:
        # Kliket eo bet e diavaez ar gael
        next_player()


def next_player():
    # Niverenn ar c'hoarier,
    # etre 0 (c'hoarier kentañ) ha 3 (evit ar pevare c'hoarier)
    global n_choarier
    
    global t_choarier # Amzer o tremen e kerz tro ar c'hoarier
    
    # Tremen d'ar c'hoarier da-heul
    n_choarier += 1
    if n_choarier >= len(choarierien):
        n_choarier = 0
    
    choarier = choarierien[n_choarier]
    choarier.update_taoliou_aloubin()
    
    t_choarier = 0
    
    #Reiñ poentoù
    choarier.poentou += 1


class Choarier:
    def __init__(self, anv, liv):
        self.anv = anv
        self.liv = liv
        self.n_taol = 0
        self.poentou = 1
        self.taoliou_aloubin = set()
    
    def update_taoliou_aloubin(self):
        # Dizoloiñ an taolioù aloubin posupl e pep tro
        
        if self.n_taol == 0:
            for k in kelligou:
                if len(k.amezeien) < 6 and k.aloubet_gant == None:
                    self.taoliou_aloubin.add(k)
        else:
            self.taoliou_aloubin.clear()
            for k in kelligou:
                if k.aloubet_gant == None:
                    for amezeg in k.amezeien:
                        if amezeg.aloubet_gant == self and k.talvoud <= self.poentou:
                            self.taoliou_aloubin.add(k)
                            break            
        

class Kellig:
    def __init__(self, x, y):
        self.pos = PVector(x, y)
        self.talvoud = 0
        self.dizoloet = True
        self.amezeien = set()
        self.aloubet_gant = None  # 'None' m'a n'eo ket bet aloubet, ar c'hoarier perc'hen mod-all (class Choarier)
    
    def draw(self):
        # Fonksion galvet evit tresañ pep kellig
        
        if self.dizoloet:
            val2 = self.talvoud * self.talvoud
            fill(val2 * 2, val2 * 4, val2 * 2.5)
            draw_hex(self.pos.x, self.pos.y, self.rad)
            
            if self.aloubet_gant != None:
                # Tresañ merk liv ar c'hoarier n'eus aloubet ar c'hellig mañ
                pushStyle()
                fill(self.aloubet_gant.liv)
                circle(self.pos.x, self.pos.y, S*1.3)
                stroke(self.aloubet_gant.liv)
                strokeWeight(S*0.7)
                for k in self.amezeien:
                    if self.aloubet_gant == k.aloubet_gant:
                        line(self.pos.x, self.pos.y, k.pos.x, k.pos.y)
                popStyle()
                
        else:
            n = noise(self.pos.x * 10, self.pos.y * 10) * 44
            fill(220-n, 230-n, 190-n)
            draw_hex(self.pos.x, self.pos.y, self.rad)

    def draw_talvoud(self):
        # Skrivañ talvoud ar c'hellig a-us dezhi
        if self.dizoloet == True:
            fill(255)
            textSize(20)
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
    # Saveteet e vez ur poltred-skramm
    if key == 'p':
        saveFrame("strategiezh_###.png")
        println("Poltred-scramm saveteet")
