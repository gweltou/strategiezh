#ANV AR C'HOARI

from random import shuffle


N = 8 # Niver a c'hellig dre kostez
S = 25 # Ment pep kellig (e pixel)


class Choarier:
    def __init__(self, anv, liv):
        self.anv = anv
        self.liv = liv
        self.n_taol = 0


class Kellig:
    def __init__(self, x, y):
        self.pos = PVector(x, y)
        self.value = int(random(1, 6))
        self.dizoloet = False
        self.amezeien = set()
        self.aloubet_gant = None  # 'None' m'a n'eo ket bet aloubet, niveren ar c'hoarier perc'hen mod-all
    
    def draw(self):
        # Fonksion galvet evit tresañ pep kellig
        
        if self.dizoloet:
            val2 = self.value * self.value
            fill(val2 * 2, val2 * 4, val2 * 2.5)
            draw_hex(self.pos.x, self.pos.y, self.rad)
            
            if self.aloubet_gant != None:
                # Tresañ merk liv ar c'hoarier n'eus aloubet ar c'hellig mañ
                pushStyle()
                fill(choarierien[self.aloubet_gant].liv)
                circle(self.pos.x, self.pos.y, S*1.3)
                stroke(choarierien[self.aloubet_gant].liv)
                strokeWeight(S*0.7)
                for k in self.amezeien:
                    if self.aloubet_gant == k.aloubet_gant:
                        line(self.pos.x, self.pos.y, k.pos.x, k.pos.y)
                popStyle()
                
            fill(255)
            textSize(20)
            text(self.value, self.pos.x-7, self.pos.y+7)
        else:
            n = noise(self.pos.x * 10, self.pos.y * 10) * 44
            fill(220-n, 230-n, 190-n)
            draw_hex(self.pos.x, self.pos.y, self.rad)



kelligou = []
choarierien = []

def setup():
    size(800, 600)
    
    # Krouiñ c'hoarierien
    NIVER_CHOARIERIEN = 3
    liviou = [
              color(130, 180, 30),
              color(30, 255, 50),
              color(240, 30, 255),
              color(120, 127, 220),
              color(255, 90, 110),
              color(90, 250, 255)
            ]
    shuffle(liviou)    # Meskañ al livioù
    for i in range(NIVER_CHOARIERIEN):
        choarierien.append(Choarier("C'hoarier " + str(i+1), liviou[i]))
    global n_choarier
    n_choarier = 0
    
    # Amañ e vez dibabet ment an tablez
    sevel_kael(N, S)
    
    # Klask an amezeien tro-dro pep kellig
    for k1 in kelligou:
        for k2 in kelligou:
            if dist(k1.pos.x, k1.pos.y, k2.pos.x, k2.pos.y) < 2*S+5 and k1 != k2:
                k1.amezeien.add(k2)


def draw():
    global tostan
    
    background(220 * 0.4, 230 * 0.4, 190 * 0.4)
    
    choarier = choarierien[n_choarier]
    fill(choarier.liv)
    noStroke()
    circle(20, 20, 20)
    fill(255)
    textSize(20)
    text(choarier.anv, 40, 27)
    
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
    
    # Ad-tresañ an hini dindan al logodenn
    if tostan:
        stroke(0)
        fill(255, 0, 0, 100)
        draw_hex(tostan.pos.x, tostan.pos.y, tostan.rad)



def mousePressed():
    # Niverenn ar c'hoarier,
    # etre 0 (c'hoarier kentañ) ha 3 (evit ar pevare c'hoarier)
    global n_choarier  
    
    if tostan:
        # Kliket eo bet war ur c'hellig
        
        is_valid_move = False
        if tostan.dizoloet and tostan.aloubet_gant == None:
            # Ar c'hoarier a aloub anezhi ma'z eo bet dizoloet ha m'a n'eo ket bet aloubet dija
            for k in tostan.amezeien: # Sellet m'az eo bet dija aloubet ur c'hellig amezeg  ### NEW
                if k.aloubet_gant == n_choarier:   ### NEW
                    tostan.aloubet_gant = n_choarier   ### NEW
                    is_valid_move = True
                    break   ### NEW
        
        elif not tostan.dizoloet:
            if choarierien[n_choarier].n_taol == 0 and len(tostan.amezeien) < 6:
                # Taol kentañ
                tostan.dizoloet = True
                tostan.aloubet_gant = n_choarier
                is_valid_move = True
            
        if is_valid_move:
            # Dizoloiñ ar c'helligoù tro-dro
            for k in tostan.amezeien:
                k.dizoloet = True
            
            # Tremen d'ar c'hoarier da-heul
            choarierien[n_choarier].n_taol += 1
            n_choarier += 1
            if n_choarier >= len(choarierien):
                n_choarier = 0


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
