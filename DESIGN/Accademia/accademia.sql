create type strutturato as enum ('Ricercatore', 'Professore Associato', 'Professore Ordinario');

create type LavoroProgetto as enum ('Ricerca e Sviluppo', 'Dimostrazione', 'Management', 'Altro');

create type LavoroNonProgettuale as enum ('Didattica', 'Ricerca', 'Missione', 'Incontro Dipartimentale', 'Incontro Accademico', 'Altro');

create type CausaAssenza as enum ('Chiusura Universitaria', 'Maternita', 'Malattia');


create domain PosInteger as integer check (value >= 0);

create domain StringaM as varchar(100);

create domain NumeroOre as integer check (value >= 0 and value <= 8);

create domain Denaro as real ≥ 0;



create table Persona(
    id PosInteger primary key, 
    nome StringaM not null,
    cognome StringaM not null, 
    posizione Strutturato not null,
    stipendio Denaro not null
);


create table Progetto(
    id PosInteger not null,
    nome StringaM not null,
    inizio date not null,
    fine date not null,
    budget Denaro not null,
    primary key (id),
    unique (nome),
    check (inizio < fine)
);

create table WP(
    progetto PosInteger not null,
    id PosInteger not null,
    nome StringaM not null,
    inizio date not null,
    fine date not null,
    unique (progetto, nome),
    primary key (progetto, id),
    foreign key (progetto) references Progetto(id),
    check (inizio < fine)
);

create table AttivitaProgetto(
    id PosInteger not null,
    persona PosInteger not null,
    progetto PosInteger not null,
    wp PosInteger not null,
    giorno date not null,
    tipo LavoroProgetto not null,
    oreDurata NumeroOre not null,
    primary key (id),
    foreign key (persona) references Persona(id),
    foreign key (progetto, wp) references WP(progetto, id)
);

create table AttivitaNonProgettuale(
    id PosInteger primary key,
    persona PosInteger not null, 
    tipo LavoroNonProgettuale not null,
    giorno date not null,
    oreDurata NumeroOre not null,
    foreign key (persona) references Persona(id)
);

create table Assenza(
    id PosInteger primary key,
    persona PosInteger not null,
    tipo CausaAssenza not null,
    giorno date not null,
    unique (persona, giorno),
    foreign key (persona) references Persona(id)
);


insert into Persona(id, nome, cognome, posizione, stipendio) values (48965, 'Dino', 'Campana', 'Ricercatore', 1500);
insert into Persona(id, nome, cognome, posizione, stipendio) values (59648, 'Giorgia', 'Milo', 'Professore Associato', 1900);
insert into Persona(id, nome, cognome, posizione, stipendio) values (49562, 'Viola', 'Ricci', 'Professore Ordinario', 1980);
insert into Persona(id, nome, cognome, posizione, stipendio) values (13246, 'Daniele', 'Pinto', 'Ricercatore', 1600);


insert into Progetto(id, nome, inizio, fine, budget) values (47889, 'Security', '02/11/2025', '09/03/2026', 25000);
insert into Progetto(id, nome, inizio, fine, budget) values (42163, 'R3', '18/05/2025', '16/10/2025', 14000);
insert into Progetto(id, nome, inizio, fine, budget) values (49631, 'Tor93', '17/07/2025', '19/09/2026', 18000);

