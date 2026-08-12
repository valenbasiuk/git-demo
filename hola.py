print("hola mundear? 1- si / 2- no")
try:
	respuesta = int(input("elige la opcion: ").strip())
except ValueError:
	print("opcion invalida")
	raise SystemExit(1)

if respuesta == 1:
	print("hola mundo!")
elif respuesta == 2:
	print("adios mundo!")
	raise SystemExit(0)
else:
	print("opcion fuera de rango")
	raise SystemExit(1)