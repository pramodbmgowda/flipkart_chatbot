from setuptools import find_packages, setup
from typing import List


def get_requirements() ->List[str]:

  
    requirement_list:List[str] = []

   
    return requirement_list

setup(
    name = "flipkart",
    version= "0.0.1",
    author="Pramod_BM",
    author_email="pramodbmgowda7@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)