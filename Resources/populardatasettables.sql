CREATE TABLE popularvotes (
id INT PRIMARY KEY,
state TEXT,
dem_votes VARCHAR(60),
rep_votes VARCHAR(60),
dem_percent TEXT,
rep_percent TEXT,
stateid TEXT
);

select * from popularvotes;