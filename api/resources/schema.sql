DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS exercise;
DROP TABLE IF EXISTS log;

CREATE TABLE user (
    id integer primary key,
    username char(20) unique not null,
    hash char(256) not null
);

CREATE TABLE exercise (
    id integer primary key,
    name char(50) unique not null,
    time_flag boolean default false not null
);

CREATE TABLE log (
    id integer primary key,
    id_user integer references user(id) not null on update cascade on delete no action,
    date timestamp not null,
    exercise integer references exercise(id) not null on update no action on update no action,
    value integer not null
);

