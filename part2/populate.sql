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

INSERT INTO senior VALUES ('paulo-carreira@barcos.pt');
INSERT INTO senior VALUES ('francisco-regateiro@barcos.pt');
INSERT INTO senior VALUES ('pedro-dias@barcos.pt');

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
INSERT INTO sailing_certificate VALUES('xavier-fernandes@barcos.pt', '2022-12-10', '2024-12-10', 'A');

INSERT INTO trip VALUES ();