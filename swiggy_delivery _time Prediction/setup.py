from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

    return requirements

setup(
    name = "Food_delivery_time_prediction",
    version= "0.0.1",
    author= "Ankit kumar jha",
    author_email= "ankit.aiml625@gmail.com",
    packages= find_packages(),
    install_requirements = get_requirements("requirements.txt")
)