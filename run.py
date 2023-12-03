# Search methods

import search
import timeit

ab = search.GPSProblem('A', 'B', search.romania)
oe = search.GPSProblem('O', 'E', search.romania)
gz = search.GPSProblem('G', 'Z', search.romania)
nd = search.GPSProblem('N', 'D', search.romania)
mf = search.GPSProblem('M', 'F', search.romania)

#Amplitud
print()
print("Recorrido en amplitud")
print()
print("Generados: " + str(search.breadth_first_graph_search(ab)[2]))
print("Visitados: " + str(search.breadth_first_graph_search(ab)[1]))
print("Costo total: " + str(search.breadth_first_graph_search(ab)[0].path_cost))
inicio = timeit.default_timer()
print(search.breadth_first_graph_search(ab)[0].path())
tiempo_total = timeit.default_timer() - inicio
print(f"El algoritmo tardó {tiempo_total} segundos")
# Result:
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450

print()
print("Generados: " + str(search.breadth_first_graph_search(oe)[2]))
print("Visitados: " + str(search.breadth_first_graph_search(oe)[1]))
print("Costo total: " + str(search.breadth_first_graph_search(oe)[0].path_cost))
inicio = timeit.default_timer()
print(search.breadth_first_graph_search(oe)[0].path())
tiempo_total = timeit.default_timer() - inicio
print(f"El algoritmo tardó {tiempo_total} segundos")
# Result:
# [<Node E>, <Node H>, <Node U>, <Node B>, <Node F>, <Node S>, <Node O>]

print()
print("Generados: " + str(search.breadth_first_graph_search(gz)[2]))
print("Visitados: " + str(search.breadth_first_graph_search(gz)[1]))
print("Costo total: " + str(search.breadth_first_graph_search(gz)[0].path_cost))
inicio = timeit.default_timer()
print(search.breadth_first_graph_search(gz)[0].path())
tiempo_total = timeit.default_timer() - inicio
print(f"El algoritmo tardó {tiempo_total} segundos")
# Result:
# [<Node Z>, <Node A>, <Node S>, <Node F>, <Node B>, <Node G>]

print()
print("Generados: " + str(search.breadth_first_graph_search(nd)[2]))
print("Visitados: " + str(search.breadth_first_graph_search(nd)[1]))
print("Costo total: " + str(search.breadth_first_graph_search(nd)[0].path_cost))
inicio = timeit.default_timer()
print(search.breadth_first_graph_search(nd)[0].path())
tiempo_total = timeit.default_timer() - inicio
print(f"El algoritmo tardó {tiempo_total} segundos")
# Result:
# [<Node D>, <Node C>, <Node P>, <Node B>, <Node U>, <Node V>, <Node I>, <Node N>]

print()
print("Generados: " + str(search.breadth_first_graph_search(mf)[2]))
print("Visitados: " + str(search.breadth_first_graph_search(mf)[1]))
print("Costo total: " + str(search.breadth_first_graph_search(mf)[0].path_cost))
inicio = timeit.default_timer()
print(search.breadth_first_graph_search(mf)[0].path())
tiempo_total = timeit.default_timer() - inicio
print(f"El algoritmo tardó {tiempo_total} segundos")
# Result:
# [<Node F>, <Node S>, <Node R>, <Node C>, <Node D>, <Node M>]


#Profundidad
print()
print("Recorrido en profundidad")
print()
print("Generados: " + str(search.depth_first_graph_search(ab)[2]))
print("Visitados: " + str(search.depth_first_graph_search(ab)[1]))
print("Costo total: " + str(search.depth_first_graph_search(ab)[0].path_cost))
inicio = timeit.default_timer()
print(search.depth_first_graph_search(ab)[0].path())
tiempo_total = timeit.default_timer() - inicio
print(f"El algoritmo tardó {tiempo_total} segundos")
# Result:
# [<Node B>, <Node P>, <Node C>, <Node D>, <Node M>, <Node L>, <Node T>, <Node A>] : 101 + 138 + 120 + 75 + 70 + 111
# + 118 = 733

print()
print("Generados: " + str(search.depth_first_graph_search(oe)[2]))
print("Visitados: " + str(search.depth_first_graph_search(oe)[1]))
print("Costo total: " + str(search.depth_first_graph_search(oe)[0].path_cost))
inicio = timeit.default_timer()
print(search.depth_first_graph_search(oe)[0].path())
tiempo_total = timeit.default_timer() - inicio
print(f"El algoritmo tardó {tiempo_total} segundos")
# Result: [<Node E>, <Node H>, <Node U>, <Node B>, <Node P>, <Node R>, <Node S>, <Node O>]

