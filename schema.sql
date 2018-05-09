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