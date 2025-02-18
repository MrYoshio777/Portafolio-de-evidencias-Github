# Author: Deivi Rodriguez Rangel
# Generamos un menú ciclíco con ayuda de do-until que asimismo desplegará
# nuestras funciones que se encuentran en el HowToCreateDirectories.psm1
# siendo el módulo de nuestro script actual.
do{
  menuprincipal
  $input = Read-Host "Selecciona una opción"
  switch($input)
  {
    # Se invocan las función New-Directorio
    '1' {
      'Opción 1.'
      New-Directorio
    }
    # Se invocan las función New-Archivo
    '2' {
      'Opción 2.'
      New-Archivo
    }
    # Se invocan las función Remove-Directorio
    '3' {
      'Opción 3.'
      Remove-Directorio
    }
    # El ciclo se mantendrá activo hasta que el usuario indique con 4 salir
    '4' {
      return}
  }Pause
}
until($input-eq '4')
