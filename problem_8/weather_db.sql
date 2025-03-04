CREATE TABLE weather_data (
                              id INTEGER PRIMARY KEY AUTOINCREMENT,
                              city TEXT NOT NULL,
                              temperature REAL NOT NULL,
                              humidity INTEGER NOT NULL,
                              wind_speed REAL NOT NULL,
                              date_recorded DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Insert initial weather data
INSERT INTO weather_data (city, temperature, humidity, wind_speed) VALUES
                                                                       ('Tbilisi', 22.5, 65, 3.2),
                                                                       ('Batumi', 25.8, 78, 5.1),
                                                                       ('Kutaisi', 20.3, 60, 2.7),
                                                                       ('Rustavi', 23.1, 55, 4.0),
                                                                       ('Poti', 26.4, 82, 6.5);