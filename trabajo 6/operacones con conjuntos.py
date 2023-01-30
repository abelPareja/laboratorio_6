 c1 = {1, 2, 3, 4, 5, 6}
 c2 = {2, 4, 6, 8, 10}
 c3 = {1, 2, 3}
 c4 = {4, 5, 6}
print("union de los conjuntos c1 y c2 = ", c1 | c2)
print("union de los conjuntos c3 y c4 = ", c3 | c4)
print("")
print("intersecion de los conjuntos c1 y c2 =", c1 & c2)
print("intersecion de los conjuntos c3 y c4 = ", c1 & c2)
print("")
print("diferencia de los conjuntos c1 y c2 = ", c1 - c2)
print("diferencia de los conjuntos c3 y c4 = ", c1 - c2)
print("")
print("deferencia simetrrica de los conjuntos c1, c2 y c3 =",c1.symmetric_difference(c2.symmetric_difference(c3)))
print("deferencia simetrrica de los conjuntos c2, c3 y c4 =",c2.symmetric_difference(c3.symmetric_difference(c4)))

