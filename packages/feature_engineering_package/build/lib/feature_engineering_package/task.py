import argparse
import file_operations
"""
To start running package code use below command in terminal
python3 task.py


"""
def impute_nan(df, variable, median):
	df[variable+"_median"] = df[variable].fillna(median)
	return df  


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument(
	'--localFilePath',
	type=str,
	required = True,
	help = 'Local file path to read file for feature engineering'

	)
	parser.add_argument(
	'--gcsFilePath',
	type=str,
	required=False,
	help = 'if raw files are stored in google clold storage give path to google cloud storage bucket'
	)
	parameters = parser.parse_args()
	
	#all parameters are stored in the form of namespace
	#print(parameters)
	df = file_operations.local_read_csv_file(parameters.localFilePath)
	print(df.head())
	print(df.isnull().sum())
	df = impute_nan(df,'Age',df.Age.median())
	print(df.isnull().sum())


