# Non-rigid registration Survey

Yongkang Sun 



## A Survey on Shape Correspondence - Oliver van Kaick

### Problem Statement

* **Full correspondence**: correspondence between whole shape
* **Sparse correpondece**: small subset of all elements.

* Alignment needed?
* Non-rigid alignment

### Classification

* Input: point sets, 3D + time
* Output: correspondence only, bijection, 



possible way:

* Certain methods allow the user to select which type of mapping is desired, such as [LH05], where the final correspondence is obtained by filtering an initial result according to the mapping constraints. Other approaches assume that the focus of interest is only on a specific type of mapping and proceed to build their method over such an assumption (e.g. [MC03, BBM05], in which the correspondence problem is posed as an optimization where the mappings are constrained to be one-to-one).
* 5.2. Correspondence search 



## A Survey of Non-Rigid 3D Registration

### Representation

* **Pointwise position variables**:  
  * simply all vertices, redundant of degree of freedom
  * preserve local shape: [LZW∗ 09,HBH11]
  * local similarity: [YKM13]
  * 我觉得可以从这里截取出一些代码
* **Pointwise affine transformation**:
  * Affine transformation on each vertices
  *  [ARV07,YMYK14,YLLL15,LYLG19, YGL∗ 19]
* **Deformation graph-based methods** 

