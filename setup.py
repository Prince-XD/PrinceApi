import setuptools


with open("README.md", "r") as txt:
    long_description = txt.read()

setuptools.setup(
    name='princeapi',
    version='1.0.3',
    description='Prince Api Wrapper',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
    author='prince-xd',
    author_email='prince30112001@gmail.com',
    url='https://github.com/Prince-XD/PrinceApi.git',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    install_requires= ['requests'],
    python_requires='>=3.6'
)
