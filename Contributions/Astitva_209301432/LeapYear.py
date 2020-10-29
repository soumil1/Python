"""
Single if-else approach to check if a given year is leap or not.
"""
def isLeap(year):
	if year%4 == 0 and (year%100 != 0 or (year%100 == 0 and year%400 == 0)):
		return True
	else:
		return False
year = int(input('Enter year: '))
print(year, 'is leap year' if isLeap(year) else 'is not a leap year')