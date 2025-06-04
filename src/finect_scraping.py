from bs4 import BeautifulSoup
import requests

finect_url = "https://www.finect.com/fondos-inversion/IE00BYX5NX33-Fidelity_msci_world_index_eur_p_acc"
#Maybe i need the headers to avoid being blocked

response = requests.get(finect_url)

soup = BeautifulSoup(response.text, 'html.parser')

# Extract the html when we only know the class name
html_div = soup.find_all('div', class_="partials__Column-sc-jtcrtv-4 partials__HeaderColumn-sc-jtcrtv-5 goFpZn cQIrrR")
#html_span = soup.find_all('span', class_="Label-sc-1esfagn-0 gCsBVA")
 
#RESUMEN

# TabChild-sc-e313xw-0 xkoFx
# partials__Inner-sc-jtcrtv-0 dVBgww
# partials__RowBlock-sc-jtcrtv-3 gPFXSc SI ES NUMERO O LETRA
# partials__Column-sc-jtcrtv-4 dWvuOc SI ES UNA FECHA

# Aquí dentro está el nombre de la caracterísitca y separado el valor

# partials__Column-sc-jtcrtv-4 partials__HeaderColumn-sc-jtcrtv-5 goFpZn cQIrrR NOMBRE
# AppLink-sc-1iw8l8l-0 dayaFw VALOR
# partials__Column-sc-jtcrtv-4 dWvuOc VALOR SI ES EL ULTIMO


# COMISIONES
# TabChild-sc-e313xw-0 xkoFx
# partials__Inner-sc-jtcrtv-0 dVBgww
# partials__RowBlock-sc-jtcrtv-3 gPFXSc 

# partials__Column-sc-jtcrtv-4 partials__HeaderColumn-sc-jtcrtv-5 goFpZn cQIrrR NOMBRE

# partials__Column-sc-jtcrtv-4 dWvuOc
# Label-sc-1esfagn-0 gCsBVA VALOR

# RATIOS 1 año
# TabChild-sc-e313xw-0 xkoFx
# partials__Inner-sc-jtcrtv-0 dVBgww
# partials__RowBlock-sc-jtcrtv-3 gPFXSc

# partials__Column-sc-jtcrtv-4 partials__HeaderColumn-sc-jtcrtv-5 goFpZn cQIrrR NOMBRE

# partials__Column-sc-jtcrtv-4 dWvuOc
# Label-sc-1esfagn-0 gCsBVA VALOR
# partials__RowBlock-sc-jtcrtv-3 eggwXa VALOR SI ES EL ULTIMO





print(html_div)