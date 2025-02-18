function menu{
    param([String]$Title = "Bienvenido al menú de PowerShell")
    cls
    Write-Host "--------------Opciones----------------"
    Write-Host "1. Status del perfil"
    Write-Host "2. Cambiar el status del perfil"
    Write-Host "3. Ver perfil de red actual"
    Write-Host "4. Cambiar perfil de red actual"
    Write-Host "5. Ver reglas de bloqueo"
    Write-Host "6. Agregar reglas de bloqueo"
    Write-Host "7. Eliminar reglas de bloqueo"
    Write-Host "8. Salir"
}

function Ver-StatusPerfil{ 
	param([Parameter(Mandatory)] [ValidateSet("Public","Private")] [string] $perfil) 
	$status = Get-NetFirewallProfile -Name $perfil 
	Write-Host "Perfil:" $perfil 
	if($status.enabled){ 
		Write-Host "Status: Activado`n" 
	} else{ 
		Write-Host "Status: Desactivado`n"} 
}

function Cambiar-StatusPerfil{ 
	param([Parameter(Mandatory)] [ValidateSet("Public","Private")] [string] $perfil) 
	$status = Get-NetFirewallProfile -Name $perfil 
	Write-Host "Perfil:" $perfil 
	if($status.enabled){ 
		Write-Host "Status actual: Activado" 
		$opc = Read-Host -Prompt "Deseas desactivarlo? [Y] Si [N] No" 
		if ($opc -eq "Y"){try{ 
			Set-NetFirewallProfile -Name $perfil -Enabled False -ErrorAction "Stop"} catch{Write-Host "`n`t`t-------------------------`n`t`t  No se tienen permisos`n`t`t-------------------------`n" }
	}} else{ 
		Write-Host "Status: Desactivado" 
		$opc = Read-Host -Prompt "Deseas activarlo? [Y] Si [N] No" 
		if ($opc -eq "Y"){try{ 
			Write-Host "Activando perfil" 
			Set-NetFirewallProfile -Name $perfil -Enabled True -ErrorAction "Stop"} catch{Write-Host "`n`t`t-------------------------`n`t`t  No se tienen permisos`n`t`t-------------------------`n"}
	} 
	Ver-StatusPerfil -perfil $perfil 
}  
}


function Ver-PerfilRedActual{ 
	$perfilRed = Get-NetConnectionProfile 
	Write-Host "Nombre de red:" $perfilRed.Name 
	Write-Host "Perfil de red:" $perfilRed.NetworkCategory 
}


function Cambiar-PerfilRedActual{ 
	$perfilRed = Get-NetConnectionProfile 
	if($perfilRed.NetworkCategory -eq "Public"){ 
		Write-Host "El perfil actual es público" 
		$opc = Read-Host -Prompt "Quieres cambiar a privado? [Y] Si [N] No" 
		if($opc -eq "Y"){try{ 
			Set-NetConnectionProfile -Name $perfilRed.Name -NetworkCategory Private -ErrorAction Stop 
			Write-Host "Perfil cambiado" 
		} catch{Write-Host "`n`t`t-------------------------`n`t`t  No se tienen permisos`n`t`t-------------------------`n"}}
      } else{ 
		Write-Host "El perfil actual es privado" 
		$opc = Read-Host -Prompt "Quieres cambiar a público? [Y] Si [N] No" 
		if($opc -eq "Y"){try{ 
			Set-NetConnectionProfile -Name $perfilRed.Name -NetworkCategory Public -ErrorAction Stop
			Write-Host "Perfil cambiado" 
		}catch{Write-Host "`n`t`t-------------------------`n`t`t  No se tienen permisos`n`t`t-------------------------`n"}} 
	} 
	Ver-PerfilRedActual 
} 


function Ver-ReglasBloqueo{ 
	if(Get-NetFirewallRule -Action Block -Enabled True -ErrorAction SilentlyContinue){ 
		Get-NetFirewallRule -Action Block -Enabled True 
	} else{ 
		Write-Host "No hay reglas definidas aún" 
	} 
}


function Agregar-ReglasBloqueo{ 
	$puerto = Read-Host -Prompt "Cuál puerto quieres bloquear?" 
    try{
	New-NetFirewallRule -DisplayName "Puerto-Entrada-$puerto" -Profile "Public" -Direction Inbound -Action Block -Protocol TCP -LocalPort $puerto -ErrorAction Stop} catch{
    Write-Host "`n`t`t-------------------------`n`t`t  No se tienen permisos`n`t`t-------------------------`n"} 
}


function Eliminar-ReglasBloqueo{ 
	$reglas = Get-NetFirewallRule -Action Block -Enabled True 
	Write-Host "Reglas actuales" 
	foreach($regla in $reglas){ 
		Write-Host "Regla:" $regla.DisplayName 
		Write-Host "Perfil:" $regla.Profile 
		Write-Host "ID:" $regla.Name 
		$opc = Read-Host -Prompt "Deseas eliminar esta regla [Y] Si [N] No" 
		if($opc -eq "Y"){try{ 
			Remove-NetFirewallRule -ID $regla.name -ErrorAction "Stop"
			Write-Host "`n`t`t-------------------------`n`t`t  No se tienen permisos`n`t`t-------------------------`n"}catch{
            Write-Host "`n`t`t-------------------------`n`t`t  No se tienen permisos`n`t`t-------------------------`n"}
            break 
		} 
	} 
}