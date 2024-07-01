import meshio
import meshplot as mp
import numpy as np


# pure_vtx_pos = [ori_vtx_pos[cell[:4]] for cell in lagrange_tetra_cells]
# pure_vtx_pos = np.array(pure_vtx_pos)

mesh = meshio.read("./result_sheet1/step_0.vtu")

lagrange_tetra_cells = mesh.cells_dict["VTK_LAGRANGE_TETRAHEDRON"]

vtx_nodes = mesh.points[lagrange_tetra_cells[0]]

colors = np.array([
    [1, 0, 0],  # Red
    [1, 0, 0],  # Red
    [1, 0, 0],  # Red
    [1, 0, 0],  # Red
    [0, 0, 1],  # Blue
    [0, 0, 1],  # Blue
    [0, 0, 1],  # Blue
    [0, 0, 1],  # Blue
    [0, 0, 1],  # Blue
    [0, 0, 1]   # Blue
])


p = mp.plot(vtx_nodes, c=colors, shading={"point_size": 0.1})

# print(pure_vtx_pos)

for tets in pure_vtx_pos:
    for v in tets:
        print(v)