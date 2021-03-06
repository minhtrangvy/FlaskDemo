import csv
import os
print(os.getcwd())

def read_in_genres_from_csv():
    """
    Reads in the csv file that maps genre ids to their friendly names
    :return dict: genre id to friendly name
    """
    all_genres = {}
    
    with open(os.getcwd() + '/gaproject/genres.csv', 'r') as csv_file:
        genre_reader = csv.DictReader(csv_file)
        for genre in genre_reader:
            all_genres[genre['Id']] = genre['FriendlyName']
    return all_genres
