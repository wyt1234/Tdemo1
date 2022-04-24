def LinkGame(graph, x1, y1, x2, y2):
    graph[x1][y1] = 0
    graph[x2][y2] = 0
    to_y1 = True
    to_y2 = True
    x_min = min(x1, x2)
    for i in range(abs(x1 - x2) + 1):
        if graph[x_min + i][y1] == 1:
            to_y1 = False
        if graph[x_min + i][y2] == 1:
            to_y2 = False

    to_x1 = True
    to_x2 = True
    y_min = min(y1, y2)
    for j in range(abs(y1 - y2) + 1):
        if graph[x1][y_min + j] == 1:
            to_x1 = False
        if graph[x2][y_min + j] == 1:
            to_x2 = False

    x_way = to_y1 or to_y2
    y_way = to_x1 or to_x2

    return x_way and y_way


if __name__ == '__main__':
    graph = [[1, 0, 0, 1, 0],
             [0, 0, 1, 0, 1],
             [1, 0, 1, 0, 0],
             [0, 1, 0, 0, 1],
             [0, 1, 0, 1, 1]]
    # LinkGame(graph, 0, 0, 2, 2)
    LinkGame(graph, 0, 0, 3, 1)
