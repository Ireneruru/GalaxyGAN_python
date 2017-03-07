# GalaxyGAN_python
This project is the implementation of the Paper "Generative Adversarial Networks recover features in astrophysical images of galaxies beyond the deconvolution limit" on python.

##Setup

##Prerequisites
- Python with numpy
- NVIDIA GPU + CUDA 8.0 + CuDNNv5.1
- TensorFlow 1.0

### Getting Started
- Clone this repo:
```bash
git clone https://github.com/Ireneruru/GalaxyGAN_python.git
```

##Run our code

###Preprocess the .FITs
If the mode equals zero, this is the training data. If the mode equals one, the data is used for testing.

```bash
    python roou.py --input XXX --fwhm XXX --sig XXX --figure XXX --mode 0
```
XXX is your local address.

Then modify the constants in the Config.py.

###Train the model

```bash
    python train.py
```

##Acknowledge

This project is for the space.ml project.
