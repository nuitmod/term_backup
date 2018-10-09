read -p "Input a name : " x

#if [ -n $1 ]; then
if [[ $x != " " ]]; then
i=0
while [[ $i < 3 ]]; 
	do echo "Ruth" ; 
	sleep 1
	echo "$i : $x"
	let i+=1
#if [[ $i=3 ]]; then break ; fi
	done

else break
fi
