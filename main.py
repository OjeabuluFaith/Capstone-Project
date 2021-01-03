from scraper import *
import csv
import datetime


def save_to_csv(job_listings):
    """
     accepts the extracted job listings as input and save it using a csv library.

    Args:
        job_listings (list): a list of job listings
    """
    file_name = "job_listing_" + str(datetime.date.today()) + ".csv"
    with open(file_name, "w") as file:
        # write the headers
        writer = csv.DictWriter(file, fieldnames=[
                                "title", "link", "employer", "logo", "location", "type", "salary", "sector", "summary", "timestamp"])
        writer.writeheader()

        # write the rows
        for job_listing in job_listings:
            writer.writerow({'title': job_listing.title, 'link': job_listing.link,'employer':job_listing.employer,'logo':job_listing.logo,'location':job_listing.location,
                             'type':job_listing.type, 'salary':job_listing.salary, 'sector':job_listing.sector, 'summary':job_listing.summary, 'timestamp':job_listing.timestamp})


def main():
    # get total number of pages
    print("-->>> fetching total number of pages <<<--")
    pages_num = Scraper.get_pages_total()

    # get user's input of pages to be scraped
    pages_to_scrape = input(
        f"{pages_num} pages are available. How many will you like to scrape? ")
    print("\n")

    # scrape job listings under the specified pages
    no_of_pages_to_scrape = int(pages_to_scrape) if int(
        pages_to_scrape) <= pages_num else pages_num

    print(f"-->>> scraping {pages_to_scrape} pages. please wait. <<<---\n")

    job_listings = Scraper.extract_all_job_listings(no_of_pages_to_scrape)

    print(f"\n-->>> Scraping Completed <<<---\n")

    save_to_csv(job_listings)

    print(f"\n-->>> Job Listings collecting to csv <<<---\n")


if __name__ == '__main__':

    main()
