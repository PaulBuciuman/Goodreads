SELECT id, name, author_id, rating_score, rating_count, reviews_count, genre
	FROM public.books;
	
#count_books_by_genre
select count(*),genre from books
group by genre
order by count desc

#filer_by_author_name
select * from books
join authors on authors.id = books.author_id
where authors.name = 'Mark Manson'


#filter_by_rating_count(absolute_value)_order_by_rating_score_top10
select books.name as title, rating_score,author.name as author from books
join author on books.author_id=author.id
where rating_count > 5000
order by rating_score desc
limit 10



#filter_by_rating_count(relative_value)_order_by_rating_score_top10
select name, rating_score,genre from books
where genre = 'romance' and rating_count > 0.1 * (select avg(rating_count) from books
												 	where genre = 'romance')
order by rating_score desc
limit 10


#most_rated_book_by_genre
with max_rating_count as
(select genre, max(rating_count) from books
group by genre
order by max desc)

select max, books.genre, name from books
join  max_rating_count on max_rating_count.genre = books.genre
where books.rating_count = max
order by max desc,name asc


#order_authors_by_average_rating_filter_by_2_conditions
select distinct name, avg_rating,books_count from author
where books_count > 10 and ratings_count > 500
order by avg_rating desc


#order_author_by_book_count
with book_count as
(select author_id,count(*) from books
group by author_id)

select name,count,books_count from author
join book_count on book_count.author_id = author.id
order by count desc
limit 10


#top3authors(by_average_rating)_for_each_genre
with avg_rating_author_id_by_genre as
(select author_id, authors.name,  avg(rating_score) as average_rating, genre, 
       dense_rank() over(partition by genre order by avg(rating_score) desc) as ranking
from books
join authors on authors.id = author_id
group by genre,author_id,authors.name
having avg(rating_score) < 5)

select name,average_rating,genre from avg_rating_author_id_by_genre
where ranking <= 3


#top5books(by_rating_score)_for_each_genre_no_duplicate_score
with books_rating_by_genre as 
(select name, rating_score, genre,  
	row_number() over(partition by genre order by avg(rating_score) desc) as ranking
from books
where rating_count > 50
group by genre, name, rating_score
order by rating_score desc)

select name,rating_score,genre from books_rating_by_genre
where ranking <=5
order by genre asc, rating_score desc
