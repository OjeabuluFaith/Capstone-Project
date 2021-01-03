from bs4 import BeautifulSoup as bsoup
import requests
import re
from job_listing import JobListing



class Scraper:
    """
    A class to handle all scraping operations.

    ...
    Attributes
    ----------
    base_url: str
        base URL of the website data is to be extracted from
    total_pages: int
        number of pages available for scraping


    Methods
    -------
    get_pages_total():
        get the total number of pages available to be scraped
    """
    base_url = "https://www.jobberman.com/jobs"
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    total_pages = None

    @classmethod
    def get_pages_total(cls):
        """
        A method for getting the total number of pages of job listings available

        Returns:
            int: total number of pages
        """
        with requests.Session() as session:
            page = session.get(url=cls.base_url, headers=cls.headers)
            soup = bsoup(page.text, 'html.parser')
            total_pages = soup.find_all(
                'li', class_="page-item")[-2].get_text()
            cls.total_pages = int(total_pages)
            return int(total_pages)

    @ staticmethod
    def __extract_job_listings_per_page(page_soup):
        """
        Returns job listings instances (or objects)

        Args:
            page_soup (BeatifulSoup): a data structure representing a parsed HTML or XML document

        Returns:
            list: a list of job listing instances (or objects)
        """
        containers = page_soup.find_all('article', class_="search-result")
        job_listings = []
        for container in containers:

            # Title
            try:
                title = container.find(
                    'a', class_="search-result__job-title").get("title")
            except AttributeError:
                title = "--"

            # Link
            try:
                link = container.find(
                    'a', class_="search-result__job-title").get("href")
            except AttributeError:
                link = "--"

            # Employer
            try:
                employer = container.find(
                    'div', class_="search-result__job-meta").get_text().strip()
            except AttributeError:
                employer = "--"

            # Logo
            try:
                logo = container.find(
                    'img', class_="employer-logo__image").get("data-src")
            except AttributeError:
                logo = "--"

            # Location
            try:
                location = container.find(
                    'div', class_="search-result__location").get_text().strip()
            except AttributeError:
                location = "--"

            # Type
            try:
                type = container.find(
                    'span', class_="search-result__job-type").get_text().strip()
            except AttributeError:
                type = "--"

            # Salary
            try:
                salary = container.find(
                    'div', class_="search-result__job-salary").get_text().replace('\n', '').strip()
                salary = re.sub(r"\s\s+", " ", salary)
            except AttributeError:
                salary = "--"

            # Sector
            try:
                sector_div = container.find(
                    'div', class_="search-result__job-function")
                sector = sector_div.find(
                    'span', class_="padding-lr-10 gutter-flush-under-lg").get_text().strip()
            except AttributeError:
                sector = "--"

            # Summary
            try:
                summary_div = container.find(
                    'div', class_="search-result__content")
                summary = summary_div.find('p').get_text().strip()
            except AttributeError:
                summary = "--"

            # Timestamp
            try:
                timestamp_div = container.find(
                    'div', class_="search-result__job-function")
                timestamp = timestamp_div.find(
                    'div', class_="if-wrapper-column align-self--end text--right").get_text().strip()
            except AttributeError:
                timestamp = "--"

            print(title)
            job_listing = JobListing(
                title, link, employer, logo, location, type, salary, sector, summary, timestamp)
            job_listings.append(job_listing)
        return job_listings

    @classmethod
    def extract_all_job_listings(cls, no_of_pages):
        """
        Return a list of all of job listings for the specified number of pages 

        Args:
            no_of_pages (int): number of pages to be scraped <= total page

        Returns:
            list: a flattened list of job listings for all pages scrapped
        """
        all_job_listings = []
        stop = no_of_pages + 1
        for no_of_page in range(1, stop):
            print(f"...scraping page {no_of_page} / {no_of_pages}...\n")

            url = cls.base_url + "?page=" + str(no_of_page)
            with requests.Session() as session:
                page = session.get(url=url, headers=cls.headers)
                page_soup = bsoup(page.text, 'html.parser')
                job_listings = Scraper.__extract_job_listings_per_page(
                    page_soup)
                all_job_listings.append(job_listings)

        # flatten list of all job_listings lists
        flatten_list = [
            item for sub_list in all_job_listings for item in sub_list]
        return flatten_list
