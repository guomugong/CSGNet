## CSGNet: Cascade semantic guided net for retinal vessel segmentation
Please read my [paper](https://doi.org/10.1016/j.bspc.2022.103930) for more details!
### Introduction:
Retinal vessels are essential biomarkers for the early diagnosis of ophthalmic diseases. Accurate segmentation
of retinal vessels is necessary for further quantitative analysis of fundus images. With the development of
deep learning, many deep segmentation models have been proposed and show promising results. Nevertheless,
segmentation performance is not satisfactory in tiny vessels and low-contrast vessels. A cascade semantic
guided network (CSGNet) is proposed to address this problem. CSGNet follows a low-to-high pipeline, where
low-resolution semantic-rich features are first learned. Then, higher-resolution features are learned under
the guidance of low-resolution features. In this way, CSGNet is expected to learn both semantic-rich and
detail-preserved high-resolution representations to facilitate the segmentation of thin vessels. Meantime, a
multi-scale and multi-directional feature learning (M2FL) module is developed, which leverages two strip
convolutions and two dilated convolutions to align with the shape of vessels and encode context information.
Extensive experiments are conducted to validate the segmentation performance of the proposed method over
six public datasets, including four photography datasets (CHASE\_DB1, DRIVE, STARE, HRF) and two color
scanning laser ophthalmoscopy datasets (IOSTAR, RC-SLO). Also, the proposed method is compared with
several popular deep learning-based models. Experimental results show that the proposed method achieves
comparable or superior segmentation performance compared with other deep learning-based models with fewer
parameters and faster segmentation speed. Meantime, cross-training experiments demonstrate the competitive
generalization capability of the proposed method.

# Architecture of CSGNet
![image](https://github.com/guomugong/CSGNet/blob/main/csgnet_arch.jpg)


## License
[![LICENSE](https://img.shields.io/badge/license-Anti%20996-blue.svg)](https://github.com/996icu/996.ICU/blob/master/LICENSE)
[![Badge](https://img.shields.io/badge/link-996.icu-red.svg)](https://996.icu/#/zh_CN)
