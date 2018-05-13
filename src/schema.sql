drop table Users;
drop table Category;
drop table Belongs_To;
drop table Business;
drop table Deals;

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
insert into Category values ('C1', 'Food');

create table Deals (
  dealId varchar(128) primary key,
  dateSubmitted Date not null,
  title varchar(128) not null,
  description varchar(128),
  avgRating float,
  imageURL varchar(128),
  startDate Date not null,
  endDate Date not null
);
insert into Deals values ('TempDealId1', '01-19-18', 'Pizza Hut Deals', '$10 off your first order at PizzaHut.com!', 4.5, 
                   'https://www.bleepstatic.com/content/posts/2017/10/15/PizzaHut.jpg',
                   '01-20-18', '01-25-18');

create table Ratings(
  cid integer,
  did varchar(128),
  value integer,
  primary key (cid, did),
  foreign key (cid) references Users(customerId),
  foreign key (did) references Deals(dealId)
);
insert into Ratings values (6135, 'TempDealId1', 4);
insert into Ratings values (3155, 'TempDealId1', 1);

create table Favorites(
  cid integer,
  did varchar(128),
  primary key (cid, did),
  foreign key (cid) references Users(customerId),
  foreign key (did) references Deals(dealId)
);
insert into Ratings values (6135, 'TempDealId1');
insert into Favorites values (3155, 'TempDealId1');

create table Business (
  businessId varchar(128) primary key,
  name varchar(128) not null,
  imageURL varchar(128),
  homePageURL varchar(128),
  phoneNum BIGINT unique,
  did varchar(128),
  foreign key (did) references Deals(dealId) on delete cascade
);

create table Belongs_To (
  bid varchar(128),
  cid varchar(128),
  primary key (bid, cid),
  foreign key (bid) references Business(businessId),
  foreign key (cid) references Category(categoryId)
);

insert into Business values ('1', 'BNAME', 'http://www1.cv-ag.com/wp-content/uploads/2016/01/business-people-working-together-istock_000017346252medium.jpg', 'https://business.com', 7033333333, 'TempDealId1');
insert into Business values ('2', 'Apple', 'https://www.apple.com/ac/structured-data/images/knowledge_graph_logo.png?201606271147', 'https://www.apple.com/mac/home/images/social/macbook_mac_og.png?201804191038', 7022222222, 'TempDealId1');
insert into Business values ('3', 'Nike', 'https://cdn.thesolesupplier.co.uk/2017/08/NIKE-Logo.jpg', 'https://c.static-nike.com/a/images/t_PDP_1280_v1/f_auto/lmpq4yxn0aqre66opd5d/air-presto-womens-shoe-89Tqz1nG.jpg', 70111111111, 'TempDealId1');
insert into Business values ('4', 'Ikea', 'http://cache.magicmaman.com/data/photo/w515_c18/4m/ikea.jpg', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSH56xX80atcDnT7lZ757lDFCpzvMhtmzs_GvYgG-PJkgxzkYWv', 70000000000, 'TempDealId1');
insert into Belongs_To values ('1', 'C1');

