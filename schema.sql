CREATE TABLE member(
	member_id	SERIAL 		PRIMARY KEY	NOT NULL,
	firstName	VARCHAR(40)	NOT NULL,
	lastName	VARCHAR(40) NOT NULL,
	school		VARCHAR(40)	NOT NULL,
	email		VARCHAR(70) NOT NULL,
	address		VARCHAR(70) NOT NULL,
	city		VARCHAR(30) NOT NULL,
	province	VARCHAR(30) NOT NULL,
	postal_code	VARCHAR(6) 	NOT NULL,
	phone		VARCHAR(10)	NOT NULL,
	subject		VARCHAR(30)	NOT NULL,
	facebook	VARCHAR(99) NOT NULL,
	twitter		VARCHAR(99)	NOT NULL	
);

CREATE TABLE book(
	book_id		SERIAL		PRIMARY KEY	NOT NULL,
	title		VARCHAR(90)	NOT NULL,
	author		VARCHAR(90)	NOT NULL,
	publisher	VARCHAR(90)	NOT NULL,
	year		INTEGER 	NOT	NULL,
	subject		VARCHAR(90)	NOT NULL
);

CREATE TABLE school(
	school_id	SERIAL 		PRIMARY KEY NOT NULL,
	name		VARCHAR(99)	NOT NULL,
	address	VARCHAR(99) NOT NULL,
	city		VARCHAR(30)	NOT NULL,
	province	VARCHAR(30)	NOT NULL,
	postal_code	VARCHAR(6 )	NOT NULL	
);

CREATE TABLE auction(
	auction_id	SERIAL 	PRIMARY KEY NOT NULL,
	book_id		INTEGER UNIQUE 	NOT NULL,
	member_id	INTEGER UNIQUE	NOT NULL,
	min_price	FLOAT	NOT NULL,
	bid_id 		INTEGER UNIQUE 	NOT NULL
);

CREATE TABLE bid(
	bid_id		INTEGER PRIMARY KEY	NOT NULL,
	bdPrice 	float	NOT NULL,
	member_id	INTEGER UNIQUE	NOT NULL
);



