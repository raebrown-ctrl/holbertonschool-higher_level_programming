-- that lists all shows

SELECT S.title, G.genre_id
FROM tv_shows S
LEFT JOIN tv_show_genres G
ON S.id = G.show_id
ORDER BY S.title, G.genre_id ASC;
