import pandas as pd
import plotly_express as px
import csv
import numpy as np

def getDataSource(data_path):
    sleep1 = []
    coffee1 = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            sleep1.append(float(row['dayspresent']))
            coffee1.append(float(row['percent']))
    return{'x':coffee1, 'y':sleep1}

def findCorelation(dataSource):
    correlation = np.corrcoef(dataSource['x'],dataSource['y'])
    print('Correlation between sleep hours and coffee sales \n -->', correlation[0,1])
    
def setup():
    data_path = './csv/attendance.csv'
    dataSource = getDataSource(data_path)
    findCorelation(dataSource)
setup()


        
