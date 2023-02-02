#remove_duplicates_from_tables
create table books as
(select distinct name, author_id, rating_score, rating_count, reviews_count, genre
from book)

create table authors as
(select distinct name, books_count, followers_count, avg_rating,ratings_count, reviews_count
from author)


delete from books 
where author_id is null

delete from books
where name ='null'


remove_books_with_same_names_over_different_genre
with duplicates as
(select id, name, author_id, rating_score, rating_count, reviews_count, genre,
	row_number() over(partition by name) as apparation_count
from book)

select *
into books
from duplicates 
where apparation_count = 1

alter table books
drop column apparation_count


remove_authors_with_same_names_over_different_genre
with duplicates as
(select id, name, books_count, followers_count, avg_rating, ratings_count, reviews_count, apparation_count
	row_number() over(partition by name) as apparation_count
from author)

select *
into authors
from duplicates 
where apparation_count = 1

alter table authors
drop column apparation_count



#delete_unexpected_names
delete from books
where id in (select books.id from books
				join authors on authors.id = books.author_id
				where authors.name like '%BOOK%')

delete from authors
where name like '%BOOK%'


delete from authors 
where left(name,1) in ('1','2','3','4','5','6','7','8','9','0')