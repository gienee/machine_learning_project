from setuptools import setup   ### used to install the requirements,txt file, we do not need to use pip install.
from typing import List
def get_requirements_list()->List[str]:  ###it is going to return the list which has strings in it,it icreases the readability
    pass

###Declaring the variables

PROJECT_NAME="housing-predictor"
VERSION="0.0.1"    ###we can change the version time to time,so,the change we r going to done in the project will be going to update  to update time to time
AUTHOR="Nikita"
DESCRIPTION="This is my first machine learning project"
PACKAGES="housing"


def get_requirements_list()->List[str]: ### it is going to give us the list of string datatype which contained all the libraries mentioned in the requirements.txt file.
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES
    install_requires=get_requirements_list()
)