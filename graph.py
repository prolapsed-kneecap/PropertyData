# g = {
#     "Алейск": {"people": 22, "paths": {"Барнаул": 130, "Рубцовск": 160, "Камень-на-Оби": 220}},
#     "Барнаул": {"people": 631, "paths": {"Алейск": 130, "Бийск": 160, "Камень-на-Оби": 195}},
#     "Бийск": {"people": 184, "paths": {"Барнаул": 160}},
#     "Рубцовск": {"people": 127, "paths": {"Алейск": 160, "Камень-на-Оби": 350}},
#     "Камень-на-Оби": {"people": 32, "paths": {"Барнаул": 195, "Алейск": 220, "Рубцовск": 350}},
# }
#
# g_n = {
#
# }
#
# NO_PATH = float('INF')
# int.__sub__()
# int.__add__()
# int.__truediv__()
# int.__mul__()
# g_m = [
#     [0, 130, NO_PATH, 160, 220],
#     [130, 0, 160, NO_PATH, 195],
#     [NO_PATH, 160, 0, NO_PATH, NO_PATH],
#     [160, NO_PATH, NO_PATH, 0, 350],
#     [220, 195, NO_PATH, 350, 0],
# ]
#
# town_dict = {
#     "Алейск": 1,
#     "Барнаул": 1,
#     "Бийск": 1,
#     "Рубцовск": 1,
#     "Камень-на-Оби": 1
# }
#
#
# def get_people_by_name(name: str):
#     return g[name]["people"] * 1000
#
#
# def get_paths_by_name(name: str):
#     return g[name]["paths"]
#
#
# def get_path(s: int, f: int, n: int = 5):
#     g_d = [list(i[1]["paths"].items()) for i in g.items()]
#     g_b
#     # print(g_d)
#     # print(list(list(g.items())[0][1]["paths"].items())[0])
#     # g_d = [(town_dict[list(i[1]["paths"].items())[0][0]], list(i[1]["paths"].items())[1]) for i in g.items()]
#     for i in g.items():
#         for j in i[1]["paths"]:
#
#     print(g_d)
#     d = [NO_PATH for i in range(n)]
#     p = [1 for i in range(n)]
#     used = [False for i in range(n)]
#     d[s] = 0
#     for i in range(n):
#         v = -1
#         for j in range(n):
#             if not used[j] and (v == -1 or d[j] < d[v]):
#                 v = j
#         if d[v] == NO_PATH:
#             break
#         used[v] = True
#         for el in g[v]:
#             if d[v] + el[1] < d[el[0]]:
#                 d[el[0]] = d[v] + el[1]
#                 p[el[1]] = v
#     if d[f] == NO_PATH:
#         print(-1)
#     else:
#         print(d[f])
#
#
# get_path(1, 5, 5)


