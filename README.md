# TripAdvisor Reviews Web-Scraper

Collects TripAdvisor review data for all 20+ The Escape Game locations.

## Example output
.. csv-table::
    :widths: 25 25 25 25
    :file: reviews.csv

## Setup Instructions
### Virtual Environment
Create a virtual environment to store packages. Example:
```
conda create -n TA python=3.8 anaconda
source activate TA
source deactivate
```
Install packages
```
conda install selenium
```
