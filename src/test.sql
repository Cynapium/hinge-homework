INSERT INTO user (101, "Alice", "201-209-7463", "alice@gmail.com", "10/10/1990", "Hey this is my description");
INSERT INTO user (102, "Bob", "483-222-3333", "bob@gmail.com", "01/01/1990", "Hi there");
INSERT INTO user (103, "Charlie", "123-456-7890", "charlie@gmail.com", "12/25/1995", "Lorem ipsum");
INSERT INTO user (104, "Daphnee", "098-765-4321", "daphnee@gmail.com", "01/12/1993", "Hello world!");
INSERT INTO user (105, "Elena", "555-555-5555", "elena@gmail.com", "03/24/1996", "Hello world!");
INSERT INTO user (106, "Finn", "666-666-6665", "finn@gmail.com", "08/11/1991", "Hello world!");
# Alice likes everyone
INSERT INTO interaction (101, 102, "L");
INSERT INTO interaction (101, 103, "L");
INSERT INTO interaction (101, 104, "L");
INSERT INTO interaction (101, 105, "L");
INSERT INTO interaction (101, 106, "L");
# Everyone else also likes Finn
INSERT INTO interaction (102, 106, "L");
INSERT INTO interaction (103, 106, "L");
INSERT INTO interaction (104, 106, "L");
INSERT INTO interaction (105, 106, "L");
# Everyone blocked Bob
INSERT INTO interaction (101, 102, "B");
INSERT INTO interaction (103, 102, "B");
INSERT INTO interaction (104, 102, "B");
INSERT INTO interaction (105, 102, "B");
INSERT INTO interaction (106, 102, "B");
# Finn reports Alice & match with Charlie
INSERT INTO interaction (106, 101, "R");
INSERT INTO interaction (106, 103, "M");
# Bob & Daphnee liked Daphnee
INSERT INTO interaction (102, 104, "L");
INSERT INTO interaction (103, 104, "L");
# Daphnee match with Charlie
INSERT INTO interaction (104, 103, "M");
