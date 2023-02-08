from random import shuffle


class Choarier:
    def __init__(self, anv, liv):
        self.anv = anv
        self.liv = liv
        self.taol_kentan = True


class Kellig:
    def __init__(self, x, y):
        self.pos = PVector(x, y)
        self.value = int(random(1, 6))
        self.dizoloet = False
        self.amezog = set()
    
    def draw(self):
        if self.dizoloet:
            fill(100 + self.value * 24, 100, 255);
            draw_hex(self.pos.x, self.pos.y, self.rad)
            fill(255)
            textSize(20)
            text(self.value, self.pos.x-5, self.pos.y+5)
            fill(255)
        else:
            fill(200)
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
    N = 8 # Niver a c'hellig dre kostez
    S = 25 # Ment pep kellig (e pixel)
    sevel_kael(N, S)
    
    # Klask an amezeien tro-dro pep kellig
    for k1 in kelligou:
        for k2 in kelligou:
            if dist(k1.pos.x, k1.pos.y, k2.pos.x, k2.pos.y) < 2*S+5 and k1 != k2:
                k1.amezog.add(k2)


def draw():
    global tostan
    
    background(255)
    
    choarier = choarierien[n_choarier]
    fill(choarier.liv)
    noStroke()
    circle(20, 20, 20)
    fill(0)
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
    global n_choarier
    
    if tostan and not tostan.dizoloet:
        tostan.dizoloet = True
        # Dizoloiñ ar c'helligoù tro-dro
        for k in tostan.amezog:
            k.dizoloet = True
        
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
