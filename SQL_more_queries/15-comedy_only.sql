-- lists all Comedy shows in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command

SELECT S.title
FROM tv_shows AS S
	INNER JOIN tv_show_genres AS TS 
	ON S.id = TS.show_id

	INNER JOIN tv_genres AS G
	ON G.id = TS.genre_id
WHERE G.name = 'Comedy'
ORDER BY S.title;
