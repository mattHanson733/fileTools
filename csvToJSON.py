import csv
from ctypes import Array 
import json
import inspect
import os
from time import sleep

csvFilename = str

def getCWD():
    csvFilename = inspect.getframeinfo(inspect.currentframe()).filename
    path = os.path.dirname(os.path.abspath(csvFilename))
    return path

def writeJSONfile(data, sk:bool):

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4, skipkeys=sk))



def make_json(): 

    data = {}

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for rows in csvReader:
            key = rows['id']
            data[key] = rows
            
    return data

def convertToArray_JSON(data, skipkeys:bool):
    JSONarray = []
    i = 0
    ids = []

    for key, value in data.items():
        i += 1
        JSONarray.append(value)
        print(f'Adding items to array: {i}', end='\r')
        ids.append(key)
    
    print('\n')
    print('Done!')
    print('\n')
    print('Writing new JSON file...')

    writeJSONfile(JSONarray, skipkeys)

    print('Finished!')
    print('\n')
    print(fr'JSON file loacted at {jsonFilePath}')
    print('\n')

def convertToJSON():
    data = make_json()
    convertToArray_JSON(data, skipkeys = True)



CWD = getCWD()

csvFilePath = str(input('CSV file path (use //): '))

jsonFilePath = CWD
jsonFilename = f'{csvFilename}_JSON.json'

useAltJSON_path = str(input('Use alternate dir for JSON file output (y or n)?: '))


if useAltJSON_path == 'y' :
    jsonFilename = str(input('JSON output filename: '))
    jsonFilePath = str(input('JSON file output path (use //): '))
    
    jsonFilePath = fr'{jsonFilePath}/{jsonFilename}.json'
else :
    jsonFilename = str(input('JSON output filename: '))
    jsonFilePath = fr'{CWD}/{jsonFilename}.json'


if csvFilePath == '' or jsonFilePath == '' :
    print('Please provide valid file path and rerun program')
else:
    print('\n')
    convertToJSON()
