# Capacitor Sensor Project

Materials of independent study of NYU 2024 Summer, working with Arvi Gjoka and directed by Daniele Panozzo. This project aims to create a trainning pipeline of simulation and deep learning for a capacitor based deformation sensor. 

Previous paper: https://arxiv.org/pdf/1804.04013.

## Stage 1
Accuradtely model both the mechanical deformation of the sensor and its effect on the capacitence of the embedded sensors, which involves:
* Use of 3D scanner to acquire ground truth deformation
* Use of PolyFEM to simulate the elastic deformation of the sensor
* Evaluation of different elastic material models (Neo-Hookean, Mooney-Rivlin) and development of new ones if the existing ones will not fit the data up to a 10% error.
