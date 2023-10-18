def leapyear(year):
  if(year%4==0 and year %100!=1)or year%400 ==0:
    return True
  else:
    return False
year= int(input("enter the year:"))
if leapyear(year):
  print('{} is a leap year.'.format(year))
else:
  print('{} is not a leap year.'.format(year))