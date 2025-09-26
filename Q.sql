create database collage;
create database if not exists collage;
drop database if exists school;


drop database collage;

create database collage;

use collage;

create table student(
id int primary key,
name varchar(50),
age int not null
);

insert into student value(1,"Subhadip Sinha",21);
insert into student value(2,"rohit",19);

select * from student; 

show databases;



create database XYZ;
use XYZ;
create table employee_info(
id int not null,
name varchar(40),
salary int not null
);

insert into employee_info(id,name,salary) value
(1,"Subhadip Sinha", 500000),
(2,"sourav",40000),
(3,"vishajit",30000),
(4,"Devesh",40000);

select * from employee_info;
