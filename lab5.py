"""
A module providing a base class for creating enumerations.
Enums created using this module are iterable and can be compared using their members.
"""
from enum import Enum

class GovernmentType(Enum):
    """
    Enum representing different types of government.
    """
    DEMOCRACY = 1
    REPUBLIC = 2
    AUTOCRACY = 3

class Country:
    """
    Class representing a country with its basic attributes.

    Attributes:
        name (str): The name of the country.
        capital (str): The capital city of the country.
        code (str): The country code.
        population (int): The population of the country.
        area (float): The area of the country in square kilometers.
        gdp (int): The GDP of the country.
        government_type (GovernmentType): The type of government in the country.
    """
    def __init__(self, name, capital, code, gross_domestic_product, **kwargs):
        """
        Initializes a new Country object.

        Args:
            name (str): The name of the country.
            capital (str): The capital city of the country.
            code (str): The country code.
            gross_domestic_product (int): The GDP of the country.
            kwargs: Additional attributes, such as population, area, and government_type.
        """
        self.name = name
        self.capital = capital
        self.code = code
        self.gdp = gross_domestic_product
        self.population = kwargs.get('population', None)
        self.area = kwargs.get('area', None)
        self.government_type = kwargs.get('government_type', None)

class Land:
    """
    Class representing a landmass with countries.

    Attributes:
        name (str): The name of the landmass.
        countries (list): List of countries in the landmass.
    """
    def __init__(self, name):
        self.name = name
        self.countries = []

    def add_country(self, country):
        """
        Adds a country to the landmass.

        Args:
            country (Country): The country to be added.
        """
        self.countries.append(country)

    def calculate_population_density(self):
        """
        Calculates the population density of the landmass.

        Returns:
            float: The population density in people per square kilometer.
        """
        total_population = sum(country.population for country in self.countries)
        total_area = sum(country.area for country in self.countries)
        return total_population / total_area

def sort_countries_by_gdp(countries):
    """
    Sorts a list of countries by GDP in descending order.

    Args:
        countries (list): List of Country objects.
    """
    return sorted(countries, key=lambda country: country.gdp, reverse=True)

def top_countries_by_gdp(countries, n):
    """
    Returns the top N countries by GDP from the given list.

    Args:
        countries (list): List of Country objects.
        n (int): The number of top countries to return.
    """
    sorted_countries = sort_countries_by_gdp(countries)
    return sorted_countries[:n]

def choose_country(countries, criteria):
    """
    Filters countries based on the provided criteria function.

    Args:
        countries (list): List of Country objects.
        criteria (function): A function that takes a Country object as input and returns a boolean.
    """
    filtered_countries = [country for country in countries if criteria(country)]
    return filtered_countries

if __name__ == "__main__":
    country1 = Country("USA",
                       "Washington",
                       "US", 21433225,
                       population=331002651,
                       area=9372610,
                       government_type=GovernmentType.REPUBLIC)
    country2 = Country("Canada",
                       "Ottawa",
                       "CA",
                       1785388,
                       population=37742154,
                       area=9984670,
                       government_type=GovernmentType.DEMOCRACY)
    country3 = Country("China",
                       "Beijing",
                       "CN",
                       1434293,
                       population=1439323776,
                       area=9596961,
                       government_type=GovernmentType.AUTOCRACY)

    land1 = Land("North America")
    land1.add_country(country1)
    land1.add_country(country2)

    land2 = Land("East Asia")
    land2.add_country(country3)

    population_density = land1.calculate_population_density()
    print(f"Population of North America: {population_density} people per square kilometer")

    print("============")

    top_gdp_countries = top_countries_by_gdp(land1.countries, 3)
    print("Top 2 countries by GDP:")
    for country in top_gdp_countries:
        print(f"{country.name}: {country.gdp}")

    print("============")

    def criteria(country):
        """
        Checks if the government type of a country is AUTOCRACY.

        Args:
        country (Country): The country object to check.
        """
        return country.government_type == GovernmentType.AUTOCRACY

    autocratic_countries = choose_country(land2.countries, criteria)

    print("Autocratic countries:")
    for country in autocratic_countries:
        print(country.name)
