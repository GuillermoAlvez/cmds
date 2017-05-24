
lista = [8,3,8,3]  #3388, 3838, 3883, 8383, 8338
listaOp = ["+","-","/","*"]

for i in range (0,4):
	for j in range (0,4):
		for k in range (0,4):
			"""
			print "=" + str(lista[0]) + listaOp[i]+ str(lista[1])+ listaOp[j] + str(lista[2]) + listaOp[k] + str(lista[3]) 
			print "=(" + str(lista[0]) + listaOp[i]+ str(lista[1]) + ")"+ listaOp[j] + str(lista[2]) + listaOp[k] + str(lista[3]) 
			print "=("+str(lista[0]) + listaOp[i]+ str(lista[1]) + listaOp[j] + str(lista[2])+")" + listaOp[k] + str(lista[3]) 
			print "=("+str(lista[0]) + listaOp[i]+ str(lista[1]) + listaOp[j] + str(lista[2]) + listaOp[k] + str(lista[3]) +")"
			print "="+str(lista[0]) +    listaOp[i]+ "("+str(lista[1]) + listaOp[j] + str(lista[2])+")" + listaOp[k] + str(lista[3]) 
			print "="+str(lista[0]) +    listaOp[i]+ "("+str(lista[1]) + listaOp[j] + str(lista[2]) + listaOp[k] + str(lista[3]) +")"
			print "="+str(lista[0]) + listaOp[i]+ str(lista[1]) + listaOp[j] + "("+str(lista[2]) + listaOp[k] + str(lista[3]) + ")"

			print "=("+str(lista[0]) + listaOp[i]+ str(lista[1])+ ")" + listaOp[j] + "("+str(lista[2]) + listaOp[k] + str(lista[3]) + ")"
			"""

			print "=" + str(lista[0]) + listaOp[i]+ str(lista[1])+ listaOp[j] + str(lista[2]) + listaOp[k] + str(lista[3]) 
			print "=(" + str(lista[0]) + listaOp[i]+ str(lista[1]) + ")"+ listaOp[j] + str(lista[2]) + listaOp[k] + str(lista[3]) 
			print "=("+str(lista[0]) + listaOp[i]+ str(lista[1]) + listaOp[j] + str(lista[2])+")" + listaOp[k] + str(lista[3]) 
			print "=("+str(lista[0]) + listaOp[i]+ str(lista[1]) + listaOp[j] + str(lista[2]) + listaOp[k] + str(lista[3]) +")"
			print "="+str(lista[0]) +    listaOp[i]+ "("+str(lista[1]) + listaOp[j] + str(lista[2])+")" + listaOp[k] + str(lista[3]) 
			print "="+str(lista[0]) +    listaOp[i]+ "("+str(lista[1]) + listaOp[j] + str(lista[2]) + listaOp[k] + str(lista[3]) +")"
			print "="+str(lista[0]) + listaOp[i]+ str(lista[1]) + listaOp[j] + "("+str(lista[2]) + listaOp[k] + str(lista[3]) + ")"

			print "=("+str(lista[0]) + listaOp[i]+ str(lista[1])+ ")" + listaOp[j] + "("+str(lista[2]) + listaOp[k] + str(lista[3]) + ")"
			
			#3 2
			print "=("+str(lista[0]) + listaOp[i]+ str(lista[1]) + listaOp[j] + str(lista[2])+")" + listaOp[k] + str(lista[3]) 
			print "=(" + "(" + str(lista[0]) + listaOp[i] + str(lista[1])+ ")" + listaOp[j] + str(lista[2]) +")" + listaOp[k] + str(lista[3])
 			print "=("+str(lista[0]) + listaOp[i] +"("+str(lista[1]) + listaOp[j] + str(lista[2])+")"+ ")" + listaOp[k] + str(lista[3]) 
			print "="+str(lista[0]) +    listaOp[i]+ "("+ "("+str(lista[1]) + listaOp[j] + str(lista[2])+")" + listaOp[k] + str(lista[3]) +")"
			print "="+str(lista[0]) +    listaOp[i]+ "("+str(lista[1]) + listaOp[j] + "("+str(lista[2]) + listaOp[k] + str(lista[3])+")" +")"



