from setuptools import find_packages,setup
setup(
name = "QAsystem with haystack",
version = "0.0.1",
author = "abhay",
author_email = "rajputjiabhay3002@gmail.com",
packages = find_packages(),
install_requiries = ["pinecone-haystack","haystack-ai","fastapi","uvicorn","python-dotenev","pathlib"]

             )