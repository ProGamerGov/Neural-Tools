import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="neural-tools",
    version="0.0.2",
    author="ProGamerGov",
    description="Luminance and histogram matching tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='histogram matching histogram-matching luminance transfer luminance-transfer linear-color-transfer linear color colour',
    entry_points={
        'console_scripts': ["linear-color-transfer = color.linear_color_transfer:main",
                            "lct = color.linear_color_transfer:main",
                            "lum-transfer = color.lum_transfer:main"],
    },
    url="https://github.com/ProGamerGov/Neural-Tools",
    packages=setuptools.find_packages(),
    install_requires=['numpy', 'scipy', 'imageio', 'pillow'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Artistic Software",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
