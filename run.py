# Search methods

import search
import time

ab = search.GPSProblem('A', 'B', search.romania)


print("Generados: " + str(search.breadth_first_graph_search(ab)[2]))
print("Visitados: " + str(search.breadth_first_graph_search(ab)[1]))
print("Costo total: " + str(search.breadth_first_graph_search(ab)[0].path_cost))
inicioB = time.time()
print(search.breadth_first_graph_search(ab)[0].path())
time.sleep(0.1)
print(time.time() - inicioB - 0.1)

print("Generados: " + str(search.depth_first_graph_search(ab)[2]))
print("Visitados: " + str(search.depth_first_graph_search(ab)[1]))
print("Costo total: " + str(search.depth_first_graph_search(ab)[0].path_cost))
inicioD = time.time()
print(search.depth_first_graph_search(ab)[0].path())
time.sleep(0.1)
print(time.time() - inicioB - 0.1)

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
