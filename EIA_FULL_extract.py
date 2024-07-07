import pandas as pd
import requests 
import json
import numpy as np
from pandas import DataFrame
from lxml import html # Not needed, i think 
import zipfile 
from zipfile import ZipFile 
from pathlib import Path 

'''
# NATE ISLIP 
Background:
* Goal: To grab zip files from EIA website regarding measurements of categories listed below.
* Link (Bulk Data): https://www.eia.gov/opendata/bulkfiles.php
* Link (Data Api): https://www.eia.gov/opendata/qb.php
* Product: Pandas, panel dataframe with series_id as unique identifier and column attributes for entity
* Definition: series_id, identifies the value measured, location (Geo), data frequency, and measurement
* Other Comments:
** py -m pip --version (In command prompt)
** python -m pip install requests-html 
'''

# Extract the data 
#---------------------------------------------------------------------------------------------------

intl_data = None
def intl(): # International Energy Outlook DataFrame
    global intl_data
    r = requests.get('http://api.eia.gov/bulk/INTL.zip') # Request file from server
    with open('INTdata.zip', 'wb') as f:
        f.write(r.content) 
    unzip_file = zipfile.ZipFile('INTdata.zip', 'r') 
    unzip_file.extractall()
    IntlList = []
    with open('INTL.txt') as f: # open txt. file generated from the above code
        for jsonObj in f:
            IntlDict = json.loads(jsonObj) 
            IntlList.append(IntlDict)
        df1 = pd.DataFrame.from_dict(IntlList) # Convert from list to dictionary 
        intl_data = df1.explode('data') # Explode the list of values 
        intl_data = intl_data.reset_index(drop=True) # Reset the index values
        df2 = intl_data.dropna(subset=['data']) # Drop the NaN values 
        intl_data[['Year', 'Value']] = pd.DataFrame(df2.data.tolist(), index = df2.index) # Convert col => list, and index to sep.
        # print(final.shape) # size of data frame

nuc_data = None
def nuc(): # US Nuclear Outages 
    r = requests.get('http://api.eia.gov/bulk/NUC_STATUS.zip') # Request file from server
    with open('NUC_STATUS.zip', 'wb') as f:
        f.write(r.content) 
    unzip_file = zipfile.ZipFile('NUC_STATUS.zip', 'r') 
    unzip_file.extractall()
    nuclist = []
    with open('NUC_STATUS.txt') as f: # open txt. file generated from the above code
        for jsonObj in f:
            nucdict = json.loads(jsonObj) 
            nuclist.append(nucdict)
        df1 = pd.DataFrame.from_dict(nuclist) # Convert from list to dictionary 
        nuc_data = df1.explode('data')
        nuc_data = nuc_data.reset_index(drop=True)
        df2 = nuc_data.dropna(subset=['data']) # Drop the NaN values
        nuc_data[['Year', 'Value']] = pd.DataFrame(df2.data.tolist(), index = df2.index) # Convert col => list, and index to sep.

pet_data = None
def pet(): # Petroleum 
    global pet_data
    r = requests.get('http://api.eia.gov/bulk/PET.zip') # Request file from server
    with open('PET.zip', 'wb') as f:
        f.write(r.content) 
    unzip_file = zipfile.ZipFile('PET.zip', 'r') 
    unzip_file.extractall()
    petlist = []
    with open('PET.txt') as f: # open txt. file generated from the above code
        for jsonObj in f:
            petdict = json.loads(jsonObj) 
            petlist.append(petdict)
        df1 = pd.DataFrame.from_dict(petlist) # Convert from list to dictionary 
        # print(df1.shape) # optional 
        pet_data = df1.explode('data')
        # print(pet_data.shape) # optional 
        pet_data = pet_data.reset_index(drop=True)
        df2 = pet_data.dropna(subset=['data']) # Drop the NaN values
        pet_data[['Year', 'Value']] = pd.DataFrame(df2.data.tolist(), index = df2.index) # Convert col => list, and index to sep.
        # print(pet_data[['Year', 'Value', 'series_id']].head(30))

