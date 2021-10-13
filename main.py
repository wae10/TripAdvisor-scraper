import csv
from csv import reader
from datetime import date, datetime
from selenium import webdriver

URLs = {
  "Downtown": "https://www.tripadvisor.com/Attraction_Review-g55229-d8725964-Reviews-The_Escape_Game_Nashville_Downtown-Nashville_Davidson_County_Tennessee.html",
  "Houston Galleria": "https://www.tripadvisor.com/Attraction_Review-g56003-d23261247-Reviews-The_Escape_Game_Houston-Houston_Texas.html",
  "Berry Hill": "https://www.tripadvisor.com/Attraction_Review-g55229-d6599132-Reviews-The_Escape_Game_Nashville_Berry_Hill-Nashville_Davidson_County_Tennessee.html",
  "Orlando": "https://www.tripadvisor.com/Attraction_Review-g34515-d7393648-Reviews-The_Escape_Game_Orlando-Orlando_Florida.html",
  "Pigeon Forge": "https://www.tripadvisor.com/Attraction_Review-g55270-d8131525-Reviews-The_Escape_Game_Pigeon_Forge-Pigeon_Forge_Tennessee.html",
  "Austin": "https://www.tripadvisor.com/Attraction_Review-g30196-d8682211-Reviews-The_Escape_Game_Austin-Austin_Texas.html",
  "Chicago": "https://www.tripadvisor.com/Attraction_Review-g35805-d11777066-Reviews-The_Escape_Game_Chicago-Chicago_Illinois.html",
  "Dallas": "https://www.tripadvisor.com/Attraction_Review-g55930-d12310008-Reviews-The_Escape_Game_Dallas-Grapevine_Texas.html",
  "Minneapolis": "https://www.tripadvisor.com/Attraction_Review-g43323-d12505388-Reviews-The_Escape_Game-Minneapolis_Minnesota.html",
  "Houston": "http://www.tripadvisor.com/Attraction_Review-g56003-d13558203-Reviews-The_Escape_Game_Houston-Houston_Texas.html",
  "Opry Mills": "https://www.tripadvisor.com/Attraction_Review-g55229-d15243015-Reviews-The_Escape_Game_Nashville_Opry_Mills-Nashville_Davidson_County_Tennessee.html",
  "Cincinnati": "https://www.tripadvisor.com/Attraction_Review-g60993-d15834581-Reviews-The_Escape_Game_Cincinnati-Cincinnati_Ohio.html",
  "Jacksonville": "https://www.tripadvisor.com/Attraction_Review-g60805-d16787429-Reviews-The_Escape_Game_Jacksonville-Jacksonville_Florida.html",
  "Atlanta": "https://www.tripadvisor.com/Attraction_Review-g60898-d16969414-Reviews-The_Escape_Game_Atlanta-Atlanta_Georgia.html",
  "New Orleans": "https://www.tripadvisor.com/Attraction_Review-g60864-d17513768-Reviews-The_Escape_Game_New_Orleans-New_Orleans_Louisiana.html",
  "San Francisco": "https://www.tripadvisor.com/Attraction_Review-g60713-d17768057-Reviews-The_Escape_Game_San_Francisco-San_Francisco_California.html",
  "New York City": "https://www.tripadvisor.com/Attraction_Review-g60763-d18895596-Reviews-The_Escape_Game_New_York_City-New_York_City_New_York.html",
  "King of Prussia": "https://www.tripadvisor.com/Attraction_Review-g52930-d19525439-Reviews-The_Escape_Game_King_of_Prussia-King_of_Prussia_Pennsylvania.html",
  "Las Vegas": "https://www.tripadvisor.com/Attraction_Review-g45963-d20171620-Reviews-The_Escape_Game_Las_Vegas-Las_Vegas_Nevada.html",
  "Irvine": "https://www.tripadvisor.com/Attraction_Review-g32530-d21283729-Reviews-The_Escape_Game_Irvine-Irvine_California.html"
}

today = date.today()

driver = webdriver.Chrome("/Users/williameverett/Desktop/TEG/Reviews/TripAdvisor/chromedriver")


# remove today's data if it exists
lines = list()


with open("/Users/williameverett/Desktop/TEG/Reviews/TripAdvisor/reviews.csv", 'r') as readFile:

    reader = csv.reader(readFile)

    for row in reader:
        #handle blank cells
        if any(field.strip() for field in row):
            lines.append(row)

            try:
                csv_date = datetime.strptime(row[0], "%m/%d/%y").date()

                print(csv_date, today)
                # has today's data been pulled yet?
                if csv_date == today:
                    print("date is today")

                    lines.remove(row)
            except:
                try:
                    csv_date = datetime.strptime(row[0], "%Y-%m-%d").date()

                    print(csv_date, today)
                    # has today's data been pulled yet?
                    if csv_date == today:
                        print("date is today")

                        lines.remove(row)
                except:
                    print(row[0])

#write old, cleaned data to csv file 
with open('/Users/williameverett/Desktop/TEG/Reviews/TripAdvisor/reviews.csv', 'w') as writeFile:

    writer = csv.writer(writeFile)

    writer.writerows(lines)



# Prepare CSV file to add new data 
csvFile = open("/Users/williameverett/Desktop/TEG/Reviews/TripAdvisor/reviews.csv", "a", newline='', encoding="utf-8")
csvWriter = csv.writer(csvFile)

for location in URLs.keys():

    driver.get(URLs[location])

    try:
        excellent = driver.find_element_by_xpath('//*[@id="tab-data-qa-reviews-0"]/div/div[3]/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div').text
    except:
        print("No 'excellent' xpath found for:",location)
        excellent = 0

    try:
        very_good = driver.find_element_by_xpath('//*[@id="tab-data-qa-reviews-0"]/div/div[3]/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div').text
    except:
        print("No 'very good' xpath found for:",location)
        very_good = 0
    
    try:
        average = driver.find_element_by_xpath('//*[@id="tab-data-qa-reviews-0"]/div/div[3]/div[1]/div[2]/div/div[3]/div[2]/div/div/div').text
    except:
        print("No 'average' xpath found for:",location)
        average = 0
    
    try:
        poor = driver.find_element_by_xpath('//*[@id="tab-data-qa-reviews-0"]/div/div[3]/div[1]/div[2]/div/div[4]/div[2]/div/div/div').text
    except:
        print("No 'poor' xpath found for:",location)
        poor = 0
    
    try:
        terrible = driver.find_element_by_xpath('//*[@id="tab-data-qa-reviews-0"]/div/div[3]/div[1]/div[2]/div/div[5]/div[2]/div/div/div').text
    except:
        print("No 'terrible' xpath found for:",location)
        terrible = 0


    print((today, location, excellent, very_good, average, poor, terrible))


    # Save to CSV
    csvWriter.writerow((today, location, excellent, very_good, average, poor, terrible))







# Close CSV file and browser
csvFile.close()
driver.close()