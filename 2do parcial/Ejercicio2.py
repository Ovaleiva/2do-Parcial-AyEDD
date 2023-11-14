#2. Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los
#algoritmos necesarios para resolver las siguientes tareas:
#a) cada vértice debe almacenar el nombre de un personaje, las aristas representan la
#cantidad de episodios en los que aparecieron juntos ambos personajes que se
#relacionan;
#b) hallar el árbol de expansión minino y determinar si contiene a Yoda;
#c) determinar cuál es el número máximo de episodio que comparten dos personajes,
#y quienes son.
#d) cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda,
#Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8.
#e) agregar al ejercicio de grafo camino mas corto desde Yoda a Rey.

from grafo import Grafo

grafo = Grafo()

#A-D.
grafo.insert_vertice('Luke Skywalker')
grafo.insert_vertice('Darth Vader')
grafo.insert_vertice('Kylo Ren')
grafo.insert_vertice('Leia')
grafo.insert_vertice('Boba Fett')
grafo.insert_vertice('C-3PO')
grafo.insert_vertice('Rey')
grafo.insert_vertice('Chewbacca')
grafo.insert_vertice('Han Solo')
grafo.insert_vertice('R2-D2')
grafo.insert_vertice('BB-8')
grafo.insert_vertice('Yoda')

personajes = ['Luke Skywalker', 'Darth Vader', 'Kylo Ren', 'Leia', 'Boba Fett', 'C-3PO', 'Rey', 'Chewbacca', 'Han Solo', 'R2-D2', 'BB-8', 'Yoda']

for personaje in personajes:
    grafo.insert_arista(personaje)

#B
arbol_expansion_minimo = grafo.kruskal()

print('árbol de expansión mínimo:')
for arista in arbol_expansion_minimo:
    print(arista)

contiene_yoda = False
for arista in arbol_expansion_minimo:
    if 'Yoda' in arista:
        contiene_yoda = True
        break

if contiene_yoda:
    print('El árbol de expansión mínimo contiene a Yoda.')
else:
    print('El árbol de expansión mínimo no contiene a Yoda.')

#C
max_peso, personajes_max_episodios = grafo.max_episodios_compartidos()

if max_peso > 0:
    print(f'El número máximo de episodios compartidos es {max_peso}, y los personajes son:')
    for i in range(0, len(personajes_max_episodios), 2):
        personaje1 = personajes_max_episodios[i]
        personaje2 = personajes_max_episodios[i + 1]
        print(f'{personaje1} y {personaje2}')
else:
    print('No se encontraron personajes que compartan episodios.')

#E
#agregar al ejercicio de grafo camino mas corto desde Yoda a Rey
ori = 'habitacionUno'
des = 'salaDeEstar'
origen = grafo.search_vertice(ori)
destino = grafo.search_vertice(des)
camino_mas_corto = None
if(origen is not None and destino is not None):
    if(grafo.has_path(ori, des)):
        camino_mas_corto = grafo.dijkstra(ori, des)
        fin = des
        while camino_mas_corto.size() > 0:
            value = camino_mas_corto.pop()
            if fin == value[0]:
                print(value[0], value[1])
                fin = value [2]