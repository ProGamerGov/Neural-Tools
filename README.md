# Neural-Tools
Tools made for usage alongside artistic style transfer projects

# Linear Color Transfer:

Basic usage: `python linear-color-transfer.py --target_image target.png --source_image source.png`

### Parameters: 

`--target_image`: The image you are transfering color to. Ex: target.png

`--source_image`: The image you are transfering color from. Ex: source.png

`--output_image`: The name of your output image. Ex: output.png

`--mode`: The color transfer mode. Options are pca, chol, or sym.

`--eps`: Your eps value in scientific notation or normal notation. Ex: 1e-5
