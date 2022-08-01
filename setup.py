import os , codecs

from setuptools import setup, find_packages

pkg = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(pkg, "README.md"), encoding="utf-8") as fh:
	
    long_description = "\n" + fh.read()


setup(

    name="SalamInsta",
    
    version="1.0.2",
    
    author="salammzere3",
    
    author_email="salammzere0@gmail.com",
    
    description = ("For developers"),
    
    long_description_content_type="text/markdown",
    
    url="https://github.com/salammzere3/SalamInsta",
    
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    
    long_description=long_description,
    
    packages=find_packages(),
    
    install_requires=['requests', 'geocoder', 'user_agent', 'pyfiglet'],
    
    keywords=['SalamInsta'],
    
    classifiers=[
    
        "Development Status :: 1 - Planning",
        
        "Intended Audience :: Developers",
        
        "Programming Language :: Python :: 3",
        
        "Operating System :: Unix",
        
        "Operating System :: MacOS :: MacOS X",
        
        "Operating System :: Microsoft :: Windows",
    ]
)
