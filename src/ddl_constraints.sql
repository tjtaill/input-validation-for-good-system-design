CREATE TABLE user (
    id SERIAL PRIMARY KEY, -- NOT NULL UNIQUE
    name VARCHAR(50) NOT NULL CHECK(LENGTH(name) > 0),
    age INT NOT NULL CHECK(age > 0 AND age < 130)
);

CREATE TABLE time_ranges (
    id SERIAL PRIMARY KEY,
    start_time DATETIME NOT NULL,
    end_time DATETIME NOT NULL,
    CONSTRAINT CHECK(start_time < end_time)
);
