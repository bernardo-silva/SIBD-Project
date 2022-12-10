-- A. The name of all boats that are used in some trip.
SELECT boat_name
FROM boat
JOIN trip t
    ON boat.cni = t.cni;

-- B. The name of all boats that are not used in any trip.
SELECT boat_name
FROM boat b
WHERE (b.cni, b.country_name) NOT IN(
    SELECT (cni, country_name) FROM trip t);


-- C. The name of all boats registered in 'PRT' (ISO code) for which at least one responsible for a
-- reservation has a surname that ends with 'Santos'.
-- D. The full name of all skippers without any certificate corresponding to the class of the trip’s boat.