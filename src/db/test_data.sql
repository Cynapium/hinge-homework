INSERT INTO user VALUES (101, "Alice", "Smith", "01/01/1990", "Hey this is my description", null, null);
INSERT INTO user VALUES (102, "Bob", "John", "03/30/1990", "Hi there", "M", null);
INSERT INTO user VALUES (103, "Charlie", "Thomas", "12/25/1995", "Lorem ipsum", "M", null);
INSERT INTO user VALUES (104, "Daphnee", "P", "09/12/1993", "Test test", "F", "M");
INSERT INTO user VALUES (105, "Elena", "", "06/24/1996", "", "F", "M");
INSERT INTO user VALUES (106, "Finn", "", "08/11/1991", "Hello world!", "M", "F");
#
INSERT INTO rating (user, user_target, type) VALUES (101, 102, "L");
#
INSERT INTO rating (user, user_target, type) VALUES (102, 101, "L");
INSERT INTO rating (user, user_target, type) VALUES (102, 103, "L");
INSERT INTO rating (user, user_target, type) VALUES (102, 104, "R");
INSERT INTO rating (user, user_target, type) VALUES (102, 105, "L");
INSERT INTO rating (user, user_target, type) VALUES (102, 106, "L");
#
INSERT INTO rating (user, user_target, type) VALUES (103, 101, "L");
INSERT INTO rating (user, user_target, type) VALUES (103, 102, "B");
INSERT INTO rating (user, user_target, type) VALUES (103, 104, "R");
#
INSERT INTO rating (user, user_target, type) VALUES (104, 101, "L");
INSERT INTO rating (user, user_target, type) VALUES (104, 103, "L");
#
INSERT INTO rating (user, user_target, type) VALUES (105, 101, "L");
INSERT INTO rating (user, user_target, type) VALUES (105, 103, "L");
INSERT INTO rating (user, user_target, type) VALUES (105, 104, "R");
