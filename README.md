# MegaKeep

Simple command-line application to "touch" your Mega accounts and avoid getting closed due to inactivity.

## How to use?
#### Install package
run:  
```bash
pip install megakeep
```    
#### Create passwords file
create file containing your mega account
- each line should contain email and password separated in space/tab.
- multiple spaces are allowed.
- comments are allowed (# and //).
- empty lines are allowed.

i.e.:
```text
bla@email.com       mypa55
another@account.com n1cePass
# Bob's account:
bob_mega@gmail.com  ilovemega
// my secret account
oh@im.god look-at-my-drive
```  
#### Run
run one of the following:  
```bash
megakeep --file mega.txt
megakeep -f mega.txt
``` 

or if your file named mega.txt and in your current directory:  
```bash
megakeep
``` 

##### All flags
- --help
- --file _or_ -f
- --skip-fails _or_ -s

## Run megakeep from source
- git clone the project
- run ```python -m main.py --file path/to/file```

## Build megakeep from source
- git clone the project
- run ```python setup.py install```

## Install megakeep from source
- git clone the project
- run ``` python setup.py sdist bdist_wheel```

## Upload to PyPI
- ```pip install twine```
- ```twine upload --repository-url https://test.pypi.org/legacy/ dist/*```
- ```twine upload dist/*```   
