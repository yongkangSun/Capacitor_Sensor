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

  * **This setup could only test uniaxial deformation, what about stretch both $x$ and $y$ axis?**

* **Chane all unit to si unit:** 

  * tetrahedra model size: 250 * 450 * 5
  * scale in PolyFEM: 1e-4 (change to m)
  
* **Add marks:**

  * The density of the marks?
  * The distribution of the marks? 
    * Grid of marks
  



## After set up real silicon model

* Think about how to connect the model with the 3d print connector. 
* Think about how to apply marks on the model and the shape of the marks

### Idea

Optimization? running so slow, what does these solvers do.

Probably use python to generate json?

Quasistatic, avoid oscillation when. strething

quadratic base element: quadratic basis functions, more accurate

finite element quadratic basis / linear basis





​            "Eigen::PardisoLDLT",

​            "Eigen::CholmodDecomposition"



remove extra vertices with igl





book: Introduction to Numerical Methods for Variational Problems