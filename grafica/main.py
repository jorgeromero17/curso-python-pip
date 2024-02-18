import utils
import charts
import read_csv
import pandas as pd

def run():
  '''
  labels,values = utils.get_column_word_population_percentage(data)
  charts.generate_pie_chart(labels,values)
  '''
  df = pd.read_csv('./data.csv')
  df = df[df['Continent'] == 'Africa']
  
  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values
  
  charts.generate_pie_chart(countries,percentages)

  data = read_csv.read_csv('./data.csv')
  country = input('Type country => ')
  country_data = utils.population_by_country(data, country)

  if len(country_data) < 1:
    print('Pais no encontrado')
    return

  labels,values = utils.get_population_by_year(country_data)
  charts.generate_bar_chart(labels,values,country)


if __name__ == '__main__':
  run()
