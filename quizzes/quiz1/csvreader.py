import unicodecsv
from datetime import datetime as dt

def read_file(path, mode):
  with open(path, mode) as f:
    handler = unicodecsv.DictReader(f)
    csv_file = list(handler)

  return csv_file

def parse_date(date):
  if date == '':
    return None;
  else:
    return dt.strptime(date, '%Y-%m-%d')

def parse_maybe_int(i):
  if i == '':
    return None;
  else:
    return int(i)

enrollments = read_file('..\..\..\Resources\enrollments.csv', 'rb')
enrollments_set = set()

for enrollment in enrollments:
  enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
  enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
  enrollment['is_canceled'] = enrollment['is_canceled'] == 'True'
  enrollment['is_udacity'] = enrollment['is_udacity'] == 'True'
  enrollment['join_date'] = parse_date(enrollment['join_date'])
  enrollments_set.add(enrollment['account_key'])

print "Total number of rows: ", enrollments.__len__()
print "Total number of unique students: ", enrollments_set.__len__()

daily_engagement = read_file('..\..\..\Resources\daily_engagement.csv', 'rb')
daily_engagement_set = set()

for engagement_record in daily_engagement:
  engagement_record['lessons_completed'] = int(float(engagement_record['lessons_completed']))
  engagement_record['num_courses_visited'] = int(float(engagement_record['num_courses_visited']))
  engagement_record['projects_completed'] = int(float(engagement_record['projects_completed']))
  engagement_record['total_minutes_visited'] = float(engagement_record['total_minutes_visited'])
  engagement_record['utc_date'] = parse_date(engagement_record['utc_date'])
  daily_engagement_set.add(engagement_record['acct'])

print "Total number of rows ",  daily_engagement.__len__()
print "Total number of unique students: ", daily_engagement_set.__len__()

project_submissions = read_file('..\..\..\Resources\project_submissions.csv', 'rb')
project_submissions_set = set()

for submission in project_submissions:
  submission['completion_date'] = parse_date(submission['completion_date'])
  submission['creation_date'] = parse_date(submission['creation_date'])
  project_submissions_set.add(submission['account_key'])

print "Total number of rows", project_submissions.__len__()
print "Total number of unique students", project_submissions_set.__len__()
