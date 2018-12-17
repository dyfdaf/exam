#coding:utf-8

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "exam.settings")


import django
django.setup()


def main():
	from testing.models import Student
	f = open('data.txt')
	for line in f:
		name, task = line.split('|')
		Student.objects.get_or_create(name=name, quantityOfTask=task)

	f.close()

if __name__ == "__main__":
	main()
	print("Done!")

