import setuptools #type:ignore

with open("README.md", "r", encoding="utf-8") as f:
    long_description=f.read()

__version__ = "0.0.0"

REPO_NAME="Chicken-Disease-Classification",
AUTHOR_USER_NAME="Chamika-Dilshan-Anuruddha"
SRC_REPO="cnnClassifier" 
AUTHOR_EMAIL="anuruddhaedcd@gmail.com"

setuptools.setup(
    name=SRC_REPO,  #pip install cnnClassifier
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description=" A small python package for CNN app", #Appears in PyPI search results
    long_description=long_description, #Full project description
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",  #Main project homepage
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"  #It will appear as a clickable link on PyPI
    },
    package_dir={"":"src"}, #For ALL packages (""), look inside the src/ directory.
    packages=setuptools.find_packages(where="src") #Automatically finds all packages under src/
)