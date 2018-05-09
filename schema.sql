drop table Users;

create table Users (
  customerId integer primary key,
	age integer,
	firstName varchar(128),
	lastName varchar(128),
	gender varchar(1),
	accountId integer not null unique, 
	phoneNum varchar(10) not null,
	email varchar(128) not null,
	password varchar(128) not null
);

insert into Users values (6135, 18, 'John', 'Finkle', 'M', 6184, '1873498920', 'john.finkle@gmail.com', 'password123');
insert into Users values (3155, 25, 'Phil', 'Wrinkle', 'M', 1743, '5935290053', 'philextreme@comcast.net', '1F93jhfcS');
insert into Users values (2115, 38, 'Sarah', 'Lint', 'F', 9148, '5259482958', 'sarahsmiles@hotmail.com', 'cat43run92');
insert into Users values (3827, 27, 'Rob', 'Zambonie', 'M', 3215, '2672539982', 'RobbieBobbie234@hotmail.com', 'ihaveadog');
insert into Users values (8748, 50, 'Jill', 'Heart', 'F', 5262, '2153878738', 'iheartjill43@gmail.com', 'jillywillynilly');
insert into Users values (8973, 21, 'Will', 'Dwightson', 'M', 8532, '1234567895', 'williamnot43@gmail.com', '2Fj2i3lolp');