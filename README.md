# DSCI560-HW5

### step 1: download dataset from GitHub

### step 2: create a blank virtual environment, name it dsci560H5 in DSCI560-HW5 folder, and then activate the environment
- `pip install virtualenv`
- `virtualenv dsci560H5`
- `source dsci560H5/bin/activate`

![data](https://github.com/jieqiong-pang/DSCI560-HW5/blob/main/Screenshot1.png)

### step 3: install the dependencies generate requirements.txt
- `pip install pandas`
- `pip install bokeh`
- `pip freeze > requirements.txt`
![data](https://github.com/jieqiong-pang/DSCI560-HW5/blob/main/Screenshot2.png)
![data](https://github.com/jieqiong-pang/DSCI560-HW5/blob/main/Screenshot3.png)

### step 4: Running the script for visualization
- `Bokeh serve --show resulting.py`

### step 5: Build container
- install [Docker Desktop](https://www.docker.com/products/docker-desktop) in computer
- clone hw5 file from GitHub: `git clone https://github.com/jieqiong-pang/DSCI560-HW5.git`
- build image named ad 'image560': `docker build --tag image560 .`
![data](https://github.com/jieqiong-pang/DSCI560-HW5/blob/main/Screenshot4.png)
