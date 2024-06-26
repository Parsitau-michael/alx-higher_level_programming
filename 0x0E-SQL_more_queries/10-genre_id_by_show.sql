-- Imported the database dump from hbtn_0d_tvshows
-- A script that lists all shows contained in hbtn_0d_tvshows
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows LEFT OUTER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id WHERE tv_show_genres.show_id is NOT NULL ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC; 
