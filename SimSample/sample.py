import meshio
import meshplot as mp
import numpy as np

mesh = meshio.read("./result/step_0.vtu")
lagrange_tetra_cells = mesh.cells_dict["VTK_LAGRANGE_TETRAHEDRON"]
ori_vtx_pos = mesh.points

pure_vtx_pos = [ori_vtx_pos[cell[:4]] for cell in lagrange_tetra_cells]
pure_vtx_pos = np.array(pure_vtx_pos)

# print(pure_vtx_pos)

for tets in pure_vtx_pos:
    for v in t:
        print(v)