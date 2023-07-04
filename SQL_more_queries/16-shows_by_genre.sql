--  lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
-- If a show doesn’t have a genre, display NULL in the genre column
-- Each record should display: tv_shows.title - tv_genres.name
-- Results must be sorted in ascending order by the show title and genre name
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command

SELECT S.title, G.name
FROM tv_shows S
	LEFT JOIN tv_show_genres TS
	ON S.id = TS.show_id

	LEFT JOIN tv_genres G
	ON TS.genre_id = G.id
ORDER BY S.title, G.name;
