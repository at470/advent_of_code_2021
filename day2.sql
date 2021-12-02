.table;
drop table temp;
drop table input;

-- upload data into temp table
create table temp (input int);
.headers on
.mode csv temp;
.import input.csv temp;
-- upload data into input table, with autoincrement index
create table data (id integer primary key autoincrement, input int);
insert into data(input) select * from temp;

/* didn't use this
-- add columns for horizontal (x) and vertical (y) positions
ALTER TABLE data ADD x REAL DEFAULT 0;
ALTER TABLE data ADD y REAL DEFAULT 0;
*/
-- verify table
select * from data limit 10;


-- part 1
select *, total_depth*total_horizontal_position 
FROM (
	select sum(horizonal_position) total_horizontal_position, sum(depth_position) total_depth
	FROM (
			select id, input
			, (x_direction_vector*scalar_value) horizonal_position
			, (y_direction_vector*scalar_value) depth_position
			from (
					select *
					, case when input LIKE '%forward%' THEN 1 ELSE 0 END x_direction_vector
					, case when input LIKE '%down%' THEN 1 when input LIKE '%up%' THEN -1 ELSE 0 END y_direction_vector
					, substr(input, instr(input,' ')-LENGTH(input)) scalar_value
					from data
				)
	)
);
