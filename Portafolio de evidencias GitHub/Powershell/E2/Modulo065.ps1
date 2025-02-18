#Deivi Rodriguez Rangel, Humberto Emiliano Rodriguez Rojas, Diego Orlando Garza Tovar

do{
  menú
  $input = Read-Host "Selecciona una opción"
  switch($input)
  {
    '1' {
      'Opción 1.'
      Ver-StatusPerfil
    }
     
    '2' {
      'Opción 2.'
      Cambiar-StatusPerfil
    } 

    '3' {
      'Opción 3.'
      Ver-PerfilRedActual
    } 

    '4' {
      'Opción 4.'
      Cambiar-PerfilRedActual
    } 

    '5' {
      'Opción 5.'
      Ver-ReglasBloqueo
    } 

    '6' {
      'Opción 6.'
      Agregar-ReglasBloqueo
    }

     '7' {
      'Opción 7.'
      Eliminar-ReglasBloqueo
    } 

    '8' {
      return
    }
  }
  Pause
}
until($input -eq '8')