print()
print("Generados: " + str(search.depth_first_graph_search(gz)[2]))
print("Visitados: " + str(search.depth_first_graph_search(gz)[1]))
print("Costo total: " + str(search.depth_first_graph_search(gz)[0].path_cost))
inicio = timeit.default_timer()
print(search.depth_first_graph_search(gz)[0].path())
tiempo_total = timeit.default_timer() - inicio
print(f"El algoritmo tardó {tiempo_total} segundos")
# Result: [<Node Z>, <Node A>, <Node T>, <Node L>, <Node M>, <Node D>, <Node C>, <Node P>, <Node R>, <Node S>, <Node F>, <Node B>, <Node G>]

print()
print("Generados: " + str(search.depth_first_graph_search(nd)[2]))
print("Visitados: " + str(search.depth_first_graph_search(nd)[1]))
print("Costo total: " + str(search.depth_first_graph_search(nd)[0].path_cost))
inicio = timeit.default_timer()
print(search.depth_first_graph_search(nd)[0].path())
tiempo_total = timeit.default_timer() - inicio
print(f"El algoritmo tardó {tiempo_total} segundos")
# Result: [<Node D>, <Node C>, <Node P>, <Node R>, <Node S>, <Node F>, <Node B>, <Node U>, <Node V>, <Node I>, <Node N>]

print()
print("Generados: " + str(search.depth_first_graph_search(mf)[2]))
print("Visitados: " + str(search.depth_first_graph_search(mf)[1]))
print("Costo total: " + str(search.depth_first_graph_search(mf)[0].path_cost))
inicio = timeit.default_timer()
print(search.depth_first_graph_search(mf)[0].path())
tiempo_total = timeit.default_timer() - inicio
print(f"El algoritmo tardó {tiempo_total} segundos")
# Result: [<Node F>, <Node B>, <Node P>, <Node R>, <Node S>, <Node A>, <Node T>, <Node L>, <Node M>]


#Ramificación y acotación
print()
print("Ramificación y acotación")
print()
print("Generados: " + str(search.branch_and_bound_search(ab)[2]))
print("Visitados: " + str(search.branch_and_bound_search(ab)[1]))
print("Costo total: " + str(search.branch_and_bound_search(ab)[0].path_cost))
inicio = timeit.default_timer()
print(search.branch_and_bound_search(ab)[0].path())
tiempo_total = timeit.default_timer() - inicio
print(f"El algoritmo tardó {tiempo_total} segundos")
# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>]

print()
print("Generados: " + str(search.branch_and_bound_search(oe)[2]))
print("Visitados: " + str(search.branch_and_bound_search(oe)[1]))
print("Costo total: " + str(search.branch_and_bound_search(oe)[0].path_cost))
inicio = timeit.default_timer()
print(search.branch_and_bound_search(oe)[0].path())
tiempo_total = timeit.default_timer() - inicio
print(f"El algoritmo tardó {tiempo_total} segundos")
# Result:
# [<Node E>, <Node H>, <Node U>, <Node B>, <Node P>, <Node R>, <Node S>, <Node O>]

print()
print("Generados: " + str(search.branch_and_bound_search(gz)[2]))
print("Visitados: " + str(search.branch_and_bound_search(gz)[1]))
print("Costo total: " + str(search.branch_and_bound_search(gz)[0].path_cost))
inicio = timeit.default_timer()
print(search.branch_and_bound_search(gz)[0].path())
tiempo_total = timeit.default_timer() - inicio
print(f"El algoritmo tardó {tiempo_total} segundos")
# Result:
# [<Node Z>, <Node A>, <Node S>, <Node R>, <Node P>, <Node B>, <Node G>]

print()
print("Generados: " + str(search.branch_and_bound_search(nd)[2]))
print("Visitados: " + str(search.branch_and_bound_search(nd)[1]))
print("Costo total: " + str(search.branch_and_bound_search(nd)[0].path_cost))
inicio = timeit.default_timer()
print(search.branch_and_bound_search(nd)[0].path())
tiempo_total = timeit.default_timer() - inicio
print(f"El algoritmo tardó {tiempo_total} segundos")
# Result:
# [<Node D>, <Node C>, <Node P>, <Node B>, <Node U>, <Node V>, <Node I>, <Node N>]

print()
print("Generados: " + str(search.branch_and_bound_search(mf)[2]))
print("Visitados: " + str(search.branch_and_bound_search(mf)[1]))
print("Costo total: " + str(search.branch_and_bound_search(mf)[0].path_cost))
inicio = timeit.default_timer()
print(search.branch_and_bound_search(mf)[0].path())
tiempo_total = timeit.default_timer() - inicio
print(f"El algoritmo tardó {tiempo_total} segundos")
# Result:
# [<Node F>, <Node S>, <Node R>, <Node C>, <Node D>, <Node M>]

#Ramificacion y acotacion con subestimación
print()
print("Ramificación y acotación con subestimación")
print()