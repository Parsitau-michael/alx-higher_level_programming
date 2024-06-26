-- A script that lists all genres and displays the number of shows linked in each
SELECT tv_genres.name AS "genre", COUNT(tv_show_genres.genre_id) AS "number_of_shows"
FROM tv_genres INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY COUNT(tv_show_genres.genre_id) DESC;
