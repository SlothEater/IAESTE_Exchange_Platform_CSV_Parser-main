# The following are a dict of conditions that will be used to eliminate certain
# foreign offers. More can be added by simply adding a: 
# `{column_name: what_to_keep}`
# to the data. Note that country will be filled later as it is dependent on what
# continent we would like to keep.

CONDITIONS = {
    'ExchangeType': ['COBE', 'FCFS'],
    'OfferType': ['OPEN'],
    'Country': []
}

CONTINENTS_TO_KEEP = ['Europe']
