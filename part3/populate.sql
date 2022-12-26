START TRANSACTION;
SET CONSTRAINTS ALL DEFERRED;

INSERT INTO country VALUES
                        ('PRT', 'https://www.worldometers.info/img/flags/po-flag.gif','Portugal'),
                        ('ESP', 'https://www.worldometers.info/img/flags/sp-flag.gif','Spain'),
                        ('BRA', 'https://www.worldometers.info/img/flags/br-flag.gif', 'Brazil'),
                        ('CHE', 'https://www.worldometers.info/img/flags/sz-flag.gif', 'Switzerland'),
                        ('CAN', 'https://www.worldometers.info/img/flags/ca-flag.gif', 'Canada');

INSERT INTO location VALUES
                        (38.704908, -9.145890, 'Cais do Sodré', 'Portugal'),
                        (38.688212, -9.148381, 'Cacilhas', 'Portugal'),
                        (38.652309, -9.079597, 'Barreiro', 'Portugal'),
                        (38.845133, 0.120084, 'Dénia', 'Spain'),
                        (38.909212, 1.440670, 'Ibiza', 'Spain'),
                        (-5.775032, -35.206148, 'Natal', 'Brazil');

INSERT INTO sailor VALUES
                        ('Paulo', 'Carreira','paulo-carreira@barcos.pt'),
                        ('Francisco', 'Regateiro', 'francisco-regateiro@barcos.pt'),
                        ('Pedro', 'Dias','pedro-dias@barcos.pt'),
                        ('Xavier', 'Fernandes', 'xavier-fernandes@barcos.pt'),
                        ('José', 'Brito', 'jose-brito@barcos.pt'),
                        ('Bernardo', 'Silva', 'bernardo-silva@barcos.pt'),
                        ('Santos', 'dos Santos', 'santos-dos-santos@barcos.pt');

INSERT INTO senior VALUES
                        ('paulo-carreira@barcos.pt'),
                        ('francisco-regateiro@barcos.pt'),
                        ('pedro-dias@barcos.pt'),
                        ('santos-dos-santos@barcos.pt');

INSERT INTO junior VALUES
                        ('xavier-fernandes@barcos.pt'),
                        ('jose-brito@barcos.pt'),
                        ('bernardo-silva@barcos.pt');

INSERT INTO boat_class VALUES
                        ('A', '5'),
                        ('B', '10'),
                        ('C', '15'),
                        ('D', '20');

INSERT INTO sailing_certificate VALUES
                        ('2000-12-10', '2100-12-10', 'paulo-carreira@barcos.pt',  'D'),
                        ('2003-12-10', '2089-12-10', 'paulo-carreira@barcos.pt', 'C'),
                        ('2000-12-10', '2100-12-10', 'francisco-regateiro@barcos.pt', 'B'),
                        ('2022-12-10', '2027-12-10', 'xavier-fernandes@barcos.pt', 'A'),
                        ('2021-12-10', '2023-12-10', 'pedro-dias@barcos.pt', 'B'),
                        ('2020-12-10', '2024-12-10', 'pedro-dias@barcos.pt', 'C');

INSERT INTO valid_for VALUES
                        ('Portugal', 20, 'paulo-carreira@barcos.pt', '2000-12-10'),
                        ('Spain', 20, 'paulo-carreira@barcos.pt', '2003-12-10'),
                        ('Portugal', 10, 'francisco-regateiro@barcos.pt', '2000-12-10'),
                        ('Brazil', 5, 'xavier-fernandes@barcos.pt', '2022-12-10'),
                        ('Spain', 15, 'pedro-dias@barcos.pt', '2021-12-10');

INSERT INTO boat VALUES
                        ('Portugal', 2000, 'ABC1', 'Barquito', 4, 'A'),
                        ('Portugal', 2008, 'EFG8', 'Barcão', 18, 'D'),
                        ('Portugal', 1563, 'CRV2', 'Caravela', 17, 'D'),
                        ('Spain', 2002, 'SP1', 'Embarcacion', 7, 'B'),
                        ('Spain', 2014, 'SP2', 'Barconcillo', 13, 'C'),
                        ('Brazil', 2001, 'BR1A', 'Barco', 4.5,'A');


INSERT INTO date_interval VALUES
                        ('2021-10-10', '2021-10-20'),
                        ('2020-05-14', '2021-06-17'),
                        ('2023-11-01', '2026-11-02'),
                        ('2025-11-01', '2025-11-02'),
                        ('2022-10-10', '2022-10-20'),
                        ('2026-05-15', '2026-07-15');

