#a) los índices de cada uno de los árboles deben ser nombre, número y tipo;
#b) mostrar todos los datos de un Pokémon a partir de su número y nombre –para este
#último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben
#mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos
#caracteres–;
#c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico;
#d) realizar un listado en orden ascendente por número y nombre de Pokémon, y
#además un listado por nivel por nombre;
#e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;
#f) Determina cuantos Pokémons hay de tipo eléctrico y acero.

from arbol_binario import BinaryTree

pokemon_data = [ 
    { 'nombre': 'Charmander', 'numero': 4, 'tipo': ['Fuego']},
    {'nombre': 'Bulbasaur', 'numero': 1, 'tipo': ['Pasto', 'Veneno']},
    {'nombre': 'Charizard', 'numero': 6, 'tipo': ['Fuego', 'Volador']},
    {'nombre': 'Pikachu', 'numero': 25, 'tipo': ['Electrico']},
    {'nombre': 'Rattata', 'numero': 19, 'tipo': ['Normal']},
    {'nombre': 'Vulpix', 'numero': 37, 'tipo': ['Fuego']},
    {'nombre': 'Squirtle', 'numero': 7, 'tipo': ['Agua']},
    {'nombre': 'Golem', 'numero': 76, 'tipo': ['Roca', 'Tierra']},
    {'nombre': 'Jolteon', 'numero': 135, 'tipo': ['Electrico']},
    {'nombre': 'Lycanroc', 'numero': 745, 'tipo': ['Roca']},
    {'nombre': 'Tyrantrum', 'numero': 697, 'tipo': ['Roca', 'Dragon']}
]

nombre_tree = BinaryTree()
numero_tree = BinaryTree()
tipo_tree = BinaryTree()

#a
for pokemon in pokemon_data:
    nombre_tree.insert_node(pokemon['nombre'], {'numero': pokemon['numero'],'tipo': pokemon['tipo']})
    numero_tree.insert_node(pokemon['nombre'], {'numero': pokemon['numero'],'tipo': pokemon['tipo']})
    tipo_tree.insert_node(pokemon['nombre'], {'numero': pokemon['numero'],'tipo': pokemon['tipo']})

#b
num = 19
numero_tree.inorden(num)
nombre = 'Rat'
nombre_tree.search_by_coincidence(nombre)
tipo = 'Normal'
tipo_tree.inorden(tipo)

#c
print('Pokémon de tipo Agua:')
tipo_tree.inorden_tipo('Agua')

print('Pokémon de tipo Fuego:')
tipo_tree.inorden_tipo('Fuego')

print('Pokémon de tipo Planta:')
tipo_tree.inorden_tipo('Planta')

print('Pokémon de tipo Eléctrico:')
tipo_tree.inorden_tipo('Eléctrico')

#d
print('Listado de Pokémon en orden ascendente por número:')
numero_tree.inorden()
print('\nListado de Pokémon en orden ascendente por nombre:')
nombre_tree.inorden()
print('Listado de Pokémon por nivel nombre')
nombre_tree.by_level()

#e
print('Datos de Pokémon Jolteon:')
nombre_tree.search_pokemon_by_name('Jolteon')
print('\Datos de Pokémon Lycanroc:')
nombre_tree.search_pokemon_by_name('Lycanroc')
print('\nDatos de Pokémon Tyrantrum:')
nombre_tree.search_pokemon_by_name('Tyrantrum')

#f
print(f"Pokémones de tipo 'Eléctrico': {tipo_tree.contar('Eléctrico')}")
print(f"Pokémones de tipo 'Acero': {tipo_tree.contar('Acero')}")