CREATE TABLE country(
    name VARCHAR(70),
    iso_code CHAR(3) NOT NULL,
    flag VARCHAR(2083) NOT NULL,
    PRIMARY KEY(name),
    UNIQUE(iso_code)
);

CREATE TABLE location(
    latitude NUMERIC(8,6),
    longitude NUMERIC(9,6),
    name VARCHAR(30) NOT NULL,
    jurisdiction_of VARCHAR(70) NOT NULL,
    PRIMARY KEY(latitude, longitude),
    FOREIGN KEY(jurisdiction_of) REFERENCES country(name)
);

CREATE TABLE sailor(
    email VARCHAR(254),
    first_name VARCHAR(40) NOT NULL,
    surname VARCHAR(40) NOT NULL,
    PRIMARY KEY(email)

    -- No sailor can exist at the same time in the 'senior' table and
    -- the 'junior' table
);

CREATE TABLE senior(
    email VARCHAR(254),
    PRIMARY KEY(email),
    FOREIGN KEY(email) REFERENCES sailor(email)
    -- A senior sailor must exist in the 'sailor' table
    -- A senior sailor cannot exist in the 'junior' table
);

CREATE TABLE junior(
    email VARCHAR(254),
    PRIMARY KEY(email),
    FOREIGN KEY(email) REFERENCES sailor(email)
    -- A junior sailor must exist in the 'sailor' table
    -- A junior sailor cannot exist in the 'senior' table
);

CREATE TABLE boat_class(
    name VARCHAR(10),
    max_length NUMERIC(3,1) NOT NULL,
    PRIMARY KEY(name)
);

CREATE TABLE boat(
    country_name VARCHAR(70),
    cni CHAR(14),
    boat_name VARCHAR(80) NOT NULL,
    length NUMERIC(3,1) NOT NULL,
    year NUMERIC(4,0) NOT NULL,
    has_class_name VARCHAR(10) NOT NULL,
    PRIMARY KEY(country_name, cni),
    FOREIGN KEY(country_name) REFERENCES country(name),
    FOREIGN KEY(has_class_name) REFERENCES boat_class(name)
);

CREATE TABLE sailing_certificate(
    sailor_email VARCHAR(254),
    issue_date DATE,
    expiry_date DATE NOT NULL,
    for_class VARCHAR(10) NOT NULL,
    PRIMARY KEY(sailor_email,issue_date),
    FOREIGN KEY(sailor_email) REFERENCES sailor(email),
    FOREIGN KEY(for_class) REFERENCES boat_class(name)

    -- Every sailing certificate must exist in the table
    -- 'valid_for'
);

CREATE TABLE valid_for(
    country_name VARCHAR(70),
    sailor_email VARCHAR(254),
    issue_date TIMESTAMP,
    PRIMARY KEY(country_name, sailor_email, issue_date),
    FOREIGN KEY(country_name) REFERENCES country(name),
    FOREIGN KEY(sailor_email, issue_date) REFERENCES sailing_certificate(sailor_email, issue_date)
);

CREATE TABLE date_interval(
    start_date TIMESTAMP,
    end_date TIMESTAMP,
    PRIMARY KEY(start_date, end_date)
);

CREATE TABLE reservation(
    start_date TIMESTAMP,
    end_date TIMESTAMP,
    country_name VARCHAR(70),
    cni CHAR(14),
    responsible_email VARCHAR(254),
    PRIMARY KEY(start_date, end_date, country_name, cni),
    FOREIGN KEY(start_date, end_date) REFERENCES date_interval(start_date, end_date),
    FOREIGN KEY(country_name, cni) REFERENCES boat(country_name,cni),
    FOREIGN KEY(responsible_email) REFERENCES senior(email)
    -- Every reservation must exist in the 'authorised' table
);

CREATE TABLE authorised(
    email VARCHAR(254),
    start_date TIMESTAMP,
    end_date TIMESTAMP,
    country_name VARCHAR(70),
    cni CHAR(14),
    PRIMARY KEY(start_date, end_date, country_name, cni, email),
    FOREIGN KEY(start_date, end_date, country_name, cni) REFERENCES reservation(start_date, end_date, country_name, cni),
    FOREIGN KEY(email) REFERENCES sailor(email)
);

CREATE TABLE trip(
    res_start_date TIMESTAMP,
    res_end_date TIMESTAMP,
    country_name VARCHAR(70),
    cni CHAR(14),
    take_off_date TIMESTAMP,
    arrival_date TIMESTAMP NOT NULL,
    insurance VARCHAR(20) NOT NULL,
    skipper_email VARCHAR(254) NOT NULL,
    from_latitude NUMERIC(8,6) NOT NULL,
    from_longitude NUMERIC(9,6) NOT NULL,
    to_latitude NUMERIC(8,6) NOT NULL,
    to_longitude NUMERIC(9,6) NOT NULL,
    PRIMARY KEY(res_start_date, res_end_date, country_name, cni, take_off_date),
    FOREIGN KEY(res_start_date, res_end_date, country_name, cni) REFERENCES reservation(start_date, end_date, country_name, cni),
    FOREIGN KEY(skipper_email) REFERENCES sailor(email),
    FOREIGN KEY(from_latitude, from_longitude) REFERENCES location(latitude,longitude),
    FOREIGN KEY(to_latitude, to_longitude) REFERENCES location(latitude, longitude)
);