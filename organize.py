from automate import get_urls
import pandas as pd

df_data = get_urls()

df = pd.DataFrame(df_data, columns=["Thing", "URL"])

# df.to_csv('data.csv') # Export the datafram as a CSV file