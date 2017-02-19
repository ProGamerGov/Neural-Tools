# Neural-Tools
Tools made for usage alongside artistic style transfer projects

# Linear Color Transfer

The `match_color` function's code comes from the very talented Leon Gatys' code [here](https://github.com/leongatys/NeuralImageSynthesis/blob/master/ExampleNotebooks/ScaleControl.ipynb). This script was developed to help enable scale control in [Neural-Style](https://github.com/jcjohnson/neural-style), but it can be used for anything else that requires linear color transfer.

Scale Control examples made with [Neural-Style](https://github.com/jcjohnson/neural-style), can be viewed [here](https://github.com/ProGamerGov/Neural-Tools/wiki/Scale-Control-Examples).

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

---

# Luminance Transfer

### Dependencies: 

`sudo apt-get install python-skimage`

`sudo pip install numpy`

If you already have [Neural-Style](https://github.com/jcjohnson/neural-style) up and running, then you should only need to install `python-skimage`.

### Parameters: 

The required input and the outputs, are dependent on the `--cp_mode` option that you choose: 

`--cp_mode`: The script's mode. Options are `lum`, `lum2`, `match`, `match_style`.

### lum:

`--content_image`: Your content image. Ex: `content.png`

`--style_image`: Your style image. Ex: `style.png`

`--org_content`: Your original unmodified content image. Ex: `original_content.png`

`--output_content_image`: The name of your output content image. Ex: content_output.png

`--output_style_image`: The name of your output style image. Ex: style_output.png

### mode match:

`--content_image`: Your content image. Ex: `content.png`

`--style_image`: Your style image. Ex: `style.png`

`--output_style_image`: The name of your output style image. Ex: style_output.png

### match_style:

`--content_image`: Your content image. Ex: `content.png`

`--style_image`: Your style image. Ex: `style.png`

`--output_content_image`: The name of your output content image. Ex: content_output.png

### lum2:

`--output_lum2`: The name of your output image from Neural-Style. Ex: out.png

`--org_content`: Your original unmodified content image. Ex: `original_content.png`

`--output_image`: The name of your output image. Ex: `output.png`

