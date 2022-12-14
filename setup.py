from setuptools import find_packages,setup

from typing import List

REQUIREMENT_FILE_NAME="requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements()->List[str]:
    #opening file and storing as list 


    
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        #code to replace /n in the list
    requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
    #this code is for "-e. " is not needed while installing req.txt
    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list



setup(
    name="sensor",
    version="0.0.1",
    author="dhruva",
    author_email="dhruvabm88@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements(),
)