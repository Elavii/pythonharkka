import random

def tarkista_yatzy(heitto):
  """
  Tarkista onko heitto yatzy(5 samaa),
  jos on palauta 50, jos ei palauta 0
  """
  for i in range(1, 7):
    if heitto.count(i) == 5:
      return 50
  return 0

def tarkista_iso_suora(heitto):
  """
  Tarkista onko heitossa iso suora, jos on palauta 40,
  jos ei palauta 0
  """
  if sorted(heitto) == [1, 2, 3, 4, 5] or sorted(heitto) == [2, 3, 4, 5, 6]:
    return 40
  return 0

def tarkista_pieni_suora(heitto):
  """
  Tarkista onko heitossa pieni suora, jos on palauta 30,
  jos ei palauta 0.
  """
  for i in range(1, 7):
    if sorted(heitto) == list(range(i, i+4)):
      return 30
  return 0

def tarkista_tayskasi(heitto):
  """
  Tarkista onko heitossa täyskäsi(kolme samaa ja pari),
  jos on palauta 25 pistettä, jos ei palauta 0.
  """
  counts = {i: heitto.count(i) for i in range(1, 7)}
  if 3 in counts.values() and 2 in counts.values():
    return 25
  return 0

def tarkista_nelja_samaa(heitto):
  """
    Tarkista onko heitossa neljä samaa,
    jos on summaa ne, jos ei palauta 0
  """
  counts = {i: heitto.count(i) for i in range(1, 7)}
  for i, count in counts.items():
    if count >= 4:
      return i * 4
  return 0

def tarkista_kolme_samaa(heitto):
  """
    Tarkista onko heitossa kolme samaa,
    jos on summaa ne, jos ei palauta 0
  """
  counts = {i: heitto.count(i) for i in range(1, 7)}
  for i, count in counts.items():
    if count >= 3:
      return i * 3
  return 0

def tarkista_ykkoset(heitto):
  """
  Tarkista numeroita 1 heitossa.
  Palauta numero niin monta kertaa kuin se löytyy.
  """
  return heitto.count(1)

def tarkista_kakkoset(heitto):
  """
  Tarkista numeroita 1 heitossa.
  Palauta numero niin monta kertaa kuin se löytyy.
  """
  return heitto.count(2) * 2

def tarkista_kolmoset(heitto):
  """
  Tarkista numeroita 1 heitossa.
  Palauta numero niin monta kertaa kuin se löytyy.
  """
  return heitto.count(3) * 3

def tarkista_neloset(heitto):
  """
  Tarkista numeroita 1 heitossa.
  Palauta numero niin monta kertaa kuin se löytyy.
  """
  return heitto.count(4) * 4

def tarkista_vitoset(heitto):
  """
  Tarkista numeroita 1 heitossa.
  Palauta numero niin monta kertaa kuin se löytyy.
  """
  return heitto.count(5) * 5

def tarkista_kutoset(heitto):
  """
  Tarkista numeroita 1 heitossa.
  Palauta numero niin monta kertaa kuin se löytyy.
  """
  return heitto.count(6) * 6

def yatzy():
  # Alusta tulokset
  tulokset = [0, 0]
  nimet = ["Pelaaja 1", "Pelaaja 2"]

  # Pelaa kaksi kierrosta
  for i in range(2):
    print(f"Kierros {i+1}:")
    for j in range(2):
      print(f"{nimet[j]}:")
      # heittää 5 noppaa
      heitto = []
      for k in range(5):
        heitto.append(random.randint(1, 6))
      # Voi hettää uudelleen kaksi kertaa
      for k in range(2):
        print(f"heitto {k+1}: {heitto}")
        ok_syote = False
        while not ok_syote:
          uudelleenheitto = input("Kirjoita sen nopan paikka, jota haluat heittää uudelleen(Esim '1 2 4'), jos et halua heittää uudelleen paina Enter: ")
          if uudelleenheitto == "":
            ok_syote = True
          elif uudelleenheitto:
            try:
              uudelleenheitto = [int(x) for x in uudelleenheitto.split()]
              for l in uudelleenheitto:
                if l < 1 or l > 5:
                  raise ValueError
              ok_syote = True
              for l in uudelleenheitto:
                heitto[l-1] = random.randint(1, 6)
            except ValueError:
              print("Väärä syöte katso esimerkkisyötettä yläpuolella")
      # Laske tulos heitolle
      print(f"heitto 3: {heitto}")
      tulos = 0
      tulos_mahdollisuudet = [tarkista_yatzy(heitto), tarkista_iso_suora(heitto), tarkista_pieni_suora(heitto), tarkista_tayskasi(heitto), tarkista_nelja_samaa(heitto), tarkista_kolme_samaa(heitto), tarkista_ykkoset(heitto), tarkista_kakkoset(heitto), tarkista_kolmoset(heitto), tarkista_neloset(heitto), tarkista_vitoset(heitto), tarkista_kutoset(heitto)]
      tulos_mahdollisuudet = [x for x in tulos_mahdollisuudet if x > 0]
      if tulos_mahdollisuudet:
        tulos = max(tulos_mahdollisuudet)
      # Päivitä tulos pelaajalle(valitsee aina suurimman tuloksen)
      tulokset[j] += tulos
      print(f"{nimet[j]} sai {tulos} pistettä tällä kierroksella.")

  # Määritä voittaja
    if tulokset[0] > tulokset[1]:
        print(f"{nimet[0]} voittaa tuloksella: {tulokset[0]}!")
    elif tulokset[1] > tulokset[0]:
        print(f"{nimet[1]} voittaa tuloksella: {tulokset[1]}!")
    else:
        print("Tasapeli")
    
    with open("yatzy_tulokset.txt", "w") as tulostiedosto:

    # Kirjoita lopputulokset tiedostoon
        tulostiedosto.write(f"Viime pelin tulokset:\n")
        tulostiedosto.write(f"Pelaajan 1 lopputulos: {tulokset[0]}\n")
        tulostiedosto.write(f"Pelaajan 2 lopputulos: {tulokset[1]}\n")

# Kutsu peliä
yatzy()