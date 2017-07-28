while true
do
       cat response | nc -v -l -p55555
       # connect to localhost:55555 using your favorite browser
       sleep 2
done
