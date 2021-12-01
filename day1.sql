-- https://adventofcode.com/2021/day/1

drop table temp;
drop table data;

-- upload data into temp table
create table temp (input int);
.mode csv temp;
.import input.csv temp;
-- upload data into input table, with autoincrement index
create table data (id integer primary key autoincrement, input int);
insert into data(input) select * from temp;

-- verify base table
select * from data limit 10;

-- part 1
-- 1696
SELECT SUM(count_positive) 
FROM (
		SELECT id
		,input-lag1 delta
		, case when input-lag1 > 0 then 1 else 0 end count_positive
		FROM (
			SELECT id
			, input
			, LAG(input, 1) over (order by id) lag1
			FROM data
		)
);


-- part 2
-- 1796
SELECT SUM(count_positive) 
FROM (
		SELECT id
		,input-lag4 delta
		, case when input-lag4 > 0 then 1 else 0 end count_positive
		FROM (
			SELECT id
			, input
			, LAG(input, 4) over (order by id) lag4
			FROM data
		)
);
