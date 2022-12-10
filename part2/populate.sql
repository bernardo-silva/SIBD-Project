INSERT INTO country VALUES ('Portugal', 'PRT', 'https://upload.wikimedia.org/wikipedia/commons/5/5c/Flag_of_Portugal.svg');
INSERT INTO country VALUES ('Spain', 'ESP', 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Bandera_de_Espa%C3%B1a.svg/1125px-Bandera_de_Espa%C3%B1a.svg.png');
INSERT INTO country VALUES ('Brazil', 'BRA', 'https://upload.wikimedia.org/wikipedia/en/thumb/0/05/Flag_of_Brazil.svg/188px-Flag_of_Brazil.svg.png');
INSERT INTO country VALUES ('Switzerland', 'CHE', 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Flag_of_Switzerland_%28Pantone%29.svg/800px-Flag_of_Switzerland_%28Pantone%29.svg.png');

INSERT INTO location VALUES (38.704908, -9.145890, 'Cais do Sodré', 'Portugal');
INSERT INTO location VALUES (38.688212, -9.148381, 'Cacilhas', 'Portugal');
INSERT INTO location VALUES (38.652309, -9.079597, 'Barreiro', 'Portugal');
INSERT INTO location VALUES (38.845133, 0.120084, 'Dénia', 'Spain');
INSERT INTO location VALUES (38.909212, 1.440670, 'Ibiza', 'Spain');
INSERT INTO location VALUES (-5.775032, -35.206148, 'Natal', 'Brazil');

INSERT INTO sailor VALUES ('paulo-carreira@barcos.pt', 'Paulo', 'Carreira');
INSERT INTO sailor VALUES ('francisco-regateiro@barcos.pt', 'Francisco', 'Regateiro');
INSERT INTO sailor VALUES ('pedro-dias@barcos.pt', 'Pedro', 'Dias');
INSERT INTO sailor VALUES ('xavier-fernandes@barcos.pt', 'Xavier', 'Fernandes');
INSERT INTO sailor VALUES ('jose-brito@barcos.pt', 'José', 'Brito');
INSERT INTO sailor VALUES ('bernardo-silva@barcos.pt', 'Bernardo', 'Silva');
INSERT INTO sailor VALUES ('santos-dos-santos@barcos.pt', 'Santos', 'dos Santos');

INSERT INTO senior VALUES ('paulo-carreira@barcos.pt');
INSERT INTO senior VALUES ('francisco-regateiro@barcos.pt');
INSERT INTO senior VALUES ('pedro-dias@barcos.pt');
INSERT INTO senior VALUES ('santos-dos-santos@barcos.pt');

INSERT INTO junior VALUES ('xavier-fernandes@barcos.pt');
INSERT INTO junior VALUES ('jose-brito@barcos.pt');
INSERT INTO junior VALUES ('bernardo-silva@barcos.pt');

INSERT INTO boat_class VALUES ('A', '5');
INSERT INTO boat_class VALUES ('B', '10');
INSERT INTO boat_class VALUES ('C', '15');
INSERT INTO boat_class VALUES ('D', '20');

INSERT INTO boat VALUES ('Portugal', 'ABC1', 'Barquito', 4, 2000, 'A');
INSERT INTO boat VALUES ('Portugal', 'EFG8', 'Barcão', 18, 2008, 'D');
INSERT INTO boat VALUES ('Spain', 'SP1', 'Embarcacion', 7, 2002, 'B');
INSERT INTO boat VALUES ('Spain', 'SP2', 'Barconcillo', 13, 2014, 'C');

INSERT INTO sailing_certificate VALUES('paulo-carreira@barcos.pt', '2000-12-10', '2100-12-10', 'D');
INSERT INTO sailing_certificate VALUES('paulo-carreira@barcos.pt', '2003-12-10', '2089-12-10', 'C');
INSERT INTO sailing_certificate VALUES('francisco-regateiro@barcos.pt', '2000-12-10', '2100-12-10', 'B');
INSERT INTO sailing_certificate VALUES('xavier-fernandes@barcos.pt', '2022-12-10', '2024-12-10', 'A');
INSERT INTO sailing_certificate VALUES('pedro-dias@barcos.pt', '2021-12-10', '2023-12-10', 'B');

INSERT INTO valid_for VALUES('Portugal', 'paulo-carreira@barcos.pt', '2000-12-10');
INSERT INTO valid_for VALUES('Spain','paulo-carreira@barcos.pt', '2003-12-10');
INSERT INTO valid_for VALUES('Portugal','francisco-regateiro@barcos.pt', '2000-12-10');
INSERT INTO valid_for VALUES('Brazil','xavier-fernandes@barcos.pt', '2022-12-10');
INSERT INTO valid_for VALUES('Spain','pedro-dias@barcos.pt', '2021-12-10');

INSERT INTO  date_interval VALUES ('2021-10-10', '2021-10-20');
INSERT INTO  date_interval VALUES ('2020-05-14', '2021-06-17');
INSERT INTO  date_interval VALUES ('2023-11-01', '2021-11-02');
INSERT INTO  date_interval VALUES ('2025-11-01', '2025-11-02');

INSERT INTO reservation VALUES ('2021-10-10', '2021-10-20', 'Portugal', 'EFG8', 'paulo-carreira@barcos.pt');
INSERT INTO reservation VALUES ('2020-05-14', '2021-06-17', 'Spain', 'SP1', 'pedro-dias@barcos.pt');
INSERT INTO reservation VALUES ('2023-11-01', '2021-11-02', 'Portugal', 'ABC1', 'francisco-regateiro@barcos.pt');
INSERT INTO reservation VALUES ('2025-11-01', '2025-11-02', 'Portugal', 'ABC1', 'santos-dos-santos@barcos.pt');

INSERT INTO authorised VALUES ('paulo-carreira@barcos.pt', '2021-10-10', '2021-10-20', 'Portugal', 'EFG8');
INSERT INTO authorised VALUES ('xavier-fernandes@barcos.pt', '2021-10-10', '2021-10-20', 'Portugal', 'EFG8');
INSERT INTO authorised VALUES ('pedro-dias@barcos.pt', '2021-10-10', '2021-10-20', 'Portugal', 'EFG8');

INSERT INTO authorised VALUES ('pedro-dias@barcos.pt', '2020-05-14', '2021-06-17', 'Spain', 'SP1');
INSERT INTO authorised VALUES ('bernardo-silva@barcos.pt', '2020-05-14', '2021-06-17', 'Spain', 'SP1');

INSERT INTO authorised VALUES ('francisco-regateiro@barcos.pt', '2023-11-01', '2021-11-02', 'Portugal', 'ABC1');
INSERT INTO authorised VALUES ('jose-brito@barcos.pt', '2023-11-01', '2021-11-02', 'Portugal', 'ABC1');

INSERT INTO authorised VALUES ('santos-dos-santos@barcos.pt', '2025-11-01', '2025-11-02', 'Portugal', 'ABC1');


INSERT INTO trip VALUES ('2021-10-10', '2021-10-20', 'Portugal', 'EFG8',
                         '2021-10-11', '2021-10-19',
                         'OASD-2312-vv', 'pedro-dias@barcos.pt',
                         38.704908, -9.145890,
                         -5.775032, -35.206148);

INSERT INTO trip VALUES ('2020-05-14', '2021-06-17', 'Spain', 'SP1',
                         '2020-05-15', '2021-06-16',
                         'ADA-asd-1313', 'bernardo-silva@barcos.pt',
                         38.845133, 0.120084,
                         38.909212, 1.440670);

INSERT INTO trip VALUES ('2023-11-01', '2021-11-02', 'Portugal', 'ABC1',
                         '2023-11-01', '2021-11-01',
                         'AAA-HUE-999', 'jose-brito@barcos.pt',
                         38.704908, -9.145890,
                         38.652309, -9.079597);