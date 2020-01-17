# School Diary

## How to run the project?
- Download it and open in command line
- pip3 install -r requierements.txt
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver

## Programming language
- Python3.7+

## Modules:
- Django==3.0.2
- django-admin-tools==0.8.1
- django-crispy-forms==1.8.1
- Pillow==7.0.0
- pytz==2019.3

## Namespaces
### Project name
- school_diary
### Names of apps
- timetable - app for showing school timetable to students and giving them an ability to download PDF copies.
- main - main app of a website which controls other apps, homepage, about ane etc.
- minimum - download 'minimums' to prepare for the exam.

## Notes
- Please follow the rules to make project editing available both on Linux & Windows!

## HTML files names
- base.html - base layout with navbar and footer
- help.html - how to use the website
- homepage.html - homepage
- social.html - social pages of the school
- timetable.html - page with form to get timetable or download it
- timetable_list.html - where tables with timetable are printed
- timetable_download.html - where users can download timetable in PDF
