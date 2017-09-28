import unicodecsv

with open('..\..\..\Resources\enrollments.csv', 'rb') as f:
	reader = unicodecsv.DictReader(f)
	enrollments = list(reader)

print enrollments[0]

with open('..\..\..\Resources\daily_engagement.csv', 'rb') as f:
	reader = unicodecsv.DictReader(f)
	daily_engagement = list(reader)

print daily_engagement[0]