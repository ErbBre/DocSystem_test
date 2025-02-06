-- =========================================
--  Table of languages - ISO 639-1
-- =========================================

create table sett_languages(
    code_lan        CHAR(2) NOT NULL UNIQUE,
    description_lan varchar(50)
);


INSERT INTO sett_languages(description_lan, code_lan) VALUES 
('Español',  'ES'),
('Inglés',  'EN'),
('Francés',  'FR'),
('Alemán',  'DE'),
('Italiano',  'IT'),
('Portugués',  'PT'),
('Holandés',  'NL'),
('Ruso',  'RU'),
('Chino simplificado',  'ZH'),
('Japonés',  'JA'),
('Árabe',  'AR'),
('Coreano',  'KO'),
('Sueco',  'SV'),
('Danés',  'DA'),
('Noruego',  'NO'),
('Polaco',  'PL'),
('Turco',  'TR'),
('Griego',  'EL'),
('Hebreo',  'HE'),
('Hindi',  'HI'),
('Búlgaro',  'BG'),
('Checo',  'CS'),
('Finlandés',  'FI'),
('Rumano',  'RO'),
('Ucraniano',  'UK'),
('Vietnamita',  'VI'),
('Indonesio',  'ID'),
('Tailandés',  'TH'),
('Malayo',  'MS'),
('Filipino',  'TL');