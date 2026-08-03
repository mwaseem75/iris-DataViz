
# Summary

**iris-DataViz** is an Exploratory Data Analysis and Visualization Streamlit Application that leverages the functionality of [**IRIS embedded python**](https://docs.intersystems.com/irisforhealthlatest/csp/docbook/DocBook.UI.Page.cls?KEY=AFL_epython) and SQLAlchemy to interact with IRIS, as well as the [**PyGWalker**](https://kanaries.net/pygwalker) python library for data analysis and data Visualization. PyGWalker (Python Graphic Walker) is an interactive data visualization library built for Python, aiming to bring the ease and functionality of **Tableau-style** drag-and-drop visualization into Python environments.

[![one](https://img.shields.io/badge/Platform-InterSystems%20IRIS-blue)](https://www.intersystems.com/data-platform/) [![one](https://img.shields.io/badge/WebFrameWork-Streamlit-Orange)](https://streamlit.io/) [![one](https://img.shields.io/badge/VectorStore-IRIS-blue)](https://www.intersystems.com/data-platform/) [![one](https://img.shields.io/badge/ORM-SQLAlchemy-teal)](https://www.sqlalchemy.org/)  [![one](https://img.shields.io/badge/PythonLib-pygwalker-yellow)](https://docs.kanaries.net/pygwalker) [![OEX](https://img.shields.io/badge/Available%20on-Intersystems%20Open%20Exchange-00b2a9.svg)](https://github.com/mwaseem75/iris-RAG-Gen/blob/main/LICENSE) [![license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/mwaseem75/iris-RAG-Gen/blob/main/LICENSE)

# Application Interface
![](https://github.com/mwaseem75/iris-DataViz/blob/main/appInfo.gif)

# Features
* Drag-and-Drop Visualization
* Manipulate and clean your data within the visualization
* Wide Range of Chart Types:
* Interactive Data Exploration
* Interactive Aggregation and Grouping:
* Exportable Visualizations
* Automatic Data Summarization
* Calculated / Computed Fields
* Support for Categorical, Numerical, and Temporal Data
* Interactive Legends and Filters
* Interactive Report Generation
* Geospatial Data Support


# Installation
1. Clone/git pull the repo into any local directory

```
git clone https://github.com/mwaseem75/iris-DataViz.git
```

2. Open a Docker terminal in this directory and run:

```
docker-compose build
```

3. Run the IRIS container:

```
docker-compose up -d 
```

## Management Portal
Application already imported car-related data. In order to view the data navigate to the Management Portal SQL [(http://localhost:52773/csp/sys/exp/%25CSP.UI.Portal.SQL.Home.zen?$NAMESPACE=USER)](http://localhost:52773/csp/sys/exp/%25CSP.UI.Portal.SQL.Home.zen?$NAMESPACE=USER) to view Data [SuperUser | SYS]
<img width="960" alt="image" src="https://github.com/user-attachments/assets/754986ea-4500-4881-96a7-1c0c6b4f5058">

## Run Streamlit Web Application
To run the application Navigate to [**http://localhost:8051**](http://localhost:8051) 

On macOS, you need to start the application manually. Run the following command inside the container:
```
streamlit run /irisdev/app/src/python/dataviz/app.py --server.port=8051 --server.address=0.0.0.0 
```

Select Namespace,Schema and table. Click on Data tab to view the data
![image](https://github.com/user-attachments/assets/5aa606ef-a1ea-43bb-a7d9-419b6992902c)

Drag desired columns in X-Axis and Y-Axis, and select the desired graph type.
![image](https://github.com/user-attachments/assets/fb2c5b30-52ab-4ee5-afbc-2b236c01e261)
