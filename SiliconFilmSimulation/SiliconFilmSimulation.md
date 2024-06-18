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

### 20x20x1 + sparse + dirichlet

Simulation of a toy demo of a silicon film, 20 x 20 x 1 (mm) with maximum tets' volume of 0.5. Below are the statics of the mesh:

| points | tetrahedra | faces |
| ------ | ---------- | ----- |
| 532    | 1392       | 3304  |

#### Boundary Condition

Dirichlet_boundary, stretch the scilicon from `y` and `-y`, until double the length. 



## Further work on simulation part

* **Test material size:** 

  * Size from original paper: 200000 * 200000 * 500 $\mu m$, (0.2m * 0.2m)

  * Simulation size: 25000 * 25000 * 500 $\mu m$, (0.025m * 0.025m)

  * Final model size: 25000 * 45000 * 500 $\mu m$, (0.025m * 0.045m)

    extra 1cm for both end are used for connection.

* **Arvi's material size:**

  * Arvi's Sample size: 100000 * 100000 * 500 $\mu m$, (0.1m * 0.1m)
  * Arvi's Simulation size: 120000 * 100000 * 500 $\mu m$, (0.12m * 0.1m)
  * **Do we need to simulate how silicon film connect to the connector? Change boundary condition?**

* **Chane all unit to si unit:** 

  * tetrahedra model size: 1200 * 1000 * 5: 

    * Dense:

      <img src="/Users/johnnnysun/Library/Application Support/typora-user-images/image-20240617230318360.png" alt="image-20240617230318360" style="zoom: 50%;" />

    * Sparse:

      <img src="/Users/johnnnysun/Library/Application Support/typora-user-images/image-20240617232713891.png" alt="image-20240617232713891" style="zoom:50%;" />

  * scale in PolyFEM: 1e-4 (change to m)

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
