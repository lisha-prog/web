import math
import numpy as np
import matplotlib.pyplot as plt 

#15.3) Tsunami
lam_3= 800
per_3= 1
freq_3= 1/per_3
vel_3= freq_3*lam_3
vel_ms_3= (vel_3*1000)/3600
print("ejercicio 3")
print("La  rapidez de las olas es de ", vel_3, "km/h o de", vel_ms_3,"m/s")

#15.24 Imagine que un compañero con dotes matemáticas le dice que la función de onda de una onda viajera en una cuerda delgada es y(x, t) 5 2.30 mm cos[(6.98 rad>m)x 1 (742 rad>s)t]. Usted, que es una persona más práctica, efectúa mediciones y determina que la cuerda tiene una longitud de 1.35 m y una masa de 0.00338 kg. Ahora le piden determinar lo siguiente: a) amplitud; b) frecuencia; c) longitud de onda; d) rapidez de la onda; e) dirección en que viaja la onda; f) tensión en la cuerda; g) potencia media transmitida por la onda.
#y(x,t)= 2.30 mm cos[(6.98 rad/m)x + (742 rad/s)t]
amp_24= 2.30
num_ond_24= 6.98
ang_freq_24= 742
lar_cu_24= 1.35
mas_cu_24= 0.00338
mas_u_cu_24= mas_cu_24/lar_cu_24
print("ejercicio 24")
#a)
print( "La amplitud es ", amp_24, "mm" )
#b)
freq_24= ang_freq_24/(2*math.pi)
print( "La frecuencia es ", freq_24, "Hz" )
#c)
lam_24= 2*math.pi/num_ond_24
print( "La longitud de onda es de ", lam_24, "m" )
#d)
vel_24= freq_24*lam_24
print( "La rapidez de la onda es de ", vel_24, "m/s" )
#e)
print( "Como kx y wt tienen el mismo signo, la onda viaja en la direccion -x" )
#f)
ten_cu_24= mas_u_cu_24*vel_24**2
print( "La tension en la cuerda es de ", ten_cu_24, "N" )
#g)
pot_med_24= 0.5*math.sqrt(mas_u_cu_24*ten_cu_24)*ang_freq_24**2*(amp_24*1e-3)**2
print( "La potencia media es de ", pot_med_24, "W" ) 

#15.13 Una onda transversal que viaja en una cuerda tiene amplitud de 0.300 cm, longitud de onda de 12.0 cm y rapidez de 6.00 cm>s y se representa con y(x, t) del ejercicio 15.12. a) En el tiempo t 5 0, calcule y a intervalos de x de 1.5 cm (es decir, en x 5 0, x 5 1.5 cm, x 5 3.0 cm, etcétera) de x 5 0 a x 5 12.0 cm. Muestre los resultados en una gráfica. Ésta es la forma de la cuerda en el tiempo t 5 0. b) Repita los cálculos para los mismos valores de x en t 5 0.400 s y t 5 0.800 s. Muestre gráficamente la forma de la cuerda en esos instantes. ¿En qué dirección viaja la onda?
amp_13= 0.300
lam_13= 12.0
vel_13= 6

despl_13= []
pos_13_0= []
pos_13_1= []
pos_13_2= []
for i in range(9):
    despl= i*1.5
    despl_13.append(despl)
    pos_13_0.append(amp_13*math.cos(2*math.pi/lam_13*(despl - vel_13*0)))
    pos_13_1.append(amp_13*math.cos(2*math.pi/lam_13*(despl - vel_13*0.400)))
    pos_13_2.append(amp_13*math.cos(2*math.pi/lam_13*(despl - vel_13*0.800)))

plt.figure()
plt.plot(despl_13, pos_13_0, "o-", label="t= 0")
plt.plot(despl_13, pos_13_1, "s-", label="t= 0.400 s")
plt.plot(despl_13, pos_13_2, "^-", label="t= 0.800 s")
plt.axhline(0)
plt.xlabel("x (cm)")
plt.ylabel("y (cm)")
plt.legend()
plt.show()
print( "La cresta se corre hacia x mayor (2.4 cm en 0.4 s y 4.8 cm en 0.8 s), la onda viaja hacia +x" )

print( "Ailish Ortiz" ) 