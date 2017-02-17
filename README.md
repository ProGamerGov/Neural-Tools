# Neural-Tools
Tools made for usage alongside artistic style transfer projects

# Linear Color Transfer

The `match_color` function's code comes from the very talented Leon Gatys' code [here](https://github.com/leongatys/NeuralImageSynthesis/blob/master/ExampleNotebooks/ScaleControl.ipynb). This script was developed to help enable scale control in [Neural-Style](https://github.com/jcjohnson/neural-style).

### Usage: 

Basic usage: 

```
python linear-color-transfer.py --target_image target.png --source_image source.png
```

Advanced usage: 

```
python linear-color-transfer.py --target_image target.png --source_image source.png --output_image output.png --mode pca --eps 1e-5
```

### Dependencies: 

`sudo apt-get install python-skimage`

`sudo pip install numpy`

If you already have [Neural-Style](https://github.com/jcjohnson/neural-style) up and running, then you should only need to install `python-skimage`.

### Parameters: 

`--target_image`: The image you are transfering color to. Ex: `target.png`

`--source_image`: The image you are transfering color from. Ex: `source.png`

`--output_image`: The name of your output image. Ex: `output.png`

`--mode`: The color transfer mode. Options are `pca`, `chol`, or `sym`.

`--eps`: Your eps value in scientific notation or normal notation. Ex: `1e-5` or `0.00001`.

### Examples: 

Source Image: 

![](https://i.imgur.com/eoX7f3Il.jpg)

Target Image: 

![](https://i.imgur.com/7FPCSril.jpg)

Output Image: 

![](https://i.imgur.com/STZ0Mspl.png)
