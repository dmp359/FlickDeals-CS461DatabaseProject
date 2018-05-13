drop table Belongs_To;
drop table Ratings;
drop table Favorites;
drop table Deals;
drop table Users;
drop table Category;
drop table Business;

create table Users (
  customerId integer primary key,
	age integer,
	firstName varchar(128),
	lastName varchar(128),
	gender varchar(1),
	accountId integer not null unique, 
	phoneNum BIGINT not null,
	email varchar(128) not null,
	password varchar(128) not null
);
insert into Users values (6135, 18, 'John', 'Finkle', 'M', 6184, 1873498920, 'john.finkle@gmail.com', 'password123');
insert into Users values (3155, 25, 'Phil', 'Wrinkle', 'M', 1743, 5935290053, 'philextreme@comcast.net', '1F93jhfcS');
insert into Users values (2115, 38, 'Sarah', 'Lint', 'F', 9148, 5259482958, 'sarahsmiles@hotmail.com', 'cat43run92');
insert into Users values (3827, 27, 'Rob', 'Zambonie', 'M', 3215, 2672539982, 'RobbieBobbie234@hotmail.com', 'ihaveadog');
insert into Users values (8748, 50, 'Jill', 'Heart', 'F', 5262, 2153878738, 'iheartjill43@gmail.com', 'jillywillynilly');
insert into Users values (8973, 21, 'Will', 'Dwightson', 'M', 8532, 1234567895, 'williamnot43@gmail.com', '2Fj2i3lolp');

create table Category (
  categoryId varchar(128) primary key,
  categoryName varchar(128) not null
);
insert into Category values ('Cat1', 'Food');

create table Business (
  businessId varchar(128) primary key,
  name varchar(128) not null,
  imageURL varchar(128),
  homePageURL varchar(128),
  phoneNum BIGINT unique
);

create table Belongs_To (
  bid varchar(128),
  cid varchar(128),
  primary key (bid, cid),
  foreign key (bid) references Business(businessId),
  foreign key (cid) references Category(categoryId)
);

insert into Business values ('b1', 'Pizza Hut', 'http://www1.cv-ag.com/wp-content/uploads/2016/01/business-people-working-together-istock_000017346252medium.jpg', 'https://business.com', 7033333333);
insert into Business values ('b2', 'Apple', 'https://www.apple.com/ac/structured-data/images/knowledge_graph_logo.png?201606271147', 'https://www.apple.com/mac/home/images/social/macbook_mac_og.png?201804191038', 7022222222);
insert into Business values ('b3', 'Nike', 'https://cdn.thesolesupplier.co.uk/2017/08/NIKE-Logo.jpg', 'https://c.static-nike.com/a/images/t_PDP_1280_v1/f_auto/lmpq4yxn0aqre66opd5d/air-presto-womens-shoe-89Tqz1nG.jpg', 70111111111);
insert into Business values ('b4', 'Ikea', 'http://cache.magicmaman.com/data/photo/w515_c18/4m/ikea.jpg', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSH56xX80atcDnT7lZ757lDFCpzvMhtmzs_GvYgG-PJkgxzkYWv', 70000000000);
insert into Belongs_To values ('b1', 'Cat1');

create table Deals (
  dealId varchar(128) unique,
  dateSubmitted Date not null,
  title varchar(128) not null,
  description varchar(128),
  avgRating float,
  imageURL varchar(128),
  startDate Date not null,
  endDate Date not null,
  bid varchar(128),
  primary key (dealId, bid),
  foreign key (bid) references Business(businessId) on delete cascade
);
insert into Deals values ('DealId1', '01-19-18', 'Pizza Hut Deals1', '$10 off your first order at PizzaHut.com!', 4.5, 
                          'https://www.bleepstatic.com/content/posts/2017/10/15/PizzaHut.jpg',
                          '01-20-18', '01-25-18', 'b1');
insert into Deals values ('DealId2', '01-19-18', 'Pizza Hut Deals2', '$6 off your first order at PizzaHut.com!', 4.5, 
                          'https://www.bleepstatic.com/content/posts/2017/10/15/PizzaHut.jpg',
                          '01-26-18', '01-28-18', 'b1');
insert into Deals values ('DealId3', '01-19-18', 'Pizza Hut Deals3', '$12 off your first order at PizzaHut.com!', 4.5, 
                          'https://www.bleepstatic.com/content/posts/2017/10/15/PizzaHut.jpg',
                          '01-29-18', '02-10-18', 'b1');
insert into Deals values ('DealId4', '01-19-18', 'Pizza Hut Deals4', '$4 off your first order at PizzaHut.com!', 4.5, 
                          'https://www.bleepstatic.com/content/posts/2017/10/15/PizzaHut.jpg',
                          '02-11-18', '02-18-18', 'b1');
insert into Deals values ('DealId5', '01-19-18', 'Pizza Hut Deals5', '$15 off your first order at PizzaHut.com!', 4.5, 
                          'https://www.bleepstatic.com/content/posts/2017/10/15/PizzaHut.jpg',
                          '02-19-18', '02-24-18', 'b1');
insert into Deals values ('DealId6', '01-19-18', 'Pizza Hut Deals6', '$5 off your first order at PizzaHut.com!', 4.5, 
                          'https://www.bleepstatic.com/content/posts/2017/10/15/PizzaHut.jpg',
                          '02-24-18', '02-28-18', 'b1');

create table Ratings(
  cid integer,
  did varchar(128),
  value integer,
  primary key (cid, did),
  foreign key (cid) references Users(customerId),
  foreign key (did) references Deals(dealId)
);
insert into Ratings values (6135, 'DealId1', 4);
insert into Ratings values (3155, 'DealId1', 1);

create table Favorites(
  cid integer,
  did varchar(128),
  primary key (cid, did),
  foreign key (cid) references Users(customerId),
  foreign key (did) references Deals(dealId)
);
insert into Favorites values (6135, 'DealId1');