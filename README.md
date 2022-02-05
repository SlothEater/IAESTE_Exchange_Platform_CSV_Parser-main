# IAESTE Exchange Platform CSV Parser

The idea behind this project was to allow IAESTE Exec members to filter through the list of o-forms found on the outgoing tab in a more refined manner.

This was accomplished though a series of filters performed in Python through Pandas DataFrames. The version of Python used was 3.8.7, however any Python3 version should work on it.

Currently there are a total of 3 filters available:
* ExchangeType, which retains COBE and FCFS
* OfferType, which retains non-remote jobs
* Country, which would retain all countries of a given continent

## Importing the data

*The process to obtain the CSV data to start making use of this process.*

To obtain this data one must navigate to the [IAESTE Exchange Platform](https://iaeste.smartsimple.ie/), select the CSV and select **Export Foreign Offers**.
Once on the Export Foreign Offers page, select **File Export** at the top left of the page, which is represented by the following icon:

![File Export](./files/images/file_export.png)

The exported data is then to be placed in the [./files/raw](./files/raw) directory.

## Changes to utils

There are a number of changes that can be done to the program to better cater for the users needs.

### Adding/Removing/Editing conditions

A user may elect to change the conditions found in [filter_conditions.py](./src/utils/filter_conditions.py):
* Change the dictionary of CONDITIONS to allow more or less data to be filtered out, dependant on the {column_name:[list_of_data_to_retain]} changed;
* Change the list of CONTINENTS_TO_KEEP to specify which continents you would like to keep;

### Amending columns to keep in final files

A user can choose to edit [columns_for_final_excel.py](./src/utils/columns_for_final_excel.py) to select which columns they would like to keep in that final output excel file.

## Installing all dependencies

The only dependency required to run this program is `pandas`. This can be installed through:

`pip install -r requirements.txt`

If a version is already installed, ensure there are no version conflicts that occur due to deprecated functions.

## Running the program

The program can be simply run from [main.py](main.py).

## The final data

The final data can be found in [./files/final](./files/final).
