#! /bin/bash
#Deivi Rodriguez Rangel 

if type -t wevtutil &> /dev/null
then
    OS=MSWin
elif type -t scutil &> /dev/null
then
    OS=macOS
else
    OS=Linux
fi
echo "Tu sistema operativo es: $OS"
function is_alive_ping() {
  ping -c 1 $1 > /dev/null 2>&1
  [ $? -eq 0 ] && echo "Node with IP: $i is up."
  if [ $? -eq 0 ]
  then 
	host=$1
      for ((counter=10; counter<=500; counter++))
      do
        (echo >/dev/tcp/$host/$counter) > /dev/null 2>&1 && echo "$counter open in IP $i"
      done
  fi
}

for i in 192.168.44.{1..255}
do
is_alive_ping $i & disown
done