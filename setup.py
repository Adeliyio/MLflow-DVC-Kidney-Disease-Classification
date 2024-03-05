import setuptools

# Read the contents of README.md file for the long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Define project metadata
__version__ = "0.0.0"  # Package version
REPO_NAME = "MLflow-DVC-Kidney-Disease-Classification"  # Name of the repository
AUTHOR_USER_NAME = "Adeliyio"  # GitHub username of the author
SRC_REPO = "cnnClassifier"  # Name of the source repository
AUTHOR_EMAIL = "oadatascientist@gmail.com"  # Author's email address

# Setup configuration
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small Python package for CNN app",
    long_description=long_description,  # Long description for PyPI
    long_description_content_type="text/markdown",  # Long description content type
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",  # Project URL
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",  # Bug tracker URL
    },
    package_dir={"": "src"},  # Directory structure of packages
    packages=setuptools.find_packages(where="src")  # Automatically find packages under "src" directory
)
