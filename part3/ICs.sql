---------- (IC-1) Every Sailor is either Senior or Junior ----------
--------------------------------------------------------------------

---------- Drop Triggers ----------
DROP TRIGGER IF EXISTS tg_check_sailor ON sailor;
DROP TRIGGER IF EXISTS tg_check_junior ON junior;
DROP TRIGGER IF EXISTS tg_check_senior ON senior;

---------- Trigger Function -----------

-- check_sailor_integrity(): Checks if all sailors exist in either the senior table or the junior table
-- but not in both at same time
CREATE OR REPLACE FUNCTION check_sailor_integrity()
RETURNS TRIGGER AS
$$
BEGIN
    -- Checks for disjoint specialization of sailor
    -- 1 - Selects emails from senior sailors
    -- 2 - Selects emails from junior sailors
    -- 3 - INTERSECT keeps the emails that exist in both tables
    -- 4 - If an email remains, then it exists in both tables, meaning a sailor is both senior
    --     and junior
    IF EXISTS((SELECT email FROM senior)
              INTERSECT
              SELECT email FROM junior)
    THEN
        RAISE EXCEPTION 'A sailor cannot exist in both the senior table and the junior table';
    END IF;

    --Checks for mandatory specialization of sailor
    -- 1 - Selects email from all sailors
    -- 2 - Selects emails from the UNION of the junior and senior tables
    -- 3 - EXCEPT keeps the emails from the sailor table that do not exist in the second table
    -- 4 - If an email is left, the IF condition triggers
    IF EXISTS(SELECT email FROM sailor
              EXCEPT
             (SELECT email FROM senior UNION SELECT email from junior))
    THEN
        RAISE EXCEPTION 'A sailor must exist in either the senior table or the junior table';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

---------- Trigger Creation ----------
CREATE CONSTRAINT TRIGGER tg_check_sailor
AFTER INSERT OR UPDATE ON sailor DEFERRABLE
FOR EACH ROW EXECUTE PROCEDURE check_sailor_integrity();

CREATE CONSTRAINT TRIGGER tg_check_junior
AFTER INSERT OR UPDATE OR DELETE ON junior DEFERRABLE
FOR EACH ROW EXECUTE PROCEDURE check_sailor_integrity();

CREATE CONSTRAINT TRIGGER tg_check_senior
AFTER INSERT OR UPDATE OR DELETE ON senior DEFERRABLE
FOR EACH ROW EXECUTE PROCEDURE check_sailor_integrity();
--------- END OF (IC-1) -----------


----------- (IC-2) The take-off and arrival dates of Trips for the same  ----------
----------- reservation must not overlap (i.e., one Trip cannot take off ----------
----------- before the arrival of another).                              ----------
-----------------------------------------------------------------------------------

---------- Drop Triggers ----------
DROP TRIGGER IF EXISTS tg_check_trip_overlap ON trip;

---------- Trigger Function -----------

-- check_trip_overlap(): When a trip is inserted into the trip table, checks if its takeoff
-- and arrival date overlap with other trips in the same reservation
CREATE OR REPLACE FUNCTION check_trip_overlap()
RETURNS TRIGGER AS
$$
BEGIN
    -- If a trip from the same reservation as the new one has overlapping dates
    -- then the new trip cannot be inserted.
    IF EXISTS(SELECT * FROM trip AS t
              WHERE t.cni = NEW.cni
              AND t.boat_country = NEW.boat_country
              AND t.reservation_start_date = NEW.reservation_start_date
              AND t.reservation_end_date = NEW.reservation_end_date
              AND (t.arrival >= NEW.takeoff AND t.takeoff <= NEW.arrival))
    THEN
        RAISE EXCEPTION  'Takeoff and arrival dates of new trip overlap with an existing trip';
    END IF;

    RETURN NEW;
END;
$$ language plpgsql;

---------- Trigger Creation ----------
CREATE TRIGGER tg_check_trip_overlap
BEFORE INSERT OR UPDATE ON trip
FOR EACH ROW EXECUTE PROCEDURE check_trip_overlap();
---------- END OF (IC-2) -------------
