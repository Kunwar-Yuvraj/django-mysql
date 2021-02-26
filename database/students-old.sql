create database School_Management_System_by_KunwarYuvraj;

USE School_Management_System_by_KunwarYuvraj;

create table student
        (
            UID int auto_increment, 
            Roll_No int(15), 
            Name varchar(300), 
            Class varchar(100), 
            Address varchar(500),
            Gender varchar(100),
            Phone_No varchar(255), 
            Email varchar(300),
            Primary Key (UID)
        );


alter table student auto_increment = 1000;

insert into student(Roll_no, Name, Class, Address, Gender, Phone_No, Email) values(0, "Zero", "12th F", "Raj Nagar II, Palam", "Female", "+91 1234567891", "zero@mail.cm");

insert into student(Roll_no, Name, Class, Address, Gender, Phone_No, Email) values(1, "One", "5th C", "123, Mahipalpur", "Male","+11 7878912496", "one@mail.cm");

insert into student(Roll_no, Name, Class, Address, Gender, Phone_No, Email) values(2, "Two", "3rd F", "Street No. 8, Raj Nagar", "Female","+2 4211234567", "two@mail.cm");

insert into student(Roll_no, Name, Class, Address, Gender, Phone_No, Email) values(3, "Three", "9th B", "9th Street, Palam", "Male","+3 87450987", "three@mail.cm");

insert into student(Roll_no, Name, Class, Address, Gender, Phone_No, Email) values(4, "Four", "2nd D", "F Block, Rajiv Chawk", "Female","+4 1212121212", "four@mail.cm");

insert into student(Roll_no, Name, Class, Address, Gender, Phone_No, Email) values(5, "Five", "10th E", "93, Dwarka Opp. NSUT", "Male","+5 8723412706", "five@mail.cm");

insert into student(Roll_no, Name, Class, Address, Gender, Phone_No, Email) values(6, "Six", "7th F", "Pillar No. 811, Dwarka Metro", "Female","+6 8798124508", "sie@mail.cm");

 