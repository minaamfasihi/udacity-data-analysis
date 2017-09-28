import unicodecsv

def read_file(path, mode):
	with open(path, mode) as f:
		handler = unicodecsv.DictReader(f)
		csv_file = list(handler)

	return csv_file

enrollments = read_file('..\..\..\Resources\enrollments.csv', 'rb')

print enrollments[0]

daily_engagement = read_file('..\..\..\Resources\daily_engagement.csv', 'rb')

print daily_engagement[0]

project_submissions = read_file('..\..\..\Resources\project_submissions.csv', 'rb')

print project_submissions[0]
