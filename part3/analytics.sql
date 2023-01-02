-- ===============   Part 3   ===============
-- ==========  Data Analytics Queries  ===========
--

-- 1. The start date (i.e., per year, per month independently of year, and per exact date);
SELECT date_part('year', trip_start_date) AS year,
       date_part('month', trip_start_date) AS month,
       COUNT(*) AS number_of_trips
FROM trip_info
GROUP BY GROUPING SETS (
    (date_part('year', trip_start_date)),
    (date_part('month', trip_start_date)),
    (trip_start_date));


-- 2. The location of origin (i.e., per location within countries, per country, and in total).
SELECT country_name_origin AS origin_country, loc_name_origin AS origin_location_name, COUNT(*) AS number_of_trips
FROM trip_info
GROUP BY ROLLUP (country_name_origin, loc_name_origin);