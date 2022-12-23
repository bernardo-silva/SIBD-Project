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
    -- 1 - Selects emails corresponding to the union of all senior and junior sailors, including duplicates
    -- 2 - Selects emails from sailors table
    -- 3 - EXCEPT ALL keeps the emails that exist in the first table that do not exist in second table
    -- 4 - Using UNION ALL and EXCEPT ALL is crucial, if a sailor is present in both senior and junior
    --     his email will appear twice due to UNION ALL. EXCEPT ALL will remove all entries except for
    --     the duplicate one, meaning the IF condition will trigger.
    IF EXISTS((SELECT email FROM senior UNION ALL SELECT email FROM junior)
              EXCEPT ALL
              SELECT email FROM sailor)
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
DECLARE
    -- Creates a cursor that encapsulates a query that selects all trips from the same reservation
    trip_cursor CURSOR FOR
        SELECT *
        FROM trip
        WHERE (reservation_start_date, reservation_end_date, boat_country, cni) =
              (NEW.reservation_start_date, NEW.reservation_end_date, NEW.boat_country, NEW.cni);
BEGIN
    -- Iterate over all rows in the cursor (i.e., iterate over all trips in the same reservation)
    FOR trip_row in trip_cursor
        LOOP
             -- If the new trip's dates overlap an already existing trip, then raise an exception
             IF (NEW.takeoff <= trip_row.arrival AND NEW.arrival >= trip_row.takeoff) THEN
                RAISE EXCEPTION
                'This trip would overlap with an already existing trip on the same reservation';
            END IF;
        END LOOP;
    RETURN NEW;
END;
$$ language plpgsql;

---------- Trigger Creation ----------
CREATE TRIGGER tg_check_trip_overlap
BEFORE INSERT OR UPDATE ON trip
FOR EACH ROW EXECUTE PROCEDURE check_trip_overlap();
---------- END OF (IC-2) -------------
