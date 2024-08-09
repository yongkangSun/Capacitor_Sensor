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



### Arvi's Model with tetrahedra bump

### Model Size

* tetrahedra model size: 8.0 * 4.0 * 0.2  (cm) 

* scale in PolyFEM: 0.01 (change to m)

* Two density:

  * Sparse: v

    | points | tetrahedra | faces (boundary) |
    | ------ | ---------- | ---------------- |
    | 4149   | 12372      | 8294             |



### Arvi's Model with tetrahedra bump (9 * 9) , 1

### Model Size

* tetrahedra model size: 10.0 * 5.0 * 0.1875  (cm) 

* scale in PolyFEM: 0.01 (change to m)

* stretch & selection in x direction

* Two density:

  * Sparse: v

    | points | tetrahedra | faces (boundary) |
    | ------ | ---------- | ---------------- |
    | 1960   | 5839       | 3916             |



### Arvi's Model with tetrahedra bump (9 * 9) , 2

### Model Size

* tetrahedra model size: 10.0 * 5.0 * 0.2875  (cm) 

* scale in PolyFEM: 0.01 (change to m)

* stretch & selection in x direction

* Two density:

  * Sparse: v

    | points | tetrahedra | faces (boundary) |
    | ------ | ---------- | ---------------- |
    | 1362   | 3866       | 2720             |



### Arvi's Model with tetrahedra bump (9 * 9) , 5

### Model Size

* tetrahedra model size: 10.0 * 5.0 * 0.5875  (cm) 

* scale in PolyFEM: 0.01 (change to m)

* stretch & selection in x direction

* Two density:

  * Sparse: v

    | points | tetrahedra | faces (boundary) |
    | ------ | ---------- | ---------------- |
    | 1699   | 5507       | 2953             |



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
* Think about how two match the mark (index) with its position (xyz cordinate).
  * First, for our easy case (pure stretching), this could be trivial
  * Second, The original paper must have a way to do so.




## FurtherMore

* Compression: 
  * Make a cube of material, compress it, record force for different displacements
  * Reference: https://www.baecher.info/publication/mat_char_robosoft20/mat_char_robosoft20.pdf
