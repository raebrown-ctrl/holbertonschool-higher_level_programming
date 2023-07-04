-- lists all shows contained in hbtn_0d_tvshows
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command

SELECT S.title, G.genre_id
FROM tv_shows S
LEFT JOIN tv_show_genres G
ON S.id = G.show_id
WHERE G.show_id IS NULL
ORDER BY S.title, G.genre_id ASC;
