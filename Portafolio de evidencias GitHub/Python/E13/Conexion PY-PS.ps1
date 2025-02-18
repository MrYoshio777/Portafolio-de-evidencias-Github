#Deivi Rodriguez Rangel
# Python Executable Definition
$Python = "python.exe"

# Python Scrip that I wish to execute
$Script = "C:\Users\usuario\Documents\Python Scripts\Python FCFM\3er Semestre LSTI\E13\SearchEmail.py"
$file = Get-Content "C:\Users\usuario\Documents\Python Scripts\Python FCFM\3er Semestre LSTI\E13\emails.txt"
foreach ($line in $file) 
{
Write-Output "$line"
}  
$Python | &  $Script
