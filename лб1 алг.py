# ==========================================
# 1. КЛАС: АСТРОНАВТ
# ==========================================
class Astronaut:
    def __init__(self, name, role, health, oxygen, status):
        self.name = name                 
        self.role = role                 
        self.health = health             
        self.oxygen = oxygen  
        self.status = status             

    def rabota(self, chto_delat):
        self.health = self.health - 15
        self.status = "Працює"
        print(self.name, "робить роботу:", chto_delat, ". Здоров'я тепер:", self.health)

    def otdih(self):
        self.health = self.health + 20
        self.status = "Спить"
        print(self.name, "пішов відпочивати. Здоров'я піднялося до:", self.health)


# ==========================================
# 2. КЛАС: ВАНТАЖ
# ==========================================
class Cargo:
    def __init__(self, name, ves, tip, temperatura, zakreplen):
        self.name = name               
        self.ves = ves             
        self.tip = tip     
        self.temperatura = temperatura  
        self.zakreplen = zakreplen     

    def proverka_temperaturi(self, t_v_korable):
        if t_v_korable > self.temperatura:
            print("Увага! Вантаж", self.name, "може зіпсуватися через спеку!")
            return False
        else:
            print("З вантажем", self.name, "все нормально.")
            return True

    def prikrepit(self):
        if self.zakreplen == True:
            self.zakreplen = False
            print("Вантаж", self.name, "відчеплений.")
        else:
            self.zakreplen = True
            print("Вантаж", self.name, "закріплений у трюмі.")


# ==========================================
# 3. КЛАС: ДВИГУН
# ==========================================
class Engine:
    def __init__(self, model, moshnost, temp, rashod, rabotaet):
        self.model = model               
        self.moshnost = moshnost 
        self.temp = temp   
        self.rashod = rashod  
        self.rabotaet = rabotaet               

    def vkluchit(self):
        self.rabotaet = "Так"
        self.temp = 350
        print("Двигун", self.model, "запущений! Температура:", self.temp)

    def ohladit(self):
        self.temp = self.temp - 100
        print("Двигун трохи охолов. Температура:", self.temp)


# ==========================================
# 4. КЛАС: ЖИТТЄЗАБЕЗПЕЧЕННЯ
# ==========================================
class LifeSupport:
    def __init__(self, vozduh, davlenie, gradus, nagruzka, status):
        self.vozduh = vozduh 
        self.davlenie = davlenie         
        self.gradus = gradus   
        self.nagruzka = nagruzka  
        self.status = status             

    def potrablenie(self, chel1, chel2):
        vsego_rashod = chel1.oxygen + chel2.oxygen
        self.vozduh = self.vozduh - vsego_rashod
        print("Екіпаж подихав. Кисню залишилося:", self.vozduh)

    def pomenyat_temp(self, novaya_t):
        self.gradus = novaya_t
        print("Всередині корабля тепер кондиціонер на", self.gradus, "градусів.")


# ==========================================
# 5. КЛАС: КОРАБЕЛЬ (ГОЛОВНИЙ)
# ==========================================
class Spaceship:
    def __init__(self, imya, toplivo, dvigatel, jizn, mesta):
        self.imya = imya                 
        self.toplivo = toplivo         
        self.dvigatel = dvigatel  
        self.jizn = jizn          
        self.mesta = mesta 
        self.ekipaj = []                   
        self.truym = []                   

    def dobavit_astronavta(self, astro):
        self.ekipaj.append(astro)
        print("На корабель", self.imya, "зайшов", astro.name)

    def dobatit_gruz(self, tovar):
        if len(self.truym) < self.mesta:
            self.truym.append(tovar)
            print("Поклали вантаж", tovar.name, "в трюм.")
        else:
            print("Місця немає!")

    def zapusk_vsego(self):
        print("\n--- ПОЧИНАЄТЬСЯ СИМУЛЯЦІЯ ---")
        
        self.dvigatel.vkluchit()
        self.toplivo = self.toplivo - self.dvigatel.rashod
        
        chel1 = self.ekipaj[0]
        chel2 = self.ekipaj[1]
        
        chel1.rabota("Лагодження керма")
        self.jizn.potrablenie(chel1, chel2)
        
        gruz1 = self.truym[0]
        gruz1.proverka_temperaturi(self.jizn.gradus)
        
        print("Кінець симуляції. Палива залишилося:", self.toplivo)
        print("-----------------------------\n")


# ==========================================
# ПЕРЕВІРКА КОДУ (ВИВІД У КОНСОЛЬ)
# ==========================================
if __name__ == "__main__":
    motor = Engine("Vortex-V", 4000, 20, 50, "Ні")
    climat = LifeSupport(500, 1, 22, 10, "ОК")

    ship = Spaceship("Apollo", 1000, motor, climat, 2)

    p1 = Astronaut("Олег", "Капітан", 100, 12, "Готовий")
    p2 = Astronaut("Ігор", "Інженер", 100, 10, "Готовий")
    box = Cargo("Ящик їжі", 100, "Їжа", 25, True)

    ship.dobavit_astronavta(p1)
    ship.dobavit_astronavta(p2)
    ship.dobatit_gruz(box)

    ship.zapusk_vsego()
