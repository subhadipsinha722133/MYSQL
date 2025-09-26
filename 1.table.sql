create database collage;

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
