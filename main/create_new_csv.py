from utilities.utilities import read_csv, transform_csv, write_csv

zillow_df = read_csv('zillow.csv')
clean_zillow_df = transform_csv(zillow_df)
write_csv(clean_zillow_df)

