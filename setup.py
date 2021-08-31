from setuptools import setup, find_packages
import pathlib

requirements = pathlib.Path("requirements.txt").read_text(encoding="utf-8").splitlines()

install_requires = [
    req.strip()
    for req in requirements
    if req.strip() and ("git+" not in req) and (not req.startswith("#")) and (not req.startswith("-"))
]

setup(
    name="megakeep",
    description=(
        'Simple command-line application to "touch" your Mega accounts and avoid getting closed due to inactivity'
    ),
    version="1.1.1",
    packages=find_packages(),
    install_requires=install_requires,
    python_requires=">=3.8",
    entry_points={"console_scripts": ["megakeep=megakeep.megakeep:main"]},
    author="Neria Tzidkani",
    keyword="mega, mega.nz, mega.co.nz, keepalive, login",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://neria.dev",
    dependency_links=[x.strip().replace("git+", "") for x in requirements if "git+" not in x],
    author_email="me@neria.dev",
)
