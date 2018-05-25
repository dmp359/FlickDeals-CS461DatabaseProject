drop table Belongs_To;
drop table Ratings;
drop table Favorites;
drop table Deals;
drop table Category;
drop table Business;
drop table Customers;

create table Customers (
  customerId varchar(128) primary key,
  age integer,
  firstName varchar(128),
  lastName varchar(128),
  gender varchar(1),
  accountId integer not null unique, 
  phoneNum BIGINT not null,
  email varchar(128) not null,
  password varchar(128) not null
);

insert into Customers values ('C1', 18, 'John', 'Finkle', 'M', 6184, 1873498920, 'john.finkle@gmail.com', 'password123');
insert into Customers values ('C2', 25, 'Phil', 'Wrinkle', 'M', 1743, 5935290053, 'philextreme@comcast.net', '1F93jhfcS');
insert into Customers values ('C3', 38, 'Sarah', 'Lint', 'F', 9148, 5259482958, 'sarahsmiles@hotmail.com', 'cat43run92');
insert into Customers values ('C4', 27, 'Rob', 'Zambonie', 'M', 3215, 2672539982, 'RobbieBobbie234@hotmail.com', 'ihaveadog');
insert into Customers values ('C5', 50, 'Jill', 'Heart', 'F', 5262, 2153878738, 'iheartjill43@gmail.com', 'jillywillynilly');
insert into Customers values ('C6', 21, 'Will', 'Dwightson', 'M', 8532, 1234567895, 'williamnot43@gmail.com', '2Fj2i3lolp');
insert into Customers values ('C7', 29, 'Sam', 'Arnold', 'M', 1243, 9283726635, 'sam.arnold@hotmail.com', 'sam.arnolds');
insert into Customers values ('C8', 27, 'Artem', 'Addison', 'M', 2837, 2736748837, 'artem.artems@hotmail.com', 'artemruns');
insert into Customers values ('C9', 39, 'Olivia', 'Johnson', 'F', 0283, 2847563984, 'olivia.johnson@hotmail.com', 'oliviainny');
insert into Customers values ('C10', 40, 'David', 'Johns', 'M', 3647, 8293846354, 'johns.david@hotmail.com', 'davidinphilly');

create table Category (
  categoryId varchar(128) primary key,
  categoryName varchar(128) not null
);

insert into Category values ('Cat1', 'Food');
insert into Category values ('Cat2', 'Electronics');
insert into Category values ('Cat3', 'Shoe');
insert into Category values ('Cat4', 'Furniture');
insert into Category values ('Cat5', 'Sports');
insert into Category values ('Cat6', 'Boats');
insert into Category values ('Cat7', 'Cars');
insert into Category values ('Cat8', 'Cloths');
insert into Category values ('Cat9', 'Office Supplies');
insert into Category values ('Cat10', 'Travel');

create table Business (
  businessId varchar(128) primary key,
  name varchar(128) not null,
  imageURL varchar(128),
  homePageURL varchar(128),
  phoneNum BIGINT unique,
  reputationId varchar(128) not null unique,
  numVisited Integer,
  numFavouritedDeals Integer
);

insert into Business values ('b1', 'Pizza Hut', 'https://bit.ly/2IbLOCR', 'https://pizzahut.com', 18005555555, 'R1', '100', '30');
insert into Business values ('b2', 'Apple', 'https://apple.co/2Ilxbc8', 'https://apple.com', 18001231234, 'R2', '224', '40');
insert into Business values ('b3', 'Nike', 'http://bit.ly/2KYpEBP', 'https://www.nike.com', 18005244254, 'R3', '330', '50');
insert into Business values ('b4', 'Ikea', 'http://bit.ly/2jWp8rU', 'https://www.ikea.com', 1800545455, 'R4', '142', '29');
insert into Business values ('b5', 'Adidas', 'http://bit.ly/2jUJH8d', 'https://www.adidas.com', 18001325984, 'R5', '230', '11');
insert into Business values ('b6', 'Yamaha', 'http://bit.ly/2rEHFNK', 'https://www.yamaha.com', 18008765443, 'R6', '131', '32');
insert into Business values ('b7', 'BMW', 'http://bit.ly/2wEa1fN', 'https://www.bmw.com', 18009999999, 'R7', '113', '12');
insert into Business values ('b8', 'Zara', 'http://bit.ly/2IdyVZi', 'https://www.zara.com', 18007778888, 'R8', '92', '23');
insert into Business values ('b9', 'Staples', 'http://bit.ly/2KVljzs', 'https://www.staples.com', 18001234567, 'R9', '94', '18');
insert into Business values ('b10', 'Expedia', 'https://bit.ly/2rFKspU', 'https://www.expedia.com', 18009584382, 'R10', '432', '94');

