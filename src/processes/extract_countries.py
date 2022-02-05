from src.utils.list_of_countries import countries
from typing import Dict, List


def get_countries_by_continent() -> Dict[str, List[str]]:
    """Extract the list of countries by their respective continents

    Returns:
        Dict[str:List[str]]: A dict of continents as keys and its respective
        counties as a list of values.
    """
    country_in_cont = {}
    for country in countries:
        if country['continent'] not in country_in_cont.keys():
            country_in_cont.update(
                {country['continent']: [country['name'].lower()]})
        else:
            country_in_cont[country['continent']].append(
                country['name'].lower())
    return country_in_cont