ng_data = None
def ng(): # Natural Gas 
    global ng_data
    r = requests.get('http://api.eia.gov/bulk/NG.zip') # Request file from server
    with open('NG.zip', 'wb') as f:
        f.write(r.content) 
    unzip_file = zipfile.ZipFile('NG.zip', 'r') 
    unzip_file.extractall()
    nglist = []
    with open('NG.txt') as f: # open txt. file generated from the above code
        for jsonObj in f:
            ngdict = json.loads(jsonObj) 
            nglist.append(ngdict)
        df1 = pd.DataFrame.from_dict(nglist) # Convert from list to dictionary
        #print(df1.shape) # optional 
        ng_data = df1.explode('data')
        #print(ng_data.shape) # optional 
        ng_data = ng_data.reset_index(drop=True)
        df2 = ng_data.dropna(subset=['data']) # Drop the NaN values
        ng_data[['Year', 'Value']] = pd.DataFrame(df2.data.tolist(), index = df2.index) # Convert col => list, and index to sep.
        # print(ng_data[['Year', 'Value', 'series_id']].head(30))

te_data = None
def te(): # Total Energy
    global te_data
    r = requests.get('http://api.eia.gov/bulk/TOTAL.zip') # Request file from server
    with open('TOTAL.zip', 'wb') as f:
        f.write(r.content) 
    unzip_file = zipfile.ZipFile('TOTAL.zip', 'r') 
    unzip_file.extractall()
    telist = []
    with open('TOTAL.txt') as f: # open txt. file generated from the above code
        for jsonObj in f:
            tedict = json.loads(jsonObj) 
            telist.append(tedict)
        df1 = pd.DataFrame.from_dict(telist) # Convert from list to dictionary
        #print(df1.shape) # optional 
        te_data = df1.explode('data')
        #print(te_data.shape) # optional 
        te_data = te_data.reset_index(drop=True)
        df2 = te_data.dropna(subset=['data']) # Drop the NaN values
        te_data[['Year', 'Value']] = pd.DataFrame(df2.data.tolist(), index = df2.index) # Convert col => list, and index to sep.
        #print(te_data[['Year', 'Value', 'series_id']].head(30))

sed_data = None
def seds(): # State Energy Data System (SEDS)
    global sed_data
    r = requests.get('http://api.eia.gov/bulk/SEDS.zip') # Request file from server
    with open('SEDS.zip', 'wb') as f:
        f.write(r.content) 
    unzip_file = zipfile.ZipFile('SEDS.zip', 'r') 
    unzip_file.extractall()
    sedlist = []
    with open('SEDS.txt') as f: # open txt. file generated from the above code
        for jsonObj in f:
            seddict = json.loads(jsonObj) 
            sedlist.append(seddict)
        df1 = pd.DataFrame.from_dict(sedlist) # Convert from list to dictionary
        #print(df1.shape) # optional 
        sed_data = df1.explode('data')
        #print(sed_data.shape) # optional 
        sed_data = sed_data.reset_index(drop=True)
        df2 = sed_data.dropna(subset=['data']) # Drop the NaN values
        sed_data[['Year', 'Value']] = pd.DataFrame(df2.data.tolist(), index = df2.index) # Convert col => list, and index to sep.
        #print(sed_data[['Year', 'Value', 'series_id']].head(30))

elec_data = None
def elec(): # Electricity 
    global elec_data
    r = requests.get('http://api.eia.gov/bulk/ELEC.zip') # Request file from server
    with open('ELEC.zip', 'wb') as f:
        f.write(r.content) 
    unzip_file = zipfile.ZipFile('ELEC.zip', 'r') 
    unzip_file.extractall()
    eleclist = []
    with open('ELEC.txt') as f: # open txt. file generated from the above code
        for jsonObj in f:
            elecdict = json.loads(jsonObj) 
            eleclist.append(elecdict)
        df1 = pd.DataFrame.from_dict(eleclist) # Convert from list to dictionary
        #print(df1.shape) # optional 
        elec_data = df1.explode('data')
        #print(elec_data.shape) # optional
        elec_data = elec_data.reset_index(drop=True)
        df2 = elec_data.dropna(subset=['data']) # Drop the NaN values
        elec_data[['Year', 'Value']] = pd.DataFrame(df2.data.tolist(), index = df2.index) # Convert col => list, and index to sep.
        #print(elec_data[['Year', 'Value', 'series_id']].head(30))

