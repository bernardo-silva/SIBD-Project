DROP VIEW IF EXISTS trip_info;

CREATE VIEW trip_info AS
SELECT 
    c1.iso_code AS country_iso_origin, 
    c1.name AS country_name_origin,
    c2.iso_code AS country_iso_dest, 
    c2.name AS country_name_dest,
    l1.name AS loc_name_origin,
    l2.name AS loc_name_dest,
    t.cni AS cni_boat,
    cb.iso_code AS country_iso_boat, 
    t.boat_country AS country_name_boat,
    t.takeoff AS trip_start_date

FROM trip t
    JOIN location l1 
        ON (t.from_latitude, t.from_longitude) = (l1.latitude, l1.longitude)
    JOIN location l2 
        ON (t.to_latitude, t.to_longitude) = (l2.latitude, l2.longitude)
    JOIN country c1 
        ON l1.country_name = c1.name
    JOIN country c2 
        ON l2.country_name = c2.name
    JOIN country cb 
        ON t.boat_country = cb.name;
