.table;
drop table temp;
drop table input;

-- upload data into temp table
create table temp (input int);
.headers on
.mode csv temp
.import input.csv temp;
-- upload data into input table, with autoincrement index
create table data (id integer primary key autoincrement, input int);
insert into data(input) select * from temp;
.mode column

/* didn't need
-- add columns for horizontal (x) and vertical (y) positions
ALTER TABLE data ADD x REAL DEFAULT 0;
ALTER TABLE data ADD y REAL DEFAULT 0;
*/

-- verify table
select * from data limit 10;

-- verify table
select * from data_bits limit 10;




-- part 1
-- check max length of each string
SELECT MAX_LENGTH 
FROM (
	SELECT length(input) MAX_LENGTH 
	from data
)
GROUP BY 1;

-- create table of bits in columns
-- add 0 where column is ''
create table data_bits (id int, input int, bit_1 int, bit_2 int, bit_3 int, bit_4 int, bit_5 int, bit_6 int, bit_7 int, bit_8 int, bit_9 int, bit_10 int, bit_11 int, bit_12 int);
insert into data_bits select * , CASE WHEN substr(input, -12,1) IS '' THEN 0 ELSE substr(input, -12,1) END as bit_12
, CASE WHEN substr(input, -11,1) IS '' THEN 0 ELSE substr(input, -11,1) END as bit_11
, CASE WHEN substr(input, -10,1) IS '' THEN 0 ELSE substr(input, -10,1) END as bit_10
, CASE WHEN substr(input, -9,1) IS '' THEN 0 ELSE substr(input, -9,1) END as bit_9
, CASE WHEN substr(input, -8,1) IS '' THEN 0 ELSE substr(input, -8,1) END as bit_8
, CASE WHEN substr(input, -7,1) IS '' THEN 0 ELSE substr(input, -7,1) END as bit_7
, CASE WHEN substr(input, -6,1) IS '' THEN 0 ELSE substr(input, -6,1) END as bit_6
, CASE WHEN substr(input, -5,1) IS '' THEN 0 ELSE substr(input, -5,1) END as bit_5
, CASE WHEN substr(input, -4,1) IS '' THEN 0 ELSE substr(input, -4,1) END as bit_4
, CASE WHEN substr(input, -3,1) IS '' THEN 0 ELSE substr(input, -3,1) END as bit_3
, CASE WHEN substr(input, -2,1) IS '' THEN 0 ELSE substr(input, -2,1) END as bit_2
, CASE WHEN substr(input, -1,1) IS '' THEN 0 ELSE substr(input, -1,1) END as bit_1
from data;

-- binary
SELECT case when bit_1_one > zero_bit_1 then 1
when bit_1_one < zero_bit_1 then 0 else 'error' end bit_1
,case when bit_2_one > zero_bit_2 then 1
when bit_2_one < zero_bit_2 then 0 else 'error' end bit_2
,case when bit_3_one > zero_bit_3 then 1
when bit_3_one < zero_bit_3 then 0 else 'error' end  bit_3
,case when bit_4_one > zero_bit_4 then 1
when bit_4_one < zero_bit_4 then 0 else 'error' end bit_4
,case when bit_5_one > zero_bit_5 then 1
when bit_5_one < zero_bit_5 then 0 else 'error' end bit_5
,case when bit_6_one > zero_bit_6 then 1
when bit_6_one < zero_bit_6 then 0 else 'error' end bit_6
,case when bit_7_one > zero_bit_7 then 1
when bit_7_one < zero_bit_7 then 0 else 'error' end bit_7
,case when bit_8_one > zero_bit_8 then 1 
when bit_8_one < zero_bit_8 then 0 else 'error' end bit_8
,case when bit_9_one > zero_bit_9 then 1 
when bit_12_one < zero_bit_12 then 0 else 'error' end bit_9
,case when bit_10_one > zero_bit_10 then 1
when bit_10_one < zero_bit_10 then 0 else 'error' end bit_10
, case when bit_11_one > zero_bit_11 then 1 
when bit_11_one < zero_bit_11 then 0 else 'error' end bit_11
,case when bit_12_one > zero_bit_12 then 1 
when bit_12_one < zero_bit_12 then 0 else 'error' end bit_12
FROM (
	SELECT *
	, total_rows - bit_12_one zero_bit_12
	, total_rows - bit_11_one zero_bit_11
	, total_rows - bit_10_one zero_bit_10
	, total_rows - bit_9_one zero_bit_9
	, total_rows - bit_8_one zero_bit_8
	, total_rows - bit_7_one zero_bit_7
	, total_rows - bit_6_one zero_bit_6
	, total_rows - bit_5_one zero_bit_5
	, total_rows - bit_4_one zero_bit_4
	, total_rows - bit_3_one zero_bit_3
	, total_rows - bit_2_one zero_bit_2
	, total_rows - bit_1_one zero_bit_1
	FROM (
		SELECT COUNT(*) TOTAL_ROWS
		, SUM(bit_12) bit_12_one
		, SUM(bit_11) bit_11_one
		, SUM(bit_10) bit_10_one
		, SUM(bit_9) bit_9_one
		, SUM(bit_8) bit_8_one
		, SUM(bit_7) bit_7_one
		, SUM(bit_6) bit_6_one
		, SUM(bit_5) bit_5_one
		, SUM(bit_4) bit_4_one
		, SUM(bit_3) bit_3_one
		, SUM(bit_2) bit_2_one
		, SUM(bit_1) bit_1_one
		from data_bits
		)
	)
;

/*

bit_1  bit_2  bit_3  bit_4  bit_5  bit_6  bit_7  bit_8  bit_9  bit_10  bit_11  bit_12
-----  -----  -----  -----  -----  -----  -----  -----  -----  ------  ------  ------
1      1      1      1      0      0      1      1      1      1       1       1     

0      0      0      0      1      1      0      0      0      0       0       0     


111100111111 -- 3903
000011000000 -- 192
*/



