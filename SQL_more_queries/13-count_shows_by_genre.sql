-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>
-- First column must be called genre
-- Second column must be called number_of_shows
-- Don’t display a genre that doesn’t have any shows linked
-- Results must be sorted in descending order by the number of shows linked
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command

SELECT G.name AS genre, COUNT(TS.genre_id) AS number_of_shows
from tv_genres G
JOIN tv_show_genres TS
ON G.id = TS.genre_id
GROUP BY G.name
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
