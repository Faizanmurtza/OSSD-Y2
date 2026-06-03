import requests
from bs4 import BeautifulSoup
import csv

def get_cars_data(car):
    url = f'https://www.pakwheels.com/new-cars/pricelist/{car}'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    cars = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        tables = soup.find_all('table')
        if not tables:
            print("No tables found on the webpage.")
        for table in tables:
            rows = table.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                if len(cols) >= 2:
                    name = cols[0].get_text(strip=True)
                    price = cols[1].get_text(strip=True)
                    cars.append({'name': name, 'price': price})
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    
    return cars

# Yeh function kisi ek car ka data scrape karega
def scrapper(car_name):
    """
    car_name: string, e.g., 'suzuki', 'toyota', 'honda'
    returns: list of dictionaries with keys 'name' and 'price'
    """
    data = get_cars_data(car_name)
    if data:
        print(f"Scraped {len(data)} entries for {car_name}")
    else:
        print(f"No data found for {car_name}")
    return data

# Yeh function data ko CSV file mein save karega
def save_to_file(data, filename):
    """
    data: list of dictionaries (like output of scrapper)
    filename: string, e.g., 'cars_data.csv'
    """
    if not data:
        print("No data to save.")
        return
    
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'price'])
        writer.writeheader()
        writer.writerows(data)
    
    print(f"Data successfully saved to {filename}")

# Example usage (agar tu directly run karega to ye kaam karega)
if __name__ == "__main__":
    # Example: scrap data for 'suzuki' cars
    car_name = "suzuki"  # tu yahan apni marzi ki car daal (honda, toyota, etc.)
    scraped_data = scrapper(car_name)
    if scraped_data:
        save_to_file(scraped_data, f"{car_name}_prices.csv")
    else:
        print("Kuch bhi nahi mila, check kar URL ya internet.")