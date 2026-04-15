## Overview
A python based fast CLI Tool for Educative Course downloading.



### Setup
Open the project folder.

Create a .env file in the project root.

Add your Educative cookies in one line like this:

COOKIES=your_full_cookie_string_here

The code reads this value from the environment and uses it for authenticated API requests.

### USAGE

```python
from KursoDownloaderLowLevelDesign.coursesearch import CourseSearch
from KursoDownloaderLowLevelDesign.coursetocfetcher import CourseTOCFetcher
from KursoDownloaderLowLevelDesign.coursefetcher import CourseChapterFetcher
import os
cs = CourseSearch()
cs.busco('system design')
course_result = cs.get('system design')
cf = CourseTOCFetcher()
cc = CourseChapterFetcher()
coursesToc = {}
coursesMainDir = "..//coursesChapterJson"
for course_name in os.listdir(coursesMainDir):
    tempTOC =  cf.get_kurso_toc(course_name)
    # cc.downloadCourse(tempTOC)
    cc.downloadOfflineCourse(f"..//coursesChapterJson//{course_name}",tempTOC)


```


## Dependencies
pip install dotenv


### Open for PR. I will highly appericate any PR especially for the remaining components that haven't been implemented, and readme file.


