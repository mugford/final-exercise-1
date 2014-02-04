import pandas
data = pandas.read_csv("weather_data/weather_year.csv")
col_names = data.columns.values.tolist()
col_names2=[]
for i in col_names[0:len(col_names)]:
	i=str(i).strip()
	col_names2.append(i)
outfile=open("columnNames", "w")
outfile.write('\n'.join(col_names2))


