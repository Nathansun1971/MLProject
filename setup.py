# This creates a package for the project. It is used to install the package and its dependencies.
from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # this goes into the requirement.txt and grabs the line but when the line is grabbed it also imports a \n indicating new line so we have to replace that with a blank
        requirements = [req.replace("\n","") for req in requirements]

        
        if "-e ." in requirements:
            requirements.remove("-e .")
    
    return requirements

setup(
    name = "mlproject",
    version = "0.0.1",
    author = "Nathan",
    author_email = "nathansun0523@gmail.com",
    packages = find_packages(),
    install_requires =  get_requirements("requirements.txt")
)