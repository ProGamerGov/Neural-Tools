import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="neural-tools",
    version="0.0.1.dev1",
    author="ProGamerGov",
    description="Luminance and histogram matching tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='histogram matching histogram-matching luminance transfer luminance-transfer linear-color-transfer linear color colour',
    scripts=['linear-color-transfer', 'lum-transfer'],
    url="https://github.com/ProGamerGov/Neural-Tools",
    packages=setuptools.find_packages(),
    install_requires=['numpy', 'scipy', 'scikit-image', 'pillow'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
