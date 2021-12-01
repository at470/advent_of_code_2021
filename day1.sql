-- create table using sqlite3
-- original input data modified to add index column
create table if not exist data (id int, input int);
.mode csv;
.import input_id.csv data;

-- verify base table
select * from data limit 10;

-- part 1
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