create table Belongs_To (
  bid varchar(128),
  cid varchar(128),
  primary key (bid, cid),
  foreign key (bid) references Business(businessId),
  foreign key (cid) references Category(categoryId)
);

insert into Belongs_To values ('b1', 'Cat1');
insert into Belongs_To values ('b2', 'Cat2');
insert into Belongs_To values ('b3', 'Cat3');
insert into Belongs_To values ('b4', 'Cat4');
insert into Belongs_To values ('b5', 'Cat5');
insert into Belongs_To values ('b6', 'Cat6');
insert into Belongs_To values ('b7', 'Cat7');
insert into Belongs_To values ('b8', 'Cat8');
insert into Belongs_To values ('b9', 'Cat9');
insert into Belongs_To values ('b10', 'Cat10');

create table Deals (
  dealId varchar(128) unique,
  dateSubmitted Date not null,
  title varchar(128) not null,
  description varchar(128),
  avgRating float,
  imageURL varchar(128),
  durId varchar(128) unique,
  startDate Date not null,
  endDate Date not null,
  bid varchar(128),
  primary key (dealId, bid),
  foreign key (bid) references Business(businessId) on delete cascade
);

insert into Deals values ('DealId1', '01-19-18', 'Pizza Hut : Discount', '$10 off your first order at PizzaHut.com!', 2.5, 
                          'https://www.bleepstatic.com/content/posts/2017/10/15/PizzaHut.jpg', 'DUR1',
                          '01-20-18', '01-25-18', 'b1');
insert into Deals values ('DealId2', '01-19-18', 'Buy 3 iphones get 1 free', 'Buy 3 iPhones get 1 free!', 1.0, 
                          'https://vz.to/2wEXqJq', 'DUR2',
                          '01-26-18', '01-28-18', 'b2');
insert into Deals values ('DealId3', '01-19-18', 'Discount on golf kit', '$100 off your first order of nike Golf kit', 1.5, 
                          'http://bit.ly/2IBnV7s', 'DUR3',
                          '01-29-18', '02-10-18', 'b3');
insert into Deals values ('DealId4', '01-19-18', '$60 off', '40% off when you do more than $500 dollars worth of shopping', 4.0, 
                          'http://bit.ly/2jSaHVC', 'DUR4',
                          '02-11-18', '02-18-18', 'b4');
insert into Deals values ('DealId5', '01-19-18', 'Free Sneakers', 'Only valid in limited stores', 4.0, 
                          'http://bit.ly/2IwuLer', 'DUR5',
                          '02-19-18', '02-24-18', 'b5');
insert into Deals values ('DealId6', '01-19-18', 'Discount on boats', '$1000 off your first SMX32xv boat', 3.0, 
                          'http://bit.ly/2IavX7E', 'DUR6',
                          '02-24-18', '02-28-18', 'b6');
insert into Deals values ('DealId7', '01-19-18', 'Free Insurance', '$850 worth of free insurance ', 5.0, 
                          'http://bit.ly/2rDYg4d', 'DUR7',
                          '02-24-18', '02-28-18', 'b7');
insert into Deals values ('DealId8', '01-19-18', 'Buy 1 get 1 50% off', 'Offer valid on limited items', NULL, 
                          'http://bit.ly/2KWPgz6', 'DUR8',
                          '02-24-18', '02-28-18', 'b8');
insert into Deals values ('DealId9', '01-19-18', '40% off trip to Paris', 'Offer valid during month of January and February', NULL, 
                          'http://bit.ly/2IhQzH9', 'DUR9',
                          '01-01-18', '02-28-18', 'b10');
insert into Deals values ('DealId10', '01-19-18', 'Laser Printer', 'Laser Printer just for $90', NULL, 
                          'http://bit.ly/2jSfWVi', 'DUR10',
                          '01-01-18', '02-28-18', 'b9');
