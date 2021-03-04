import bs4, requests, webbrowser
#Inserisci il link
link = "https://www.ebay.it/sch/i.html?_dcat=80053&_fsrp=1&_nkw=monitor&_sacat=0&_udhi=100&_from=R40&LH_BIN=1&LH_ItemCondition=1000&Risoluzione%2520massima=1920%2520x%25201080%7C%21&Frequenza%2520di%2520aggiornamento=76%2520Hz%7C75%2520Hz%7C%21&_sop=12"

#Inserisci il link uguale per le pagine dei prodotti
Pre_link_annuncio = "https://www.ebay.it/itm"

response = requests.get(link)

response.raise_for_status()

soup = bs4.BeautifulSoup(response.text, 'html.parser')

#Inserisci la classe del div da controllare (il div è dove si trova immagine e nome prodotto per trovare gli <a> link
div_annunci = soup.find('div', class_='srp-river srp-layout-inner')
a_annunci = div_annunci.find_all('a')

link_annunci = []

for a_annuncio in a_annunci:
    link_annuncio = str(a_annuncio.get('href'))
    
    if Pre_link_annuncio in link_annuncio:
        link_annunci.append(link_annuncio)

#from pprint import pprint #prove per vede se funziona
#pprint(link_annunci)
        
f = open('risultati_salvati.txt', 'a')

old_link_annunci = [riga.rstrip('\n\n') for riga in open ('risultati_salvati.txt')]

new_link_annunci = []

for link_annuncio in link_annunci:
    if link_annuncio not in old_link_annunci:
        new_link_annunci.append(link_annuncio)
        f.write('%s\n\n' % link_annuncio)
        
f.close()

if new_link_annunci:
    print("Ci sono nuovi risultati")
    
    for new_link in new_link_annunci:
        print("apri o chiudi pagina?") #per evitare spam che si aprono controll stringa inserita se è apri, apri pagine
        Apri=input().upper()
        if(Apri == 'APRI'):
            webbrowser.open(new_link)
        else:
            break
else:
    print("Nessuno annuncio trovato")
    
