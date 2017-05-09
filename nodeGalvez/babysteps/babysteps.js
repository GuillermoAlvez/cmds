var lista = process.argv
var result = 0
for (var i = 2 ; i < lista.length; i++)
	result += Number(lista[i])

console.log(result)