insert into Deals values ('DealId11', '01-19-18', 'Special Deals', '3 Medium Pizza for $20', 3.5, 
                          'https://read.bi/2KXUlHv', 'DUR11',
                          '01-20-18', '01-25-18', 'b1');
insert into Deals values ('DealId12', '01-19-18', 'Free Cookies', 'Get free cookies on order of $30 or more', NULL, 
                          'http://bit.ly/2GaOCdV', 'DUR12',
                          '01-20-18', '01-25-18', 'b1');
insert into Deals values ('DealId13', '01-19-18', 'Back to school', 'School supplies starting at $0.30. Minimum 20 dollar purchase required', NULL, 
                          'http://bit.ly/2KjKPx9', 'DUR13',
                          '01-01-18', '02-28-18', 'b9');
insert into Deals values ('DealId14', '01-19-18', 'Apple Watch', 'Apple Watch for $100', NULL, 
                          'http://bit.ly/2KY5ckL', 'DUR14',
                          '01-01-18', '02-28-18', 'b2');
insert into Deals values ('DealId15', '01-19-18', 'Air Jordan', 'Air Jordan for $150', NULL, 
                          'http://bit.ly/2IzTXjZ', 'DUR15',
                          '01-01-18', '02-28-18', 'b3');
insert into Deals values ('DealId16', '01-19-18', 'Round trip to Uk for $200', 'Offer valid during month of January and February', 3.0, 
                          'http://bit.ly/2wETmsw', 'DUR16',
                          '01-01-18', '02-28-18', 'b10');
insert into Deals values ('DealId17', '01-19-18', 'Round trip to India $250', 'Offer valid during month of January and February', NULL, 
                          'http://bit.ly/2IhLVgA', 'DUR17',
                          '01-01-18', '02-28-18', 'b10');
insert into Deals values ('DealId18', '01-19-18', '$15 off', 'Minimum $100 purchase required', 3.0, 
                          'http://bit.ly/2KYwzLj', 'DUR18',
                          '02-24-18', '02-28-18', 'b8');
insert into Deals values ('DealId19', '01-19-18', 'Discount on shoes', 'Offer valid on limited stores. Till stock lasts', NULL, 
                          'http://bit.ly/2IaBVFA', 'DUR19',
                          '02-24-18', '02-28-18', 'b8');
insert into Deals values ('DealId20', '01-19-18', '20% off on BMWX3', NULL, NULL, 
                          'http://bit.ly/2KkE7XP', 'DUR20',
                          '02-24-18', '02-28-18', 'b7');

create table Favorites(
  cid varchar(128),
  did varchar(128),
  primary key (cid, did),
  foreign key (cid) references Customers(customerId),
  foreign key (did) references Deals(dealId)
);


insert into Favorites values ('C2', 'DealId1');
insert into Favorites values ('C3', 'DealId7');
insert into Favorites values ('C4', 'DealId7');
insert into Favorites values ('C5', 'DealId4');
insert into Favorites values ('C5', 'DealId3');
insert into Favorites values ('C3', 'DealId11');
insert into Favorites values ('C8', 'DealId7');
insert into Favorites values ('C9', 'DealId4');
insert into Favorites values ('C9', 'DealId2');
insert into Favorites values ('C10', 'DealId10');

create table Ratings(
  cid varchar(128),
  did varchar(128),
  ratingId varchar(128) primary key,
  value integer,
  unique (cid, did),
  foreign key (cid) references Customers(customerId),
  foreign key (did) references Deals(dealId)
);

insert into Ratings values ('C2', 'DealId1', 'R1', 4);
insert into Ratings values ('C2', 'DealId11', 'R2', 2);
insert into Ratings values ('C3', 'DealId3', 'R3', 2);
insert into Ratings values ('C4', 'DealId1', 'R4', 1);
insert into Ratings values ('C5', 'DealId4', 'R5', 4);
insert into Ratings values ('C6', 'DealId5', 'R6', 4);
insert into Ratings values ('C2', 'DealId7', 'R7', 5);
insert into Ratings values ('C6', 'DealId2', 'R8', 1);
insert into Ratings values ('C7', 'DealId6', 'R9', 3);
insert into Ratings values ('C8', 'DealId3', 'R10', 1);
