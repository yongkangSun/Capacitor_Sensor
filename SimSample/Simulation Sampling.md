# Simulation Sampling

Yongkang Sun



## Sampling

### vtu file

#### Attributes

* **Points**: (num_points, 3), xyz coordiante of each vertices.
  * Because the `discr_order = 2`. So the first 4 are vertex and later 6 are middle points of each edge.
* **Point_data**: Attributes (scalar/vector: stress ...) for each vertices.
* **Cells**: list of `CellBlock`, stored `ndarray` of tetrahedra (num_tets, 10).
  * Index of each vertices (10 for each tetrahedra).
* **Cell_data**: Attributes (stress, strain) for each tetrahedras.
* **Cells_dict:** dictionary version of Cells.
* **Field_data**: Attributes for the whole mesh.



### Tracking Detail:

* For each bump there are two kinds of point:
  * y axis over 0: 0.375 (or lower)
  * connected to vertiecs in class 1, with y axis = -0.05
* Plan:
  * 1: Find all vertices y above 0. Put it into a list.
  * 2: Find all vertices y equals to -0.05. Put in a set (hash?)
  * For each verties in 1, find which tetrahedra it's in. determine whether have other vertex in 2.
  * Alternative: go through all tets, have one in 1?  remember its index. 
  * Register it to a 9x9 matrix, with each element being a list of index.
    * Which cell? determine by x and z ? all seperate in distance of 0.5
  * go through all remembered tets, 

* Frame number: 100