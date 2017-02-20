# Neural-Tools
Tools made for usage alongside artistic style transfer projects

# Linear Color Transfer

The `match_color` function's code comes from the very talented Leon Gatys' code [here](https://github.com/leongatys/NeuralImageSynthesis/blob/master/ExampleNotebooks/ScaleControl.ipynb). This script was developed to help enable Scale Control in [Neural-Style](https://github.com/jcjohnson/neural-style), but it can be used for anything else that requires linear color transfer. Supported image formats include: `jpg`, `jpeg`, `png`, `tiff`, etc...

Scale Control examples made with [Neural-Style](https://github.com/jcjohnson/neural-style), can be viewed [here](https://github.com/ProGamerGov/Neural-Tools/wiki/Scale-Control-Examples).

### Dependencies: 

`sudo apt-get install python-skimage`

`sudo pip install numpy`

If you already have [Neural-Style](https://github.com/jcjohnson/neural-style) up and running, then you should only need to install `python-skimage`.

### Usage: 

Basic usage: 

```
python linear-color-transfer.py --target_image target.png --source_image source.png
```

Advanced usage: 

```
python linear-color-transfer.py --target_image target.png --source_image source.png --output_image output.png --mode pca --eps 1e-5
```

### Parameters: 

`--target_image`: The image you are transfering color to. Ex: `target.png`

`--source_image`: The image you are transfering color from. Ex: `source.png`

`--output_image`: The name of your output image. Ex: `output.png`

`--mode`: The color transfer mode. Options are `pca`, `chol`, or `sym`.

`--eps`: Your eps value in scientific notation or normal notation. Ex: `1e-5` or `0.00001`.

### Examples: 

**Source Image:** 

![](https://i.imgur.com/eoX7f3Il.jpg)

**Target Image:** 

![](https://i.imgur.com/7FPCSril.jpg)

**Output Image:** 

![](https://i.imgur.com/STZ0Mspl.png)

---

---

# Luminance Transfer

This script was developed to help enable colour control in [Neural-Style](https://github.com/jcjohnson/neural-style), also known as "Luminance Transfer". This script uses code from Leon Gatys' code [here](https://github.com/leongatys/NeuralImageSynthesis/blob/master/ExampleNotebooks/ColourControl.ipynb). Supported image formats include: `jpg`, `jpeg`, `png`, `tiff`, etc...

Luminance transfer/Color Control examples made with [Neural-Style](https://github.com/jcjohnson/neural-style), can be found [here](https://github.com/ProGamerGov/Neural-Tools/wiki/Color-Control-Examples).

### Dependencies: 

`sudo apt-get install python-skimage`

`sudo pip install numpy`

If you already have [Neural-Style](https://github.com/jcjohnson/neural-style) up and running, then you should only need to install `python-skimage`.

### Usage:

Basic usage: 

```
python lum-transfer.py --content_image content.png --style_image style.png
```

Advanced usage: 

```
python lum-transfer.py --cp_mode lum --content_image content.png --style_image style.png --org_content content.png --output_style_image output_style.png --output_content_image output_content.png
```

### Parameters: 

The required input images and the output images, are dependent on the `--cp_mode` option that you choose: 

* `--cp_mode`: The script's mode. Options are `lum`, `lum2`, `match`, `match_style`.


**Mode: `lum`**


* `--content_image`: Your content image. Ex: `content.png`

* `--style_image`: Your style image. Ex: `style.png`

* `--org_content`: Your original unmodified content image. Ex: `original_content.png`

* `--output_content_image`: The name of your output content image. Ex: `content_output.png`

* `--output_style_image`: The name of your output style image. Ex: `style_output.png`

**Mode: `match`**

* `--content_image`: Your content image. Ex: `content.png`

* `--style_image`: Your style image. Ex: `style.png`

* `--output_style_image`: The name of your output style image. Ex: `style_output.png`

**Mode: `match_style`**

* `--content_image`: Your content image. Ex: `content.png`

* `--style_image`: Your style image. Ex: `style.png`

* `--output_content_image`: The name of your output content image. Ex: `content_output.png`

**Mode: `lum2`**

* `--output_lum2`: The name of your output image from Neural-Style. Ex: `out.png`

* `--org_content`: Your original unmodified content image. Ex: `original_content.png`

* `--output_image`: The name of your output image. Ex: `output.png`

### Examples:

**The style image is adjusted to match the content image:**

![](https://i.imgur.com/Q7phTmel.png)

![](https://i.imgur.com/dRf3yZHl.png)

**After Neural-Style:**

![](https://i.imgur.com/hpW8zufl.png)

**Final ouput image:** 

![](https://i.imgur.com/Vk0ym6Ol.png)

---

