# Determine Cricket Player Ratings
*This is how the player ratings for [Indian Cricket League](icricketleague.com) were calculated*
## Collecting Raw Data
First I went to espncricinfo.com and on every countrys' player page I filtered by T20 active players and then saved the HTML page to the folder CountryPlayerPages. This would not have been required in the past, but now ESPNCricinfo does not have an all players page and the same url can direct to different pages, making it so that downloading the HTML page is needed to keep the structure consistent.
## Processing Raw Data
1) First I wrote a Python script called getCricinfoURLS.py which scraped the website addresses of all the player pages for each country and then wrote them into a csv file.
2) Next the Python script readCricinfoURLs utilizing the function CricketStatGrabber scraped basic statistics from each of the player pages and wrote them to the csv called playerRecords. It also wrote all URLS that it had errors scraping to a different csv file. This file I checked to make sure there were no important players missed and that the error was due to inconsistent formatting on ESPNCricinfo's side.
3) After this I uploaded the playerRecords.csv file to Google Sheets that can be accessed [here](https://docs.google.com/spreadsheets/d/1uxmDCrvgVCz3L2LtqHHK437fyY30-mogB2fN1710TrI/edit?usp=sharing)
4) In the Google Sheets I preformed various functions on the stats to come up with 8 different rating attributes for each player.
5) After this I downloaded an csv file containing each player's rating. Then the Python script ConvertPlayerRatings turns the csv into a JSON file usable in the actual game. 
