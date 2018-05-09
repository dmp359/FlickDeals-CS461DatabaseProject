drop table Customers;
drop table Accounts;

create table Customers (
	customerId integer primary key,
	age integer,
	firstName varchar(128),
	lastName varchar(128),
	gender varchar(1),
	accountId integer unique not null,
	foreign key accountId references Accounts(accountId)
);

create table Accounts (
	accountId integer primary key,
	phoneNum integer not null,
	email varchar(128) not null,
	password varchar(128) not null,
	customerId integer unique not null,
	foreign key customerId references Customers(customerId) on delete cascade
);

insert into Customers values (6184, 18, John, Finkle, M, 613595567);
insert into Customers values (1743, 25, Phil, Wrinkle, M, 3155444588);
insert into Customers values (9148, 38, Sarah, Lint, F, 21158711);
insert into Customers values (3215, 27, Rob, Zambonie, M, 38275017);
insert into Customers values (5262, 50, Jill, Heart, F, 87483962);
insert into Customers values (8532, 21, Will, Dwightson, M, 89739173);


insert into Accounts values (613595567, 1895321832, john.finkle@gmail.com, password123, 6184);
insert into Accounts values (3155444588, 5935290053, philextreme@comcast.net, 1F93jhfcS, 1743);
insert into Accounts values (21158711, 8875314431, sarahsmiles@hotmail.com, cat43run92, 9148);
insert into Accounts values (38275017, 2672539982, RobbieBobbie234@hotmail.com, ihaveadog, 3215);
insert into Accounts values (87483962, 2155555555, iheartjill43@gmail.com, jillywillynilly, 5262);
insert into Accounts values (89739173, 88725808524, williamnot43@gmail.com, 2Fj2i3lolp, 8532);
