# TripAdvisor Reviews Web-Scraper

Collects TripAdvisor review data for all 20+ The Escape Game locations.

## Example output
See reviews.csv file
| Date       | Location         | Excellent | Very_Good | Average | Poor | Terrible |
|------------|------------------|-----------|-----------|---------|------|----------|
| 2021-09-22 | Downtown         | 3,116     | 99        | 9       | 3    | 0        |
| 2021-09-22 | Houston Galleria | 60        | 1         | 0       | 0    | 0        |
| 2021-09-22 | Berry Hill       | 4,292     | 145       | 11      | 6    | 6        |
| 2021-09-22 | Orlando          | 6,011     | 226       | 20      | 7    | 4        |
| 2021-09-22 | Pigeon Forge     | 3,820     | 145       | 11      | 7    | 5        |
| 2021-09-22 | Austin           | 3,646     | 139       | 19      | 7    | 5        |
| 2021-09-22 | Chicago          | 2,660     | 86        | 7       | 3    | 0        |
| 2021-09-22 | Dallas           | 1,401     | 26        | 3       | 1    | 1        |
| 2021-09-22 | Minneapolis      | 2,011     | 81        | 14      | 5    | 2        |
| 2021-09-22 | Houston          | 1,405     | 29        | 6       | 0    | 0        |
| 2021-09-22 | Opry Mills       | 616       | 15        | 2       | 1    | 1        |
| 2021-09-22 | Cincinnati       | 322       | 8         | 2       | 0    | 0        |
| 2021-09-22 | Jacksonville     | 343       | 11        | 3       | 1    | 0        |
| 2021-09-22 | Atlanta          | 365       | 9         | 0       | 1    | 0        |
| 2021-09-22 | New Orleans      | 343       | 9         | 2       | 2    | 0        |
| 2021-09-22 | San Francisco    | 298       | 5         | 1       | 1    | 0        |
| 2021-09-22 | New York City    | 264       | 5         | 1       | 0    | 0        |
| 2021-09-22 | King of Prussia  | 149       | 0         | 0       | 0    | 1        |
| 2021-09-22 | Las Vegas        | 219       | 3         | 0       | 0    | 0        |
| 2021-09-22 | Irvine           | 46        | 0         | 0       | 0    | 0        |
| 2021-09-23 | Downtown         | 3,116     | 99        | 9       | 3    | 0        |
| 2021-09-23 | Houston Galleria | 63        | 1         | 0       | 0    | 1        |
| 2021-09-23 | Berry Hill       | 4,292     | 145       | 11      | 6    | 6        |
| 2021-09-23 | Orlando          | 6,011     | 226       | 20      | 7    | 4        |
| 2021-09-23 | Pigeon Forge     | 3,823     | 145       | 11      | 7    | 5        |
| 2021-09-23 | Austin           | 3,646     | 139       | 19      | 7    | 5        |
| 2021-09-23 | Chicago          | 2,660     | 86        | 7       | 3    | 0        |
| 2021-09-23 | Dallas           | 1,401     | 26        | 3       | 1    | 1        |
| 2021-09-23 | Minneapolis      | 2,011     | 81        | 14      | 5    | 2        |
| 2021-09-23 | Houston          | 1,405     | 29        | 6       | 0    | 0        |
| 2021-09-23 | Opry Mills       | 616       | 15        | 2       | 1    | 1        |
| 2021-09-23 | Cincinnati       | 325       | 8         | 2       | 0    | 0        |
| 2021-09-23 | Jacksonville     | 343       | 11        | 3       | 1    | 0        |
| 2021-09-23 | Atlanta          | 365       | 9         | 0       | 1    | 0        |
| 2021-09-23 | New Orleans      | 343       | 9         | 2       | 2    | 0        |
| 2021-09-23 | San Francisco    | 298       | 5         | 1       | 1    | 0        |
| 2021-09-23 | New York City    | 264       | 5         | 1       | 0    | 0        |
| 2021-09-23 | King of Prussia  | 149       | 0         | 0       | 0    | 1        |
| 2021-09-23 | Las Vegas        | 219       | 3         | 0       | 0    | 0        |
| 2021-09-23 | Irvine           | 46        | 0         | 0       | 0    | 0        |

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
### Automatation Setup
1. Make Python File Executable with PyInstaller
```
pyinstaller --onefile main.py
```
2. Schedule a Job with crontab
Crontab Instructions
a. Edit
```
crontab -e
```
b. Hit i to activate the INSERT mode
c. Write the job (https://crontab.guru/)
```
55 23 * * * open /Users/williameverett/Desktop/TEG/Reviews/TripAdvisor/dist/main
```
d. press esc . Then type : and write wq to save and exit (w - write, q - quit) and finally, press enter.