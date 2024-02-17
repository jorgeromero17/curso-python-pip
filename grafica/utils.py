def population_by_country(data, country):
  result = next(filter(lambda item: item['Country/Territory'] == country, data),[])
  return result

def get_population_by_year(data):
  population_by_year = {key[:4]: value for key, value in data.items() if key.endswith(' Population')}

  labels = list(population_by_year.keys())
  values = [int(value) for value in population_by_year.values()]
  
  return labels,values

def get_column_word_population_percentage(data):

  labels = [country['Country/Territory'] for country in data]
  values = [float(country['World Population Percentage']) for country in data if 'World Population Percentage' in country]

  return labels,values