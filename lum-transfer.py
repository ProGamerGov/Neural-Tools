#This script performs the functions required for lumin transfer that 
#leongatys/NeuralImageSynthesis' Color Control code performs.
#https://github.com/leongatys/NeuralImageSynthesis/blob/master/ExampleNotebooks/ColourControl.ipynb
#Standalone script by github.com/ProGamerGov

import skimage 
import numpy as np
import argparse
import scipy.ndimage as spi
from skimage import io,transform,img_as_float
from skimage.io import imread,imsave
from PIL import Image
from numpy import eye 


parser = argparse.ArgumentParser()
parser.add_argument('--content_image', type=str, help="The content image. Ex: content.png")
parser.add_argument('--style_image', type=str, help="The style image. Ex: style.png")
parser.add_argument('--output_content_image', default='output_content.png', help="The name of your output content image. Ex: content_output.png", type=str)
parser.add_argument('--output_style_image', default='output_style.png', help="The name of your output style image. Ex: style_output.png", type=str)
parser.add_argument('--output_image', default='output_style.png', help="The name of your output image. Ex: output.png", type=str)
parser.add_argument('--org_content', default='original_content_image.png', help="The name of your original content image. Ex: org_content.png", type=str)
parser.add_argument('--output_lum2', default='out.png', help="The name of your output image from Neural-Style. Ex: out.png", type=str)
parser.add_argument('--cp_mode', default='lum', help="The script's mode. Options are: lum, lum2, match, and match_style", type=str)
parser.parse_args()
args = parser.parse_args()
cp_mode = args.cp_mode
output_content_name = args.output_content_image
output_style_name = args.output_style_image
output_a_name = args.output_image

Image.MAX_IMAGE_PIXELS = 1000000000 # Support gigapixel images

def lum_transform(image):
    """
    Returns the projection of a colour image onto the luminance channel
    Images are expected to be of form (w,h,c) and float in [0,1].
    """
    img = image.transpose(2,0,1).reshape(3,-1)
    lum = np.array([.299, .587, .114]).dot(img).squeeze()
    img = np.tile(lum[None,:],(3,1)).reshape((3,image.shape[0],image.shape[1]))
    return img.transpose(1,2,0)
  
def rgb2luv(image):
    img = image.transpose(2,0,1).reshape(3,-1)
    luv = np.array([[.299, .587, .114],[-.147, -.288, .436],[.615, -.515, -.1]]).dot(img).reshape((3,image.shape[0],image.shape[1]))
    return luv.transpose(1,2,0)
def luv2rgb(image):
    img = image.transpose(2,0,1).reshape(3,-1)
    rgb = np.array([[1, 0, 1.139],[1, -.395, -.580],[1, 2.03, 0]]).dot(img).reshape((3,image.shape[0],image.shape[1]))
    return rgb.transpose(1,2,0)

def match_color(target_img, source_img, mode='pca', eps=1e-5):
    '''
    Matches the colour distribution of the target image to that of the source image
    using a linear transform.
    Images are expected to be of form (w,h,c) and float in [0,1].
    Modes are chol, pca or sym for different choices of basis.
    '''
    mu_t = target_img.mean(0).mean(0)
    t = target_img - mu_t
    t = t.transpose(2,0,1).reshape(3,-1)
    Ct = t.dot(t.T) / t.shape[1] + eps * np.eye(t.shape[0])
    mu_s = source_img.mean(0).mean(0)
    s = source_img - mu_s
    s = s.transpose(2,0,1).reshape(3,-1)
    Cs = s.dot(s.T) / s.shape[1] + eps * np.eye(s.shape[0])
    if mode == 'chol':
        chol_t = np.linalg.cholesky(Ct)
        chol_s = np.linalg.cholesky(Cs)
        ts = chol_s.dot(np.linalg.inv(chol_t)).dot(t)
    if mode == 'pca':
        eva_t, eve_t = np.linalg.eigh(Ct)
        Qt = eve_t.dot(np.sqrt(np.diag(eva_t))).dot(eve_t.T)
        eva_s, eve_s = np.linalg.eigh(Cs)
        Qs = eve_s.dot(np.sqrt(np.diag(eva_s))).dot(eve_s.T)
        ts = Qs.dot(np.linalg.inv(Qt)).dot(t)
    if mode == 'sym':
        eva_t, eve_t = np.linalg.eigh(Ct)
        Qt = eve_t.dot(np.sqrt(np.diag(eva_t))).dot(eve_t.T)
        Qt_Cs_Qt = Qt.dot(Cs).dot(Qt)
        eva_QtCsQt, eve_QtCsQt = np.linalg.eigh(Qt_Cs_Qt)
        QtCsQt = eve_QtCsQt.dot(np.sqrt(np.diag(eva_QtCsQt))).dot(eve_QtCsQt.T)
        ts = np.linalg.inv(Qt).dot(QtCsQt).dot(np.linalg.inv(Qt)).dot(t)
    matched_img = ts.reshape(*target_img.transpose(2,0,1).shape).transpose(1,2,0)
    matched_img += mu_s
    matched_img[matched_img>1] = 1
    matched_img[matched_img<0] = 0
    return matched_img	
	
if cp_mode == 'lum':
	    style_img = args.style_image
	    content_img = args.content_image
            org_content = args.org_content
	    org_content = spi.imread(org_content, mode="RGB").astype(float)/256
            style_img = spi.imread(style_img, mode="RGB").astype(float)/256
	    content_img = spi.imread(content_img, mode="RGB").astype(float)/256
	    
            org_content = content_img.copy()
            style_img = lum_transform(style_img)
	    content_img = lum_transform(content_img)
            style_img -= style_img.mean(0).mean(0)
            style_img += content_img.mean(0).mean(0)
	
	    style_img [style_img < 0 ] = 0
	    style_img [style_img > 1 ] = 1

	    content_img [content_img < 0 ] = 0
	    content_img [content_img > 1 ] = 1

	    imsave(output_content_name, content_img)
            imsave(output_style_name, style_img)
elif cp_mode =='match':
	    style_img = args.style_image
	    content_img = args.content_image
	    style_img = spi.imread(style_img, mode="RGB").astype(float)/256
	    content_img = spi.imread(content_img, mode="RGB").astype(float)/256

            style_img = match_color(style_img, content_img, mode='pca')

	    imsave(output_style_name, style_img)
elif cp_mode == 'match_style':
	    style_img = args.style_image
	    content_img = args.content_image
 	    style_img = spi.imread(style_img, mode="RGB").astype(float)/256
	    content_img = spi.imread(content_img, mode="RGB").astype(float)/256

            content_img = match_color(content_img, style_img, mode='pca')
		
	    imsave(output_content_name, content_img)
elif cp_mode == 'lum2':
            output = args.output_lum2
            org_content = args.org_content
	    org_content = spi.imread(org_content, mode="RGB").astype(float)/256
	    output = spi.imread(output, mode="RGB").astype(float)/256
	
	    org_content = skimage.transform.resize(org_content, output.shape)
		
            org_content = rgb2luv(org_content)
            org_content[:,:,0] = output.mean(2)
            output = luv2rgb(org_content)
            output[output<0] = 0
            output[output>1]=1
	    imsave(output_a_name, output)	   
else:
            raise NameError('Unknown colour preservation mode')
			
