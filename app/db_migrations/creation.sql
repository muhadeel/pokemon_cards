-- pokemon: table
create table pokemon
(
    id int(11) auto_increment primary key,
    name varchar(64) not null,
    created_at datetime default now() not null,
    updated_at datetime default now() on update now() not null
);
ALTER TABLE pokemon AUTO_INCREMENT = 1;