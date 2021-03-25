-- create DATABASE, comment out if created
create database pokemon_cards;

-- pokemon: demo table (will be removed)
create table pokemon
(
    id int(11) auto_increment primary key,
    name varchar(64) not null,
    created_at datetime default now() not null,
    updated_at datetime default now() on update now() not null
);

CREATE TABLE users (
    id int(11) AUTO_INCREMENT PRIMARY KEY,
    email varchar (127) NOT NULL UNIQUE,
    name varchar(63) NOT NULL,
    bio varchar(255),
    created_at DATETIME DEFAULT NOW() NOT NULL,
    updated_at DATETIME DEFAULT NOW() ON UPDATE NOW() NOT NULL
    );

CREATE TABLE cards (
    id varchar(255) NOT NULL PRIMARY KEY,
    name varchar(127) NOT NULL,
    supertype ENUM ('Pokémon', 'Trainer', 'Energy') NOT NULL,
    subtype varchar(63),
    created_at DATETIME DEFAULT NOW() NOT NULL,
    updated_at DATETIME DEFAULT NOW() ON UPDATE NOW() NOT NULL
    );

CREATE TABLE decks (
    id int(11) AUTO_INCREMENT PRIMARY KEY,
    user_id int(10) NOT NULL,
    description varchar(255),
    created_at DATETIME DEFAULT NOW() NOT NULL,
    updated_at DATETIME DEFAULT NOW() ON UPDATE NOW() NOT NULL,
    constraint user_id_fk foreign key (user_id)
        references users (id)
        on delete cascade
    );

CREATE TABLE card_deck (
    card_id varchar(255) NOT NULL,
    deck_id int(11) NOT NULL,
    created_at DATETIME DEFAULT NOW() NOT NULL,
    updated_at DATETIME DEFAULT NOW() ON UPDATE NOW() NOT NULL,
    PRIMARY KEY (card_id, deck_id),
    constraint deck_card_id_fk foreign key (deck_id)
        references decks (id)
        on delete cascade,
    constraint card_deck_id_fk foreign key (card_id)
        references cards (id)
        on delete no action
    );

CREATE TABLE wishlists (
    user_id int(11) NOT NULL PRIMARY KEY,
    created_at DATETIME DEFAULT NOW() NOT NULL,
    updated_at DATETIME DEFAULT NOW() ON UPDATE NOW() NOT NULL,
    constraint wishlist_user_id_fk foreign key (user_id)
        references users (id)
        on delete cascade
    );

CREATE TABLE wishlist_cards (
    user_id int(11) NOT NULL,
    card_id varchar(255) NOT NULL,
    threshold float,
    created_at DATETIME DEFAULT NOW() NOT NULL,
    updated_at DATETIME DEFAULT NOW() ON UPDATE NOW() NOT NULL,
    PRIMARY KEY (user_id, card_id),
    constraint wishlist_card_user_id_fk foreign key (user_id)
        references wishlists (user_id)
        on delete cascade,
    constraint wishlist_card_id_fk foreign key (card_id)
        references cards (id)
        on delete no action
    );

CREATE TABLE trades (
    id int(11) AUTO_INCREMENT PRIMARY KEY,
    seller_id int(11) NOT NULL,
    purchaser_id int(11) NOT NULL,
    card_id varchar(255) NOT NULL,
    monetary_total float not null,
    created_at DATETIME DEFAULT NOW() NOT NULL,
    updated_at DATETIME DEFAULT NOW() ON UPDATE NOW() NOT NULL,
        constraint seller_id_fk foreign key (seller_id)
        references users (id)
        on delete no action,
    constraint purchaser_id_fk foreign key (purchaser_id)
        references users (id)
        on delete no action,
    constraint card_id_fk foreign key (card_id)
        references cards (id)
        on delete no action
    );