df1 = None # We want to store the data for use with other dataframes
def elec_df_generator():
    global df1
    elec() # access 
    df_elec = elec_data[['series_id', 'Year', 'Value']]
    df_elec.set_index('series_id', inplace = True) # Index by series ID
    lst1 = []
    lst1 = [item for item in input("Please Input a string of Series_Id's: ").split()] # Creates a list with specific series IDs
    df1 = pd.DataFrame()
    for i in lst1: 
        df2 = df_elec.loc[i]
        df1 = df1.append(df2)
    df1.reset_index()
    print(df1.head(100))
    print(type(df2))

eba_data = None
def eba(): # US electric system operating data 
    global eba_data
    r = requests.get('http://api.eia.gov/bulk/EBA.zip') # Request file from server
    with open('EBA.zip', 'wb') as f:
        f.write(r.content) 
    unzip_file = zipfile.ZipFile('EBA.zip', 'r') 
    unzip_file.extractall()
    ebalist = []
    with open('EBA.txt') as f: # open txt. file generated from the above code
        for jsonObj in f:
            ebadict = json.loads(jsonObj) 
            ebalist.append(ebadict)
        df1 = pd.DataFrame.from_dict(ebalist) # Convert from list to dictionary
        #print(df1.shape) # optional 
        eba_data = df1.explode('data')
        #print(eba_data.shape) # optional
        eba_data = eba_data.reset_index(drop=True)
        df2 = eba_data.dropna(subset=['data']) # Drop the NaN values
        eba_data[['Year', 'Value']] = pd.DataFrame(df2.data.tolist(), index = df2.index) # Convert col => list, and index to sep.
        #print(eba_data[['Year', 'Value', 'series_id']].head(30))

coal_data = None
def coal(): # Coal 
    global coal_data
    r = requests.get('http://api.eia.gov/bulk/COAL.zip') # Request file from server
    with open('COAL.zip', 'wb') as f:
        f.write(r.content) 
    unzip_file = zipfile.ZipFile('COAL.zip', 'r') 
    unzip_file.extractall()
    coallist = []
    with open('COAL.txt') as f: # open txt. file generated from the above code
        for jsonObj in f:
            coaldict = json.loads(jsonObj) 
            coallist.append(coaldict)
        df1 = pd.DataFrame.from_dict(coallist) # Convert from list to dictionary
        #print(df1.shape) # optional 
        coal_data = df1.explode('data')
        #print(coal_data.shape) # optional 
        coal_data = coal_data.reset_index(drop=True)
        df2 = coal_data.dropna(subset=['data']) # Drop the NaN values
        coal_data[['Year', 'Value']] = pd.DataFrame(df2.data.tolist(), index = df2.index) # Convert col => list, and index to sep.
        #print(coal_data[['Year', 'Value', 'series_id']].head(30))

steo_data = None
def steo(): # Short-Term Energy Outlook 
    global steo_data
    r = requests.get('http://api.eia.gov/bulk/STEO.zip') # Request file from server
    with open('STEO.zip', 'wb') as f:
        f.write(r.content) 
    unzip_file = zipfile.ZipFile('STEO.zip', 'r') 
    unzip_file.extractall()
    steolist = []
    with open('STEO.txt') as f: # open txt. file generated from the above code
        for jsonObj in f:
            steodict = json.loads(jsonObj) 
            steolist.append(steodict)
        df1 = pd.DataFrame.from_dict(steolist) # Convert from list to dictionary
        #print(df1.shape) # optional 
        steo_data = df1.explode('data')
        #print(steo_data.shape) # optional 
        steo_data = steo_data.reset_index(drop=True)
        df2 = steo_data.dropna(subset=['data']) # Drop the NaN values
        steo_data[['Year', 'Value']] = pd.DataFrame(df2.data.tolist(), index = df2.index) # Convert col => list, and index to sep.
        #print(steo_data[['Year', 'Value', 'series_id']].head(30))

# Testing Data frames are accesible from a global environment 

def size_of_data(): # Returns dimensions of Data Matrix
    intl()
    print(intl_data.shape)
    pet()
    print(pet_data.shape)
    ng()
    print(ng_data.shape)
    te()
    print(te_data.shape)
    seds()
    print(sed_data.shape)
    elec()
    print(elec_data.shape)
    eba()
    print(eba_data.shape)
    coal()
    print(coal_data.shape)
    steo()
    print(steo_data.shape)

# ===============     Data Set 1: Electricity    ==================

elec_df_generator()




