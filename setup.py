from setuptools import find_packages, setup
from typing import List

hyphen_e_dot = "-e ."

requirements_path = "requirements.txt"

def get_requirements(requirements_path: str) -> List[str]:
    with open(requirements_path, "r") as f:
        requirements = [object.strip() for object in f.readlines() if hyphen_e_dot not in object]
    return requirements
requirements = get_requirements(requirements_path)

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.1"

REPO_NAME = "Automatic-Number-Plate-Recognition-Project"
AUTHOR_NAME = "Virender Chauhan"
USER_NAME = 'vir_since2003'
SRC_REPO = "Automaitc_number_plate_recognition"
AUTHOR_EMAIL = "virchauhan657@gmail.com"


setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="Automatic Number Plate Recognition (ANPR) system using Deep Learning (DL), MLflow, and DVC.",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=requirements,
    license="Boost Software License 1.0"
)