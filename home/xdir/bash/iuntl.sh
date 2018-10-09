
u=0
until [ $u -gt 9 ];
do
echo "num is : $u"
#u=`expr $u + 1`
let "u += 1"
done
