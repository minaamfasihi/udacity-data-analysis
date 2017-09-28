import unicodecsv

with open('Resources\enrollments.csv', 'rb') as f:
	reader = unicodecsv.DictReader(f)
	enrollments = list(reader)

print enrollments[0]
