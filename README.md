# ECE324 Project

Project Topic: Exoplanet Detection

Group Members: Tian Lan

# Explaination for the folder's contents:

./data/: We store all of the data we use for our project in this folder.

./data/PS_2022.03.11_13.14.43.csv: A part of the NASA Exoplanet Archive's planetary systems table. Source: https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PS

./data/wget.exe: The wget utility. Required to download the radial velocity time series data files.

./data/wget_RADIAL.bat: Execute this batch file to download all radial velocity time series data files we use. There are more than 1000 of them.

./README.md: This file.

# ./parse.py: The code we wrote to parse the radial velocity time series data files. (You may want to read this.)

# ./table_parser.py: The code we wrote to parse the PS_2022.03.11_13.14.43.csv file. (You may want to read this.)