INSERT INTO reservation VALUES
                        ('2021-10-10', '2021-10-20', 'Portugal', 'EFG8', 'paulo-carreira@barcos.pt'),
                        ('2020-05-14', '2021-06-17', 'Spain', 'SP1', 'pedro-dias@barcos.pt'),
                        ('2023-11-01', '2026-11-02', 'Portugal', 'ABC1', 'francisco-regateiro@barcos.pt'),
                        ('2025-11-01', '2025-11-02', 'Portugal', 'ABC1', 'santos-dos-santos@barcos.pt'),
                        ('2022-10-10', '2022-10-20', 'Spain', 'SP1', 'santos-dos-santos@barcos.pt'),
                        ('2026-05-15', '2026-07-15', 'Brazil', 'BR1A', 'francisco-regateiro@barcos.pt');

INSERT INTO authorised VALUES
                        ('2021-10-10', '2021-10-20', 'Portugal', 'EFG8', 'paulo-carreira@barcos.pt'),
                        ('2021-10-10', '2021-10-20', 'Portugal', 'EFG8', 'xavier-fernandes@barcos.pt'),
                        ('2021-10-10', '2021-10-20', 'Portugal', 'EFG8', 'pedro-dias@barcos.pt'),
                        ('2020-05-14', '2021-06-17', 'Spain', 'SP1', 'pedro-dias@barcos.pt'),
                        ('2020-05-14', '2021-06-17', 'Spain', 'SP1', 'bernardo-silva@barcos.pt'),
                        ('2023-11-01', '2026-11-02', 'Portugal', 'ABC1', 'francisco-regateiro@barcos.pt'),
                        ('2023-11-01', '2026-11-02', 'Portugal', 'ABC1', 'jose-brito@barcos.pt'),
                        ('2023-11-01', '2026-11-02', 'Portugal', 'ABC1', 'xavier-fernandes@barcos.pt'),
                        ('2025-11-01', '2025-11-02', 'Portugal', 'ABC1', 'santos-dos-santos@barcos.pt'),
                        ('2022-10-10', '2022-10-20', 'Spain', 'SP1', 'santos-dos-santos@barcos.pt'),
                        ('2022-10-10', '2022-10-20', 'Spain', 'SP1', 'pedro-dias@barcos.pt'),
                        ('2026-05-15', '2026-07-15', 'Brazil', 'BR1A', 'xavier-fernandes@barcos.pt'),
                        ('2026-05-15', '2026-07-15', 'Brazil', 'BR1A', 'francisco-regateiro@barcos.pt');


INSERT INTO trip VALUES ('2021-10-11', '2021-10-19',
                         'OASD-2312-vv',
                         38.704908, -9.145890,
                         -5.775032, -35.206148,
                         'pedro-dias@barcos.pt',
                         '2021-10-10', '2021-10-20',
                         'Portugal', 'EFG8'
                         );


INSERT INTO trip VALUES ('2020-05-15', '2021-06-16',
                         'ADA-asd-1313',
                         38.845133, 0.120084,
                         38.909212, 1.440670,
                         'bernardo-silva@barcos.pt',
                         '2020-05-14', '2021-06-17',
                         'Spain', 'SP1');


-- (38.704908, -9.145890, 'Cais do Sodré', 'Portugal'),
-- (38.688212, -9.148381, 'Cacilhas', 'Portugal'),
-- (38.652309, -9.079597, 'Barreiro', 'Portugal'),
INSERT INTO trip VALUES ('2023-11-01', '2023-12-01',
                         'AAA-HUE-999',
                         38.704908, -9.145890,
                         38.652309, -9.079597,
                         'xavier-fernandes@barcos.pt',
                         '2023-11-01', '2026-11-02',
                         'Portugal', 'ABC1'
                         );

INSERT INTO trip VALUES ('2024-01-01', '2024-02-01',
                         'AAA-HUE-999',
                         38.652309, -9.079597,
                         38.704908, -9.145890,
                         'francisco-regateiro@barcos.pt',
                         '2023-11-01', '2026-11-02',
                         'Portugal', 'ABC1'
                         );


INSERT INTO trip VALUES ('2024-02-02', '2026-11-01',
                         'AAA-HUE-999',
                         38.704908, -9.145890,
                         38.688212, -9.148381,
                         'xavier-fernandes@barcos.pt',
                         '2023-11-01', '2026-11-02',
                         'Portugal', 'ABC1'
                         );

INSERT INTO trip VALUES ('2022-10-11', '2022-10-19',
                         'ADA-asd-1913',
                         38.845133, 0.120084,
                         38.909212, 1.440670,
                         'pedro-dias@barcos.pt',
                         '2022-10-10', '2022-10-20',
                         'Spain', 'SP1'
                         );

INSERT INTO trip VALUES ('2026-06-15', '2026-07-01',
                         'AAA-HUE-700',
                         -5.775032, -35.206148,
                         -5.775032, -35.206148,
                         'xavier-fernandes@barcos.pt',
                         '2026-05-15', '2026-07-15',
                         'Brazil', 'BR1A'
                         );

COMMIT;