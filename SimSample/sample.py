import meshio
import meshplot as mp
import numpy as np


# pure_vtx_pos = [ori_vtx_pos[cell[:4]] for cell in lagrange_tetra_cells]
# pure_vtx_pos = np.array(pure_vtx_pos)

mesh = meshio.read("./result_sheet1/step_0.vtu")
lagrange_tetra_cells = mesh.cells_dict["VTK_LAGRANGE_TETRAHEDRON"]
vertices = mesh.points
bump_idx_matrix = [[set() for _ in range(9)] for _ in range(9)]

cnt = 0

for i in range(lagrange_tetra_cells.shape[0]):
    tet = lagrange_tetra_cells[i]
    is_bump = False
    for idx in tet:
        if vertices[idx][1] > 0:
            is_bump = True
            break
    if is_bump:
        mid_pt = np.array([0.0, 0.0, 0.0])
        for idx in tet:
            mid_pt += vertices[idx]
        mid_pt /= 10
        print(mid_pt)
        cnt += 1

print(cnt)



vtx_nodes = mesh.points[lagrange_tetra_cells[0]]



# colors = np.array([colors = np.array([
# #     [1, 0, 0],  # Red
# #     [1, 0, 0],  # Red
# #     [1, 0, 0],  # Red
# #     [1, 0, 0],  # Red
# #     [0, 0, 1],  # Blue
# #     [0, 0, 1],  # Blue
# #     [0, 0, 1],  # Blue
# #     [0, 0, 1],  # Blue
# #     [0, 0, 1],  # Blue
# #     [0, 0, 1]   # Blue
# # ])
# #
# #
# # p = mp.plot(vtx_nodes, c=colors, shading={"point_size": 0.1})
#     [1, 0, 0],  # Red
#     [1, 0, 0],  # Red
#     [1, 0, 0],  # Red
#     [1, 0, 0],  # Red
#     [0, 0, 1],  # Blue
#     [0, 0, 1],  # Blue
#     [0, 0, 1],  # Blue
#     [0, 0, 1],  # Blue
#     [0, 0, 1],  # Blue
#     [0, 0, 1]   # Blue
# ])
#
#
# p = mp.plot(vtx_nodes, c=colors, shading={"point_size": 0.1})

# print(pure_vtx_pos)

# for tets in pure_vtx_pos:
#     for v in tets:
#         print(v)