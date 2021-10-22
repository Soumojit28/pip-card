import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='soumojit',  
     version='0.0.1',
     scripts=['soumojit'] ,
     author="Soumojit Ash",
     author_email="Soumojit Ash",
     description="A pip - Card!",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/Soumojit28/pip-card",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )