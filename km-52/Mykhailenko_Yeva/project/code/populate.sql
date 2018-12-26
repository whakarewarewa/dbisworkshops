INSERT INTO DISCIPLINE (DISCIPLINE_NAME)
VALUES('DATA BASES');
INSERT INTO DISCIPLINE (DISCIPLINE_NAME)
VALUES ('OPERATING SYSTEMS');
INSERT INTO DISCIPLINE (DISCIPLINE_NAME)
VALUES ('ENGLISH');
INSERT INTO DISCIPLINE (DISCIPLINE_NAME)
VALUES ('ECONOMICS');
INSERT INTO DISCIPLINE (DISCIPLINE_NAME)
VALUES ('MATHEMATICAL MODELS');

INSERT INTO UNI_ROLE (ROLE_NAME)
VALUES('STUDENT');
INSERT INTO UNI_ROLE (ROLE_NAME)
VALUES ('TEACHER');

INSERT INTO UNI_USER (USER_LOGIN, USER_PASSWORD, ROLE_NAME)
VALUES('happy007', 'uibsgfz56','STUDENT');
INSERT INTO UNI_USER (USER_LOGIN, USER_PASSWORD, ROLE_NAME)
VALUES ('unicorn99', 'tgvdfd','STUDENT');
INSERT INTO UNI_USER (USER_LOGIN, USER_PASSWORD, ROLE_NAME)
VALUES ('4everbestprofessor', '9jsfg','TEACHER');
INSERT INTO UNI_USER (USER_LOGIN, USER_PASSWORD, ROLE_NAME)
VALUES ('pythongod', 'u7ihbvs','TEACHER');
INSERT INTO UNI_USER (USER_LOGIN, USER_PASSWORD, ROLE_NAME)
VALUES ('superman', 'yhg7hnsf','TEACHER');

INSERT INTO STUDENT (CARD_ID, STUDENT_NAME, ST_SEMESTER, USER_LOGIN)
VALUES('509867', 'STUDENT ONE', 3, 'happy007');
INSERT INTO STUDENT (CARD_ID, STUDENT_NAME, ST_SEMESTER, USER_LOGIN)
VALUES ('890732', 'STUDENT TWO', 4, 'unicorn99');

INSERT INTO TEACHER (CONTRACT_ID, TEACHER_NAME, USER_LOGIN)
VALUES('673988', 'TEACHER ONE', 'superman');
INSERT INTO TEACHER (CONTRACT_ID, TEACHER_NAME, USER_LOGIN)
VALUES ('099222', 'TEACHER TWO', '4everbestprofessor');
INSERT INTO TEACHER (CONTRACT_ID, TEACHER_NAME, USER_LOGIN)
VALUES ('678390', 'TEACHER THREE', 'pythongod');

INSERT INTO HOMEWORK (DISCIPLINE_NAME, CONTRACT_ID, HW_DATE, HW_DESCRIPTION)
VALUES('DATA BASES', '673988', TO_DATE('22/09/2018'), 'CREATE USE CASE DIAGRAM');
INSERT INTO HOMEWORK (DISCIPLINE_NAME, CONTRACT_ID, HW_DATE, HW_DESCRIPTION)
VALUES ('OPERATING SYSTEMS', '673988', TO_DATE('17/10/2018'),'PREPARE FOR A TEST');
INSERT INTO HOMEWORK (DISCIPLINE_NAME, CONTRACT_ID, HW_DATE, HW_DESCRIPTION)
VALUES ('ENGLISH', '099222', TO_DATE('01/11/2018'),'WRITE MOTIVATION LETTER');
INSERT INTO HOMEWORK (DISCIPLINE_NAME, CONTRACT_ID, HW_DATE, HW_DESCRIPTION)
VALUES('MATHEMATICAL MODELS', '678390', TO_DATE('12/09/2018'), 'CREATE A MODEL OF A FREE FALLING OBJECT');

INSERT INTO MARK (CARD_ID, DISCIPLINE_NAME, ST_YEAR, MARK)
VALUES('509867', 'ENGLISH', TO_DATE('12/2018', 'mm/yyyy'), 98);
INSERT INTO MARK (CARD_ID, DISCIPLINE_NAME, ST_YEAR, MARK)
VALUES ('509867', 'DATA BASES', TO_DATE('12/2018', 'mm/yyyy'), 89);
INSERT INTO MARK (CARD_ID, DISCIPLINE_NAME, ST_YEAR, MARK)
VALUES ('509867', 'OPERATING SYSTEMS', TO_DATE('12/2018', 'mm/yyyy'), 67);
INSERT INTO MARK (CARD_ID, DISCIPLINE_NAME, ST_YEAR, MARK)
VALUES('509867', 'MATHEMATICAL MODELS', TO_DATE('12/2018', 'mm/yyyy'), 75);

