import requests
import re

url = input('Inserte la url:')
#url = "https://www.uanl.mx/enlinea/"

response = requests.get(url)
if response.status_code != 200:
    exit()

regex = r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"
busqueda = set(re.findall(regex, response.text, re.I))

escritura = open("emails.txt", "a")
escritura.write("Lista de emails encontrados:")
if len(busqueda) != 0:
  for email in busqueda:
      escritura.write("\n")
      escritura.write(email)
else:
  escritura.write("No se encontraron emails")
escritura.close()

print("Todo está listo!")
