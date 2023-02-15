-- A script that displays the average temprature by city ordered by
-- temprature desc.

SELECT `city`, AVG(`value`) AS average FROM `temperatures` GROUP BY `city`
ORDER BY average DESC;

