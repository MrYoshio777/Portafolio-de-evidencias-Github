#Deivi Rodriguez Rangel
from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image
import os
from os import path
import requests, bs4
import argparse

#NOTA: El manejo de la url es dinámica
#Argumentos del argparse
if __name__ == "__main__":
  description="""El script tiene como finalidad
  obtener metadata de las imágenes contenidas en la página de la UANL
  con fines didácticos, para su uso correcto debe usar el siguiente url:
          -url "https://www.uanl.mx/" """
  parser = argparse.ArgumentParser(description="E11", epilog=description,
  formatter_class=argparse.RawDescriptionHelpFormatter)
  parser.add_argument('-url', type=str, help='Se debe ingresar un link',
  default="https://www.uanl.mx/")
  params = parser.parse_args()
  url = (params.url)

#Extracción de metadata de imágenes
def decode_gps_info(exif):
  gpsinfo = {}
  if 'GPSInfo' in exif:
    #Parse geo references.
    Nsec = exif['GPSInfo'][2][2]
    Nmin = exif['GPSInfo'][2][1]
    Ndeg = exif['GPSInfo'][2][0]
    Wsec = exif['GPSInfo'][4][2]
    Wmin = exif['GPSInfo'][4][1]
    Wdeg = exif['GPSInfo'][4][0]
    if exif['GPSInfo'][1] == 'N':
      Nmult = 1
    else:
      Nmult = -1
    if exif['GPSInfo'][3] == 'E':
      Wmult = 1
    else:
      Wmult = -1
    Lat = Nmult * (Ndeg + (Nmin + Nsec / 60.0) / 60.0)
    Lng = Wmult * (Wdeg + (Wmin + Wsec / 60.0) / 60.0)
    exif['GPSInfo'] = {"Lat": Lat, "Lng": Lng}
    input()

def get_exif_metadata(image_path):
  ret = {}
  image = Image.open(image_path)
  if hasattr(image, '_getexif'):
      exifinfo = image._getexif()
      if exifinfo is not None:
          for tag, value in exifinfo.items():
              decoded = TAGS.get(tag, tag)
              ret[decoded] = value
  decode_gps_info(ret)
  return ret
print("\nObteniendo imagenes del link: "+ url)

try:
  response = requests.get(url)
  soup = bs4.BeautifulSoup(response.text, "html.parser")
  fotos = soup.find_all('img', src=True)

#Indica la cantidad de imágenes encontradas y descargadas
  Imagenes = []
  for foto in fotos:
    fotoUrl = foto.get('src')
    Imagenes.append(fotoUrl)
  print ('%s Imagenes encontradas' % len(Imagenes))

  #create directory for save images
  if path.isdir("Imagenes"):
    pass
  else:
    os.system("mkdir Imagenes")
  for image in Imagenes:
    if image.startswith("http") == False:
      download = url + image
    else:
      download = image
      # download images in images directory
    try:
      r = requests.get(download)
      f = open('Imagenes/%s' % download.split('/')[-1], 'wb')
      f.write(r.content)
      f.close()
    except:
      continue
  print("Se han almacenado las imagenes\n")

except Exception as e:
  print(e)
  print ("Error conexion con " + url)
  pass

lista = []
num = 0
ruta = "Imagenes"
os.chdir(ruta)
for root, dirs, files in os.walk(".", topdown=False):
  for name in files:
      #print(os.path.join(root, name))
      metafinal = ("[+] Metadata for file: %s " % (name) + "\n")
      try:
          exifData = {}
          exif = get_exif_metadata(name)
          if len(exif) == 0:
            continue
          else:
            long = len(name)
            cant = (name[:long-4])
            nombre = (cant + ".txt")
            archivo = open(nombre, "a")
            archivo.write(metafinal)
            for metadata in exif:
              archivo.write("Metadata: %s - Value: %s " %
                      (metadata, exif[metadata]) + "\n")
            lista.append(nombre)
            num = num + 1
            archivo.write("\n")
            archivo.close()

      except:
        continue

if num == 0:
  print("No existe metadata para ninguna imagen contenida")
else:
  print("Se almacenaron ", str(num), " txt en la carpeta",
  ruta, "con la metadata correspondiente:")
  for i in lista:
    print(i)
