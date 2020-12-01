from sys import argv
hours, salary_per_hour, prize = map(float, argv[1:] )
print('Зарплата : {}'.format(hours * salary_per_hour + prize ))


