'/path/to/csv/ZIP_CODES.txt' WITH (FORMAT csv);
COPY table_name FROM '/path/to/csv/ZIP_CODES.txt' WITH (FORMAT csv);
Psql console se hoga
\copy zip_codes FROM '/path/to/csv/ZIP_CODES.txt' DELIMITER ',' CSV
\copy tableName(col1,col2,col3.....) FROM '/path/to/csv/ZIP_CODES.txt' DELIMITER ',' CSV
share improve this answer
\copy tableName(col1,col2,col3.....) FROM '/path/to/csv/ZIP_CODES.txt' DELIMITER ',' CSV