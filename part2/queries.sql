-- A. The name of all boats that are used in some trip.
SELECT boat_name
FROM boat b
    JOIN trip t
        ON b.cni = t.cni AND b.country_name = t.country_name
;

-- B. The name of all boats that are not used in any trip.
SELECT boat_name
FROM boat
WHERE (boat_name, cni) NOT IN(
    SELECT (cni, country_name)
    FROM trip
);

-- C. The name of all boats registered in 'PRT' (ISO code) for which at least one responsible for a
-- reservation has a surname that ends with 'Santos'.
SELECT boat_name
FROM boat
    JOIN reservation r
        ON boat.country_name = r.country_name AND boat.cni = r.cni
    JOIN senior s
        ON r.responsible_email = s.email
    JOIN sailor sa
        ON s.email = sa.email
    JOIN country c
        ON boat.country_name = c.name
WHERE c.iso_code = 'PRT' and sa.surname = 'Santos'
;

-- D. The full name of all skippers without any certificate corresponding to the class of the trip’s boat.
SELECT first_name, surname
FROM trip t
    JOIN sailor s
        ON t.skipper_email = s.email
    JOIN sailing_certificate sc
        ON s.email = sc.sailor_email
    JOIN boat b
        ON t.cni = b.cni AND t.country_name = b.country_name
WHERE b.has_class_name <> sc.for_class
;