from setuptools import setup, find_packages


setup(
    name="flygym",
    version="0.2.5",
    author="Neuroengineering Laboratory, EPFL",
    author_email="sibo.wang@epfl.ch",
    description="Gym environments for NeuroMechFly in various physics simulators",
    packages=find_packages(),
    package_data={"flygym": ["data/*", "config.yaml"]},
    include_package_data=True,
    python_requires=">=3.8,<3.13",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
    ],
    install_requires=[
        "gymnasium",
        "numpy",
        "scipy",
        "pyyaml",
        "jupyter",
        "mediapy",
        "imageio",
        "imageio[pyav]",
        "imageio[ffmpeg]",
        "tqdm",
        "mujoco>=2.1.2",
        "dm_control",
        "numba",
        "opencv-python",
    ],
    extras_require={
        "dev": [
            "sphinx",
            "sphinxcontrib.googleanalytics",
            "furo",
            "numpydoc",
            "pytest",
            "ruff",
            "black==23.3.0",
            "black[jupyter]",
            "shapely",
            "rasterio",
            "requests",
        ],
        "examples": [
            "networkx",
            "lightning",
            "tensorboardX",
            "pandas",
            "scikit-learn",
            "seaborn",
            "torch",
            "phiflow",
            "flyvision @ https://github.com/TuragaLab/flyvis/archive/refs/heads/main.zip",
        ],
        "tests": ["networkx", "h5py", "scikit-learn", "torch", "lightning"],
    },
    url="https://neuromechfly.org/",
    long_description=open("README.md", encoding="UTF-8").read(),
    long_description_content_type="text/markdown",
)
