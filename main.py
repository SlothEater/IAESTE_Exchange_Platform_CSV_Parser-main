from src.utils.filter_conditions import CONDITIONS, CONTINENTS_TO_KEEP

from src.processes.extract_countries import get_countries_by_continent
from src.processes.parse_offers import parse_and_save_offers


def main():
    # Get the relevant countries
    country_by_continent = get_countries_by_continent()
    countries_to_keep = [country_by_continent[continent]
                         for continent in CONTINENTS_TO_KEEP]
    countries_to_keep = [
        country.capitalize() for sublist in countries_to_keep for country in
        sublist
    ]

    # Set the conditions according to the results of the previous step
    conditions = CONDITIONS
    conditions['Country'] = countries_to_keep

    # Parse, filer and save the foreign offers
    parse_and_save_offers(conditions)


if __name__ == "__main__":
    main()
