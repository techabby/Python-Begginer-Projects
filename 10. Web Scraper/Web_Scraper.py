import requests
from bs4 import BeautifulSoup


def scrape_website(url, output_file):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad HTTP responses
        soup = BeautifulSoup(response.text, "html.parser")
        tags = soup.find_all("h2")
        with open(output_file, "a") as f:
            for tag in tags:
                f.write(tag.text + "\n")
        print("Data has been scraped and stored in", output_file)
    except requests.exceptions.RequestException as e:
        print("Unable to connect to the website. Please try again later.")
    except Exception as e:
        print("An error occurred:", str(e))


def main():
    url = input("Enter the URL of the website you want to scrape: ")
    output_file = input("Enter the name of the output file: ")
    scrape_website(url, output_file)


if __name__ == "__main__":
    main()
