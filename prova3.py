def ita_ing():
    dizionario_giorni = {}
    for g in range(7):
        giorni = input("inserire giorno" + str(g+1)).split(",")
        dizionario_giorni[giorni[0].strip()] = giorni[1].strip()
    return dizionario_giorni
def ing_ita(dizionario_giorni):
    dizionario_giorni_2 = {}
    for giorno in diz:
        dizionario_giorni_2(dizionario_giorni[giorno]) = giorno
    return dizionario_giorni_2
def main():
    giorni_settimana = ita_ing()
    mostra_giorni_settimana(giorni_settimana)
    week_days = ing_ita(settimana)
    mostra_giorni_settimana(week_days)


main()