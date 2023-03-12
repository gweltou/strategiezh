## 1 Meurzh 2023

Betek poent e c'heller c'hoari un taol n'eus forzh pelec'h war an tablez, memes an taol kentañ, padal e rankfe bezañ berzet taolioù 'zo. Da skouer, taol kentañ pep c'hoarier a rankfe bezañ war vord an tablez nemetken. Pep taol da-heul a rank bezañ stok diouzh tiriadoù perc'hennet dija.
Er fonksion <code>mousePressed</code> (galvet bep gwech ma vez kliket en ul lec'h bennak war ar prenestr), ar varienn <code>is_valid_move</code> a servijo deomp da wiriekañ ma'z eo bet graet un taol aotreet gant ar c'hoarier, pe get. Lakaet e vo an talvoud <code>False</code> gant ar varienn-se, dre ziouer.

### Berzañ an taol kentañ

Er c'hlasad (class) <code>Choarier</code> e vez kavet ur varienn <code>n_taol</code> evit mirout soñj eus an niver a daolioù a zo bet c'hoariet gant pep hini.
Bep gwech ma kliket war ur gellig vo tu sellet ouzh stad ar varienn-se, ha ma'z eo kevatal da 0 (taol kentañ) e vo aotreet da aloubiñ an tiriadoù war ar bord nemetken. Gouezet e vez ez eo un tiriad war ar bord p'en deus nebeutoc'h eget 6 amezeg (<code>len(Kellig.amezeien) < 6</code>)

```python
# Galvet bep gwech ma vez kliket er prenestr
def mousePressed():
    global n_choarier   # niverenn ar c'hoarier
    
    if tostan:
        # Kliket eo bet war ur c'hellig
        # Liammet eo bet ar c'hellig-se d'ar varienn 'tostan'
        
        is_valid_move = False
        if tostan.dizoloet and tostan.aloubet_gant == None:
            # Aloubet e vez ar c'hellig
            # ...
            is_valid_move = True
        elif not tostan.dizoloet:
            if choarierien[n_choarier].n_taol == 0 and len(tostan.amezeien) < 6:
                # Taol kentañ
                # ...
                is_valid_move = True
            
        if is_valid_move:
            # Dizoloiñ ar c'helligoù tro-dro
            # ha tremen d'ar c'hoarier da-heul
            # ..
```

### Diskouez an tiriadoù liammet

Evit ma teufe war vel gwelloc'h tiriadoù pep c'hoarier e vez treset ur c'helc'h liv ar c'hoarier dindan talvoud pep tiriad. Evit diskouez splannoc'h hollad an tiriadoù hag al liammoù etre pep kellig e tresimp linennoù tev etre pep kellig hag e amezeien, gant ma vezont aloubet gant ar memes c'hoarier.

Trugarez da Matilin ha Paolig da vezañ labouret war ar c'hod-se !

```python
class Kellig:
    # ...
    
    def draw(self):
        # Fonksion galvet evit tresañ pep kellig
        
        if self.dizoloet:
            # ...
            if self.aloubet_gant != None:
                # Tresañ merk liv ar c'hoarier n'eus aloubet ar c'hellig mañ
                
                pushStyle()  # envoreniñ stad ar "style" (liv, tevder a linennoù...)
                # ...
                for k in self.amezeien:
                    if self.aloubet_gant == k.aloubet_gant:
                        # Al linenn etre ar c'hellig-mañ ar ur c'hellig amezeg eus ar memes liv
                        line(self.pos.x, self.pos.y, k.pos.x, k.pos.y)
                popStyle()  # gervel ar "style" kozh en dro
            
            text(self.value, self.pos.x-5, self.pos.y+5) # Talvoud skrivet a-us ar c'hellig
        else:
            # tresañ ur c'hellig el latar
            # ...
```

![prototip3](skeudennou/20230301_19857.png)

_Daoust-hag e vo merzet ar bug ganeoc'h ? ;)_


## 8 Meurzh 2023

### Kempenn 'bug' sifr an talvoudoù

Echuet on oa, ar wech diwezhañ, en ul leuskel ur bugig grafik : sifr talvoud ar c'helligoù a oa kuzhet a-wechoù, abalamour ma veze treset linennoù ar c'helligoù amezeg a-us dezho.
Evit kempenn ar gudenn-se eo bet ret deomp rannañ ar fonksion `Kellig.draw` evit dispartiañ tresañ ar gellig diouzh tresañ sifr an talvoudoù. Tennet eo bet neuze al linennoù kod a drese an talvoudoù ha lakaet int bet en ur fonksion nevez, anvet `Kellig.draw_talvoud`, adskrivet dindan :

```python
# Kavet e vez ar fonskion se er c'hlas 'Kellig'
def draw_talvoud(self):
    # Skrivañ talvoud ar c'hellig a-us dezhi
    if self.dizoloet == True:
        fill(255)
        textSize(20)
        text(self.talvoud, self.pos.x-5, self.pos.y+5)
```

Galvet e vez ar fonksion nevez-se e diabarzh ar fonksion `draw` pennañ:

```python
# Tresañ ar c'hael a-bezh
noStroke()
for k in kelligou:
    k.draw()
for k in kelligou:
    k.draw_talvoud()
```

Evel-se e vo treset an holl kelligoù penn-da-benn (pep c'hwec'hgornek, livioù ar c'hoarierien hag all) a-raok tresañ pep talvoud a-us.

### Ur gael dizingal

Jeneret e oa talvoudoù pep kellig eus ar gael en un doare ankivil. Pep kellig en doa ar memes probablentez da gaout un talvoud etre 1 ha 5. C'hoant on eus bremañ e vefe raloc'h an talvoudoù bras eget an talvoudoù bihan.
Graet e vo se gant ar c'hod da-heul, lakaet er fonksion `setup`, war-lerc'h bezañ bet krouet ar gael.
Lakaet e vez un talvoud '1' da bep kellig eus ar bord (anavezet int dre m'o deus nebeutoc'h eget 6 amezeg).
Evit ar re all e vez goulennet un talvoud ankivil etre 0 ha 100, gant ar fonksion `random`, hag hervez an talvoud roet e vo dibabet talvoud ar gellig. Evel-se, 60% chañs vo da zibab an talvoud '1' evit ar gellig, 20% evit an talvoud '2', 10% evit an talvoud '3', 7% evit an talvoud '4' ha 3% evit an talvoud '5'.
Un doare dispar da ziskouez implij ar framm `if`-`elif`-`else`.

```python
for k in kelligou:
    if len(k.amezeien) < 6:
        k.talvoud = 1
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
```

### Gounid poentoù

Brav ha plijus e krog da vezañ klikañ pep lec'h ha brasaat tiriad pep c'hoarier met n'ez eus c'hoari ebet c'hoazh. Poent eo reiñ poentoù da bep c'hoarier e penn-kentañ pep taol. Graet e vo se er fonksion `mousePressed`, ma'z eo bet graet un taol aotreet.

```python
def mousePressed():
    # ...
    choarier = choarierien[n_choarier]
    # ...
    
    if is_valid_move:
        # Dizoloiñ ar c'helligoù tro-dro
        for k in tostan.amezeien:
            k.dizoloet = True
        
        # Tremen d'ar c'hoarier da-heul
        choarier.n_taol += 1
        n_choarier += 1
        if n_choarier >= len(choarierien):
            n_choarier = 0
        
        #Reiñ poentoù
        choarier.poentou += 1
```
