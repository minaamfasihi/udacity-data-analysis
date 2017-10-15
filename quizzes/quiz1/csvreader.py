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

def get_unique_students(data):
  unique_students = set()
  for data_point in data:
    unique_students.add(data_point['account_key'])

  return unique_students

enrollments = read_file('..\..\..\Resources\enrollments.csv', 'rb')
unique_enrollments_student = get_unique_students(enrollments)

for enrollment in enrollments:
  enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
  enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
  enrollment['is_canceled'] = enrollment['is_canceled'] == 'True'
  enrollment['is_udacity'] = enrollment['is_udacity'] == 'True'
  enrollment['join_date'] = parse_date(enrollment['join_date'])

print "Total number of rows: ", len(enrollments)
print "Total number of unique students: ", len(unique_enrollments_student)

daily_engagement = read_file('..\..\..\Resources\daily_engagement.csv', 'rb')

for engagement_record in daily_engagement:
  engagement_record['lessons_completed'] = int(float(engagement_record['lessons_completed']))
  engagement_record['num_courses_visited'] = int(float(engagement_record['num_courses_visited']))
  engagement_record['projects_completed'] = int(float(engagement_record['projects_completed']))
  engagement_record['total_minutes_visited'] = float(engagement_record['total_minutes_visited'])
  engagement_record['utc_date'] = parse_date(engagement_record['utc_date'])
  engagement_record['account_key'] = engagement_record['acct']
  del engagement_record['acct']

unique_daily_engagement_students = get_unique_students(daily_engagement)

print "Total number of rows ",  len(daily_engagement)
print "Total number of unique students: ", len(unique_daily_engagement_students)

project_submissions = read_file('..\..\..\Resources\project_submissions.csv', 'rb')
unique_project_submitters = get_unique_students(project_submissions)

for submission in project_submissions:
  submission['completion_date'] = parse_date(submission['completion_date'])
  submission['creation_date'] = parse_date(submission['creation_date'])

print "Total number of rows", len(project_submissions)
print "Total number of unique students", len(unique_project_submitters)

surprising_enrollment_records = 0
for enrollment in enrollments:
  student = enrollment['account_key']
  if student not in unique_daily_engagement_students and enrollment['cancel_date'] != enrollment['join_date']:
    surprising_enrollment_records += 1
    print enrollment

print surprising_enrollment_records

udacity_test_accounts = set()
for enrollment in enrollments:
  if enrollment['is_udacity']:
    udacity_test_accounts.add(enrollment['account_key'])

print len(udacity_test_accounts)

def remove_udacity_accounts(data):
  non_udacity_data = []
  for data_point in data:
    if data_point['account_key'] not in udacity_test_accounts:
      non_udacity_data.append(data)

  return non_udacity_data

non_udacity_enrollments = remove_udacity_accounts(enrollments)
non_udacity_engagement = remove_udacity_accounts(daily_engagement)
non_udacity_submissions = remove_udacity_accounts(project_submissions)

print len(non_udacity_enrollments)
print len(non_udacity_engagement)
print len(non_udacity_submissions)

paid_students = {}
for entry in enrollments:
  if (entry['days_to_cancel'] == None or entry['days_to_cancel'] > 7) and entry['account_key'] not in udacity_test_accounts:
    paid_students[entry['account_key']] = entry['join_date']

print "Total number of paid students: ", len(paid_students)
