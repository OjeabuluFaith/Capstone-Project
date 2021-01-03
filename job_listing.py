class JobListing:
    """A class to represent a job listing

    ...

    Attributes
    ----------
    title: str
        title of job listing
    link: str
        link to job listing
    employer: str
        company seeking applicants for the job listing
    logo: str
        logo of employer company
    location: str
        location of the employer
    type: str
        classification of job listing either as full-time, contract, part-time, internship
    salary: str
        income offered by the employer
    sector: str
        sector the job listing falls under
    summary: str
        short description of duties to be performed
    timestamp: str
        how long the job listing has been posted


    Methods
    -------
    """

    def __init__(self, title, link, employer, logo, location, type, salary, sector, summary, timestamp):
        """
        The constructor for JobListing class

        Args:
            title (str): title of job listing
            link (str): link to job listing
            employer (str): company seeking applicants for the job listing
            logo (str): logo of employer company
            location (str): location of the employer
            type (str): classification of job listing
            salary (str): income offered by the employer
            sector (str): sector the job listing falls under
            summary (str): short description of duties to be performed
            timestamp (str): how long the job listing has been posted
        """
        self.title = title
        self.link = link
        self.employer = employer
        self.logo = logo
        self.location = location
        self.type = type
        self.salary = salary
        self.summary = summary
        self.sector = sector
        self.timestamp = timestamp
