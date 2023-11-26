from enum import Enum

class GovernmentType(Enum):
    DEMOCRACY = 1
    REPUBLIC = 2
    AUTOCRACY = 3

class Country:
    def __init__(self, name, capital, code, population, area, gdp, government_type):
        self.name = name
        self.capital = capital
        self.code = code
        self.population = population
        self.area = area
        self.gdp = gdp
        self.government_type = government_type

class Land:
    def __init__(self, name):
        self.name = name
        self.countries = []

    def add_country(self, country):
        self.countries.append(country)

    def calculate_population_density(self):
        total_population = sum(country.population for country in self.countries)
        total_area = sum(country.area for country in self.countries)
        return total_population / total_area

def sort_countries_by_gdp(countries):
    return sorted(countries, key=lambda country: country.gdp, reverse=True)

def top_countries_by_gdp(countries, n):
    sorted_countries = sort_countries_by_gdp(countries)
    return sorted_countries[:n]

def choose_country(countries, criteria):
    filtered_countries = [country for country in countries if criteria(country)]
    return filtered_countries

if __name__ == "__main__":
    country1 = Country("USA", "Washington", "US", 331002651, 9372610, 21433225, GovernmentType.REPUBLIC)
    country2 = Country("Canada", "Ottawa", "CA", 37742154, 9984670, 1785388, GovernmentType.DEMOCRACY)
    country3 = Country("China", "Beijing", "CN", 1439323776, 9596961, 1434293, GovernmentType.AUTOCRACY)

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
        return country.government_type == GovernmentType.AUTOCRACY

    autocratic_countries = choose_country(land2.countries, criteria)

    print("Autocratic countries:")
    for country in autocratic_countries:
        print(country.name)