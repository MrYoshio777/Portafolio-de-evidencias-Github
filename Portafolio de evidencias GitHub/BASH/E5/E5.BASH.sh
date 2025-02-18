#!/bin/bash

#cfccfca8a55b497f9f3c5b22a9cd132a 
#Función para hacer invisible lo que 
#se ponga en la consola

function invapikey(){
  sttyactual=`stty -g`
  stty -echo

  echo
  echo -n "Introduzca su APIkey: "
  read apikey
  
  # -- Se restablece la sesion stty anterior.
  stty $sttyactual
  echo
  
}

function correos(){
  while IFS= read -r line
  do
    correo=$line
    API=$(curl -s https://haveibeenpwned.com/api/v3/breachedaccount/$correo -H 'hibp-api-key':$apikey)
    if [[ "$API" = "" ]]; then
      echo -e "\n El correo $correo no ha sido vulnerado."
    else
      echo -e "\n El correo $correo ha sido vulnerado por: $API"
    fi
    echo
  done < correos.txt
}
invapikey
correos
