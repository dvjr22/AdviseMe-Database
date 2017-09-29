/* Pull curriculum for major */
select prefix, co_num, semester 
from curriculum
where major = 'ce'
order by semester;

/* Get major of a student */
select sid, major
from degree
where sid = 'z52958243';

/* List of students and their majors */
select s.sid, first, last, status, major
from students as s
join (degree as d)
on (s.sid = d.sid);

/* Pull curriculum for major with titles */
select a.prefix, a.co_num, title, major, semester, min_grade
from classes as a
join (curriculum as b)
on (a.prefix = b.prefix and a.co_num = b.co_num)
where major = 'ce'
order by semester;


select a.prefix, a.co_num, title
from classes as a
join (curriculum as b)
on (a.prefix = b.prefix and a.co_num = b.co_num)
where major = 'cs'
order by semester, prefix;
