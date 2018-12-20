## Step 1:
The fastest way to get started with this project is by using [Docker](https://www.docker.com/). Install the latest supported version of [Docker](https://docs.docker.com/install/).
## Step 2:
Run the following commands to setup the Dispy Worker Node.
````
docker pull ubuntu
docker run -d --name dispy ubuntu
docker exec -it --name dispy bash
apt-get update
apt-get install libpython3-dev python3-pip
pip3 install dispy
python3 dispynode.py
````
This will setup the Worker Node. The above steps can be repeated more number of times to create more worker nodes.
## Step 3:
In a new shell window run the following commands to setup MongoDB.
````
docker pull mongo
docker run -d -p 8888:27017 --name mongo mongo
docker exec -it --name mongo bash
mongo
````
This will create the mongoDB container and shell into it so that the mongo database can be monitored.
In another shell windows run the following commands to setup Zeppelin running on Spark.
````
docker pull apache/zeppelin
docker run -d -p 8080:8080 --name zeppelin apache/zeppelin
````
## Step 4:
To start scraping the data, copy the files `worker.py` and `data.csv` from this repository to one of the `dispy` containers. Once inside the container, run
````
python3 worker.py
````
This will start the scraping processing.

The data is stored on the Mongo database as the scrapers are running. This can be monitored from the mongo shell which was opened in Step 3.

## Step 5:
Navigate to `localhost:8080` in the web browser to get access to Zeppelin. In the Zeppelin, import `Notebook.json` from this repository. Run all the paragraphs in the notebook to perform the data preprocessing. The last cell exports the data which can be loaded in Tableau for visualizations.