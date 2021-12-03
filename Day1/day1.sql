drop table temp;
drop table input;

-- upload data into temp table
create table temp (input int);
.headers on;
.mode column;
.mode csv temp;
.import input.csv temp;
-- upload data into input table, with autoincrement index
create table data (id integer primary key autoincrement, input int);
insert into data(input) select * from temp;



-- part 1
SELECT SUM(count_positive) FROM (SELECT id,input, lag1, input-lag1 delta, case when input-lag1 > 0 then 1 else 0 end count_positive FROM (SELECT id, input, LAG(input) over (order by id) lag1 FROM data))
--1696

SELECT SUM(count_positive) 
FROM (
		SELECT id
		,input-lag1 delta
		, case when lag1-input > 0 then 1 else 0 end count_positive
		FROM (
			SELECT id
			, input
			, LAG(input, 1) over (order by id) lag1
			FROM data
		)
);




SELECT id,lag1-input delta, case when lag1-input > 0 then 1 else 0 end count_positive FROM (SELECT id, input, LAG(input) over (order by id) lag1 FROM data)
GROUP BY 1,2,3
ORDER BY 1






-- part 2
SELECT id
,input-lag4 delta
, case when lag4-input > 0 then 1 else 0 end count_positive
FROM (
	SELECT id
	, input
	, LAG(input, 4) over (order by id) lag4
	FROM data_analyst_akikot.day1
)
GROUP BY 1,2,3
ORDER BY 1




SELECT SUM(count_positive) FROM (SELECT id,input, lag4, input-lag4 delta, case when input-lag4 > 0 then 1 else 0 end count_positive FROM (SELECT id, input, LAG(input,4) over (order by id) lag4 FROM data))
-- 1796