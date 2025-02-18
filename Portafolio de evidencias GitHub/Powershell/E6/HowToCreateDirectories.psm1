function menuprincipal{
    param([String]$Title = "Bienvenido al menú de PowerShell")
    cls
    Write-Host "--------------Opciones----------------"
    Write-Host "1. Crear un nuevo directorio"
    Write-Host "2. Crear un nuevo archivo"
    Write-Host "3. Remover un directorio"
    Write-Host "4. Salir"
}

function New-Directorio{
  param([Parameter(Mandatory)] [string] $archivo,
  [Parameter(Mandatory)] [String] $ruta)
  Write-Host "Se ha creado un nuevo directorio en: $ruta\$archivo"
  try { 
  New-Item "$ruta\$archivo" -itemType Directory -ErrorAction Stop
  } 
  catch {
  Write-Host "Error. No se encuentra el directorio"
  $_.Exception.Message}
}

function New-Archivo{ 
  param([Parameter(Mandatory)] [string] $archivo,
  [Parameter(Mandatory)] [String] $ruta)
  Write-Host "Se ha creado un archivo en: $ruta\$archivo.$extension"
  try{
  New-Item "$ruta\$archivo.$extension" -itemType File -ErrorAction Stop 
  } 
  catch {
  Write-Host "Error. No se encuentra el directorio"
  $_.Exception.Message
  }
}

function Remove-Directorio{
  param([Parameter(Mandatory)] [string] $nombre_dir,
  [Parameter(Mandatory)] [String] $ruta)
  Write-Host "Borrado con éxito: $ruta\$nombre_dir"
  try{
  Remove-Item "$ruta\$nombre_dir" -recurse -ErrorAction Stop
  } 
  catch {
     Write-Host "Error. No se encuentra el directorio"
  $_.Exception.Message
  }
}