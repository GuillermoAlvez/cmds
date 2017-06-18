from __future__ import division
total=0

for x8 in range (0,9):
	for x9 in range (0,9):
		#if x8!=x9:
		for x10 in range (0,15,3) :
			print x10
			lista = [0,1,2,3,4,5,6,7,8]
			print lista
			x1=-1*x9 + x10*2/3
			x2=-1*x8 + x10*2/3
			x3=x8 + x9 - x10*1/3
			x4=x8 + 2*x9 - x10*2/3
			x5=x10*1/3
			x6=-1*x8 -2*x9 + x10*4/3
			x7=-x8-x9+x10
			#print x1
			#print ""
			if x1 in lista:
				lista.remove(x1)
				print "remove" + str(x1)
			if x2 in lista:	
				lista.remove(x2)
				print "remove" + str(x2)
			if x3 in lista:
				lista.remove(x3)
				print "remove" + str(x3)
			if x4 in lista:
				lista.remove(x4)
				print "remove" + str(x4)
			if x5 in lista:
				lista.remove(x5)
				print "remove" + str(x5)
			if x6 in lista:
				lista.remove(x6)
				print "remove" + str(x6)
			if x7 in lista:
				lista.remove(x7)
				print "remove" + str(x7)
			if x8 in lista:
				lista.remove(x8)
				print "remove" + str(x8)
			if x9 in lista:
				lista.remove(x9)
				print "remove" + str(x9)
			if not lista:
				print "VACIA"
				
			if (0<= x1 <= 8 and 0<= x2 <= 8 and 0<= x3 <= 8 and  0<= x4 <= 8 and 0<= x5 <= 8 and 0<= x6 <= 8 and 0<= x7 <= 8 and 0<= x8 <= 8 and 0<= x9 <= 8):
				total=total+1
				print "----x8="+ str(x8) + " x9="+ str(x9) +" y=" + str(x10)  +"-----"
				print "x1="+ str(x1) + " x2="+ str(x2) +" x3=" + str(x3)  
				print "x4="+ str(x4) + " x5="+ str(x5) +" x6=" + str(x6)  
				print "x7="+ str(x7) + " x8="+ str(x8) +" x9=" + str(x9)  
			
					
				
print total
