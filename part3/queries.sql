-- ===============   Part 3   ===============  
-- ==========  PostgreSQL Queries  =========== 
-- 



-- 1. Which country has more boats registered than any other?
SELECT b.country
FROM boat b
GROUP BY b.country
HAVING COUNT(*) > ALL (
    SELECT COUNT(*)
    FROM boat
    WHERE country <> b.country
    GROUP BY country
);

-- 2. List all the sailors that have at least two certificates.
SELECT CONCAT(s.firstname, ' ', s.surname) as sailor
FROM sailing_certificate sc
    JOIN sailor s
        ON s.email = sc.sailor
GROUP BY s.email
HAVING COUNT(*) >= 2;


-- 3. Who are the sailors that have sailed to every location in 'Portugal'?
SELECT CONCAT(s.firstname, ' ', s.surname) as sailor
FROM sailor s
    JOIN authorised a
        ON s.email = a.sailor
    JOIN reservation r
        ON a.cni = r.cni
        AND a.boat_country = r.country
        AND a.start_date = r.start_date
        AND a.end_date = r.end_date
    JOIN trip t
        ON t.cni = r.cni
        AND t.boat_country = r.country
        AND t.reservation_start_date = r.start_date
        AND t.reservation_end_date = r.end_date
    JOIN location l
        ON t.to_latitude = l.latitude
            AND t.to_longitude = l.longitude
WHERE l.country_name = 'Portugal'
GROUP BY s.email
HAVING COUNT(DISTINCT CONCAT(l.longitude, l.latitude)) = (
    SELECT COUNT(*)
    FROM location
    WHERE country_name = 'Portugal');


-- 4. List the sailors with the most skipped trips.
SELECT CONCAT(s.firstname, ' ', s.surname) as sailor
FROM trip t
    JOIN sailor s
        ON s.email = t.skipper
GROUP BY s.email
HAVING COUNT(*) >= ALL (
    SELECT COUNT(*)
    FROM trip
    GROUP BY skipper
);

-- 5. List the sailors with the longest duration of trips (sum of trip durations) for the same
-- single reservation; display also the sum of the trips duration.
SELECT CONCAT(s.firstname, ' ', s.surname) as sailor, SUM(AGE(t.arrival,t.takeoff)) AS sum_trip_duration
FROM sailor s
    JOIN authorised a
        ON s.email = a.sailor
    JOIN reservation r
        ON a.cni = r.cni
        AND a.boat_country = r.country
        AND a.start_date = r.start_date
        AND a.end_date = r.end_date
    JOIN trip t
        ON t.cni = r.cni
        AND t.boat_country = r.country
        AND t.reservation_start_date = r.start_date
        AND t.reservation_end_date = r.end_date
GROUP BY s.firstname, s.surname, r.cni, r.country, r.start_date, r.end_date
HAVING SUM(t.arrival - t.takeoff) >= ALL (
    SELECT SUM(t2.arrival - t2.takeoff)
    FROM sailor s2
        JOIN authorised a2
            ON s2.email = a2.sailor
        JOIN reservation r2
            ON a2.cni = r2.cni
            AND a2.boat_country = r2.country
            AND a2.start_date = r2.start_date
            AND a2.end_date = r2.end_date
        JOIN trip t2
            ON t2.cni = r2.cni
            AND t2.boat_country = r2.country
            AND t2.reservation_start_date = r2.start_date
            AND t2.reservation_end_date = r2.end_date
    GROUP BY s2.firstname, s2.surname, r2.cni, r2.country, r2.start_date, r2.end_date
);
