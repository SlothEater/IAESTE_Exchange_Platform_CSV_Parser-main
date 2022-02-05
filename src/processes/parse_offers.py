import pandas as pd

from os import path
from typing import Dict, List

from src.utils.paths import RAW_OFFERS_PATH, FINAL_OFFERS_PATH
from src.utils.columns_for_final_excel import FINAL_COLUMNS


def _load_foreign_offers_from_csv(raw_offers_path: str) -> pd.DataFrame:
    """Tries to load the foreign offers

    Args:
        raw_offers_path (str): The path to the raw foreign offers csv file

    Raises:
        FileNotFoundError: In the event that the file is not found in the 
        specified path, this error will be raised

    Returns:
        pd.DataFrame: The raw DataFrame of offers
    """
    if not path.isfile(raw_offers_path):
        raise FileNotFoundError('ForeignOffers.csv not found in /files/raw/, '
                                'please add it to the specificed directory.')

    return pd.read_csv(raw_offers_path)


def _filter_by_conditions(
        conditions: Dict[str, List[str]],
        foreign_offers: pd.DataFrame) -> pd.DataFrame:
    """Given a dict of conditions, filter the dataframe of foreign offers.

    Args:
        conditions (Dict[str:List[str]]): This is a dict of conditions comprised
        of a key that we are filtering for (ExchangeType) and the values we wish
        to keep (['COBE', 'FCFS'])
        foreign_offers (pd.DataFrame): An unfiltered DataFrame of foreign offers

    Returns:
        pd.DataFrame: A filtered DataFrame of foreign offers
    """
    for column_filter, list_to_filter in conditions.items():
        foreign_offers = foreign_offers[foreign_offers[column_filter].isin(
            list_to_filter)]
    return foreign_offers


def _parse_offers(conditions: Dict[str, List[str]]) -> pd.DataFrame:
    """Load foreign offers data to memory, filter it by a dict of conditions

    Args:
        conditions (Dict[str:List[str]]): This is a dict of conditions comprised
        of a key that we are filtering for (ExchangeType) and the values we wish
        to keep (['COBE', 'FCFS'])

    Returns:
        pd.Dataframe: A filtered dataframe of foreign offers
    """
    foreign_offers = _load_foreign_offers_from_csv(RAW_OFFERS_PATH)
    return _filter_by_conditions(conditions, foreign_offers)


def _save_dataframe_to_excel(df: pd.DataFrame, path: str, name: str):
    """Saves the given dataframe to the designated path 

    Args:
        df (pd.DataFrame): The given dataframe that is filtered accordingly
        path (str): The final excel save location of the dataframe
        name (str): The name of the given filter
    """
    print(f'Saving filter {name} to {path}')
    df.to_excel(path, index=False)


def parse_and_save_offers(conditions: Dict[str, List[str]]):
    """Calls the required functions to parse and save to file. Saving is done 
    through a filter interated and performed on FINAL_COLUMNS

    Args:
        conditions: Dict[str, List[str]]: This is a dict of conditions comprised
        of a key that we are filtering for (ExchangeType) and the values we wish
        to keep (['COBE', 'FCFS'])
    """
    foreign_offers = _parse_offers(conditions)
    # Possible implement conversion from Native Currency to EUR
    [_save_dataframe_to_excel(foreign_offers[filters], FINAL_OFFERS_PATH.format(
        name=name), name) for name, filters in FINAL_COLUMNS.items()]
