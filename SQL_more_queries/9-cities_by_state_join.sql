-- Lists all cities in hbtn_0d_usa displaying cities.id - cities.name - states.name
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
