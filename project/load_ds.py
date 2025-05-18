import pandas as pd

emissions_df = pd.read_csv("co2emission_bysecctors.csv")
gdp_pop_df = pd.read_csv("world_gdp_population.csv")

emissions_df['year'] = pd.to_datetime(emissions_df['date'], format='%d-%m-%Y').dt.year

emissions_summary = emissions_df.groupby(['country', 'year', 'sector'])['value'].sum().reset_index()
emissions_summary.rename(columns={'value': 'emissions_mt'}, inplace=True)

gdp_pop_df.rename(columns={
    'Year': 'year',
    'GDP Real (USD) ': 'gdp_usd',
    'World Population' : 'population',
}, inplace=True)

merged_df = pd.merge(emissions_summary, gdp_pop_df[['year', 'gdp_usd', 'population']], on='year', how='left')

merged_df['emissions_per_capita'] = (merged_df['emissions_mt'] * 1e6) / merged_df['population']
merged_df['emissions_per_gdp'] = (merged_df['emissions_mt'] * 1e6) / merged_df['gdp_usd']

merged_df.to_csv("cleaned_emissions_data.csv", index=False)




