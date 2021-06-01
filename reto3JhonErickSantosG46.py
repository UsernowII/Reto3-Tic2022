#Jhon Erick Santos Gonzalez
#Misiontic 2022 G46 
#Reto 3 Semana 4
#programa registro de temperaturas
#entradas datos registrados por temperaturas, dias , dias sin error, temp max , temp min
#procesos calcular el valor del descuento con base en los criterios
#salidas Numero de dias con error ( cuales < 5 cuales >35 cuantos por ambos)
#temperatura media, min , max
#porcentaje de dias de errores respecto a dias total

daysavailable = 0 # dias con tomoa de datos validos
tempMin = 1
tempMax = 1
daysError = 0
daysErrormin = 0
daysErrormax = 0
sumTempMin = 0
sumTempMax = 0
tempMinError = 0
tempMaxError = 0
days = 0 
i =1  #contador dia de toma de datos

print("Registro de temperaturas salido de campo")
print("Para finalizar la recoleccion de datos ingrese temperaturas (0,0)")
while tempMin !=0 and tempMax != 0 :
    print("Toma de temperaturas dia ", i)
    tempMin = int(input("Digite la temparatura minima: "))
    tempMax = int(input("Digite la temparatura maxima: "))
    print()
    if tempMin == 0 and tempMax == 0: #Entrada de [0,0] para detener el programa
        break
    else:
        if tempMin >=5 and tempMax <= 35:
            daysavailable = daysavailable + 1
            sumTempMin = sumTempMin + tempMin
            sumTempMax = sumTempMax + tempMax
        elif tempMin < 5 and tempMax > 35 :
            daysError = daysError + 1
            tempMinError = tempMinError + tempMin
            tempMaxError = tempMaxError + tempMax
        elif tempMin < 5 :
            daysErrormin = daysErrormin + 1
            tempMinError = tempMinError + tempMin
        elif tempMax > 35 :
            daysErrormax = daysErrormax + 1
            tempMaxError = tempMaxError + tempMax
    i = i + 1
   
days = daysavailable + daysError + daysErrormax + daysErrormin
TempMediaMin = sumTempMin / (daysavailable )
TempMediaMax = sumTempMax / (daysavailable )
sumDaysError= daysError + daysErrormax + daysErrormin 
porcentageDaysError = (sumDaysError / days)*100
print("Total temperatura minima de datos validos: ",sumTempMin)
print("Total temperatura maximo de datos validos: ",sumTempMax)
print("Dias con error temperaturas por debajo de 5°: ",daysErrormin)
print("Dias con error temperaturas por encima de 36°: ", daysErrormax)
print("Dias con error por ambos errores: ", daysError)
print("Total dias sin error: ", daysavailable)
print("Total de dias: ", days)
print("Promedio toma de datos temperatura Minima: ",TempMediaMin)
print("Promedio toma de datos temperatura Maxima: ",TempMediaMax)
print("El porcentaje de dias con errores es del ",round(porcentageDaysError), "%")
