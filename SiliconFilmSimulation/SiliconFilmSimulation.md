# Silicon Film Simulation

Simulate the deformation of silicon films with different material and geometry features.

From the original paper:

* **Thickness** of the final sensor: $540 \mu m = 450 \mu m\ RTV + 90 \mu m\ Conductive\ Layer$. Component:
  * Conductive layer: $45 \mu m * 2\ layers$ 
  * Protectice layer: $180 \mu m * 2\ layers$ 
  * Dielectric layer: $90 \mu m * 1\ layers$ 
* **Young's modulus**: 
  * Layered RTV: $729.6±13.4$ kPA
  * Add 2 conductive layer: $979.6±16.6$ kPA
* **Size**
  * time measurement: 200 X 200 mm = 2e5 x 2e5 $\mu m$ (lets use this setup)
  * Bicep experiment (large): 300 x 250 mm
  * Uni-axial sensor: 15 x 50 mm

Not stated in the paper:

* Poisson's Ratio: 0.45 ~ 0.5
* Density: 1100 ~ 1200 kg/$m^3$



## Toy demo

### 20x20x1 & sparse & dirichlet

Simulation of a toy demo of a silicon film, 20 x 20 x 1 (mm) with maximum tets' volume of 0.5. Below are the statics of the mesh:

| points | tetrahedra | faces (boundary) |
| ------ | ---------- | ---------------- |
| 532    | 1392       | 3304             |

#### Boundary Condition

* Dirichlet_boundary, stretch the scilicon from `y` and `-y`, until double the length. 

#### Comparison (conductivity)

* Compare conductive and non-conductive parameters.

* **Result**: the result looks the same, **maybe I should compare the result numerically.**



### 50x50x5 & sparse & dirichlet

#### Model Size

* Sample size: 5000 x 5000 x 500 $\mu m$ (0.005m x 0.005m )
* Model size: 50 x 50 x 5
* Density: 2.5 area
* scale in PolyFEM: 1e-4 (change to m)
  * This is not possible since the number is too small 

#### Statics

| points | tetrahedra | faces (boundary) |
| ------ | ---------- | ---------------- |
| 2340   | 9433       | 3122             |



### 100x100x0.5 & sparse

#### Model Size

* Sample size: 100000 x 100000 x 500 $\mu m$ (0.1m * 0.1m)
* Model size: 100 x 100 x 0.5
* Density: 4.0 + 1.25 area
* scale in PolyFEM: 1e-1 (change to cm)
  * **I am not sure is it ok to change all unit to cm.**

#### Statics

| points | tetrahedra | faces (boundary) |
| ------ | ---------- | ---------------- |
| 3524   | 10835      | 25192            |



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



## Real simulation

### Model Size

* Sample size: 100000 * 100000 * 500 $\mu m$, (0.1m * 0.1m)

* tetrahedra model size: 1000 * 1000 * 5: 

* scale in PolyFEM: 1e-4 (change to m)

* Two density:

  * Dense: 25.0

    | points | tetrahedra | faces (boundary) |
    | ------ | ---------- | ---------------- |
    | 122988 | 405705     | 238692           |

  * Sparse: v

    | points | tetrahedra | faces (boundary) |
    | ------ | ---------- | ---------------- |
    | 44961  | 135303     | 89918            |



## Requirement Change

之后的工作要建立在一个设计好的带凸点的模型上，设计一下凸点的大小和分布，建模。

制作倒膜，从而获得模具。

把scanning的实验器材setup好，用成熟的纯硅胶做实验，验证流程。

在新模型上完成simulation 以及tracking。



## Further work on simulation part

* **Add marks:**
  * The density of the marks?
  * The distribution of the marks? 
    * Grid of marks
  * How to add marks to the simulation?
    * Choose a set of vertex for each mark, and calclate its mean?
    * Don't know if it is a good choice.

* **Sample from simulation result:**
  * How?

* **Research on each solver:**
  * Not in a hurry, but go through all kinds of solvers.
  * Reference Book: https://hplgit.github.io/fem-book/doc/pub/book/pdf/fem-book-4print-2up.pdf
  * Questions:
    * quadratic base element: quadratic basis functions, more accurate




## After set up real silicon model

* Think about how to connect the model with the 3d print connector. 
* Think about how to apply marks on the model and the distribution of the marks.
* Think about how two match the mark (index) with its position (xyz cordinate).
  * First, for our easy case (pure stretching), this could be trivial
  * Second, The original paper must have a way to do so.




## FurtherMore

* Compression: 
  * Make a cube of material, compress it, record force for different displacements
  * Reference: https://www.baecher.info/publication/mat_char_robosoft20/mat_char_robosoft20.pdf
* 





### Idea



Today's plan:

* Think about how to sample from the simulation result, implement a demo.

* Check optitrack