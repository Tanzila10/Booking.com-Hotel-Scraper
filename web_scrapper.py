import requests  #used to send request to the websites
from bs4 import BeautifulSoup  #class name is case sensitive
import lxml
import csv
import time, random


url_text = 'https://www.booking.com/searchresults.html?ss=Delhi&ssne=Delhi&ssne_untouched=Delhi&efdco=1&label=gen173nr-10CAEoggI46AdIM1gEaGyIAQGYATO4ARfIAQzYAQPoAQH4AQGIAgGoAgG4ArDuw8YGwAIB0gIkYjk2MDc1MTItYjQwMS00YWI1LTkxNjQtZWRiYzU5OTk2MmUy2AIB4AIB&aid=304142&lang=en-us&sb=1&src_elem=sb&src=region&dest_id=3487&dest_type=region&checkin=2025-10-01&checkout=2025-10-15&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure&flex_window=2&sb_lp=1'


def web_scrapper(web_url, f_name):

    num = random.randint(3, 7)
    # processing
    
    time.sleep(num)
    #we need to tell which user we are browsing from and check if this is producing 200 as output or not
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}

    response = requests.get(url_text,headers=header)
    response.encoding = "utf-8"   # force utf-8 decode

    # html_content = response.content.decode("utf-8", errors="ignore")


        
    if response.status_code == 200:
        print("connected to the website")
        html_content = response.text
        
        #creating soup
        soup = BeautifulSoup(html_content,'lxml')
            
        # print(soup.prettify())
            
        hotel_divs = soup.find_all('div', role="listitem")
        # print(hotel_divs)
        # f_name = "hotels_data" #file name
        with open(f'{f_name}.csv', 'w', encoding='utf-8') as file_csv:
            writer = csv.writer(file_csv)
            writer.writerow(['Hotel Name', 'Location', 'Price', 'Ratings', 'Review', 'Link'])


            for hotel in hotel_divs:
                hotel_name = hotel.find('div',class_="b87c397a13 a3e0b4ffd1").text.strip()
                hotel_name if hotel_name else "NA"
                                
                location = hotel.find('span',class_="d823fbbeed f9b3563dd4").text.strip()
                location if location else "NA"
                                
                price = hotel.find('span',class_="b87c397a13 f2f358d1de ab607752a2").text.strip()
                price if price else "NA"
                

                ratings_div = hotel.find('div', class_="f63b14ab7a dff2e52086")
                ratings = ratings_div.text.strip() if ratings_div else "NA"

                
                review_div = hotel.find('div', class_="fff1944c52 fb14de7f14 eaa8455879")
                review = review_div.text.strip() if review_div else "NA"

                                
                # getting link
                link = hotel.find('a', href=True).get('href')
                link if link else 'NA'

                # print(hotel_name)  #Prints all hotel names
                # print(location)  #Prints all location of hotel
                # print(price)  #Prints all price of hotel
                # print(score)  #Prints all location of review
                # print(ratings)  #Prints all location of ratings
                # print(review)
                # print(link)

                writer.writerow([hotel_name, location, price, ratings, review, link])
                
                # print()
            print("Web Scrapped done")

    else:
        print(f"connection failed {response.status_code}")

if __name__ == '__main__':

    url = input("Please enter url! :")
    fn = input('Please give file name! :')

    # calling the function
    web_scrapper(url, fn)
