from numpy.core.numeric import correlate
import plotly.express as px
import csv
import numpy as np

def getdatasource(data_path):
    icecreamsales=[]
    colddrinksales=[]

    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)


        for row in csv_reader:
            icecreamsales.append(float(row["Temperature"]))
            colddrinksales.append(float(row["Ice-cream Sales"]))
        
    return{"x":icecreamsales,"y":colddrinksales}


def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("correlation between icecream sales and temprature is -> ",correlation[0,1])

def setup():
    data_path="Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"
    datasource=getdatasource(data_path)
    findcorrelation(datasource)

setup()