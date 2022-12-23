----------                TEST ICs                       -----------
--------------------------------------------------------------------

---------- (IC-1) Every Sailor is either Senior or Junior ----------
--------------------------------------------------------------------

-- This won't work because a sailor must be specialized
INSERT INTO sailor VALUES('Conor','McDavid','conor-mcdavid@barcos.pt');

-- This won't work because the same sailor is inserted into both tables
START TRANSACTION;
SET CONSTRAINTS ALL DEFERRED;
INSERT INTO sailor VALUES('Conor','McDavid','conor-mcdavid@barcos.pt');
INSERT INTO senior VALUES('conor-mcdavid@barcos.pt');
INSERT INTO junior VALUES('conor-mcdavid@barcos.pt');
COMMIT;

-- This will work
START TRANSACTION;
SET CONSTRAINTS ALL DEFERRED;
INSERT INTO sailor VALUES('Leon','Draisaitl','leon-draisaitl@barcos.pt');
INSERT INTO senior VALUES('leon-draisaitl@barcos.pt');
COMMIT;

-- This will also work
START TRANSACTION;
SET CONSTRAINTS ALL DEFERRED;
INSERT INTO sailor VALUES('Kirill','Kaprizov','kirill-kaprizov@barcos.pt');
INSERT INTO junior VALUES('kirill-kaprizov@barcos.pt');
COMMIT;

----------- (IC-2) The take-off and arrival dates of Trips for the same  ----------
----------- reservation must not overlap (i.e., one Trip cannot take off ----------
----------- before the arrival of another).                              ----------
-----------------------------------------------------------------------------------

-- This won't work because a trip already exists with the same dates
INSERT INTO trip VALUES ('2026-06-15', '2026-07-01',
                         'AAA-HUE-700',
                         -5.775032, -35.206148,
                         -5.775032, -35.206148,
                         'xavier-fernandes@barcos.pt',
                         '2026-05-15', '2026-07-15',
                         'Brazil', 'BR1A'
                         );

-- This won't work because the trip date overlaps with an existing one
INSERT INTO trip VALUES ('2026-06-15', '2026-06-18',
                         'AAA-HUE-700',
                         -5.775032, -35.206148,
                         -5.775032, -35.206148,
                         'xavier-fernandes@barcos.pt',
                         '2026-05-15', '2026-07-15',
                         'Brazil', 'BR1A'
                         );

-- This will work because the trip date doesn't overlap with any other trip
INSERT INTO trip VALUES ('2026-07-2', '2026-07-12',
                         'AAA-HUE-700',
                         -5.775032, -35.206148,
                         -5.775032, -35.206148,
                         'xavier-fernandes@barcos.pt',
                         '2026-05-15', '2026-07-15',
                         'Brazil', 'BR1A'
                         );

-- This will also work because the trip date doesn't overlap with any other trip
INSERT INTO trip VALUES ('2026-07-13', '2026-07-14',
                         'AAA-HUE-700',
                         -5.775032, -35.206148,
                         -5.775032, -35.206148,
                         'xavier-fernandes@barcos.pt',
                         '2026-05-15', '2026-07-15',
                         'Brazil', 'BR1A'
                         );