create PACKAGE STUDENT_PACKAGE AS

    FUNCTION GET_STUDENT_INFO(
        USR_LOGIN IN UNI_USER.USER_LOGIN%TYPE
    )RETURN SYS_REFCURSOR;

    FUNCTION GET_STUDENT_MARKS(
        USR_LOGIN IN UNI_USER.USER_LOGIN%TYPE
    )RETURN SYS_REFCURSOR;

    PROCEDURE ADD_STUDENT(
        USR_LOGIN IN UNI_USER.USER_LOGIN%TYPE,
        USR_PASSWORD IN UNI_USER.USER_PASSWORD%TYPE,
        STDNT_ID IN STUDENT.CARD_ID%TYPE, 
        STDNT_NAME IN STUDENT.STUDENT_NAME%TYPE, 
        STUDY_SEMESTER IN STUDENT.ST_SEMESTER%TYPE
    );

    PROCEDURE UPDATE_STUDENT_PASSWORD(
        USR_LOGIN IN UNI_USER.USER_LOGIN%TYPE,
        STDNT_PASSWORD IN UNI_USER.USER_PASSWORD%TYPE
    );

    PROCEDURE UPDATE_STUDENT_NAME(
        USR_LOGIN IN UNI_USER.USER_LOGIN%TYPE,
        STDNT_NAME IN STUDENT.STUDENT_NAME%TYPE
    );

    PROCEDURE DELETE_STUDENT(
        USR_LOGIN IN UNI_USER.USER_LOGIN%TYPE
    );

    FUNCTION find_student (
        s_id           STUDENT.CARD_ID%TYPE
    ) RETURN NUMBER;

END STUDENT_PACKAGE;
/

create PACKAGE BODY STUDENT_PACKAGE IS

    FUNCTION GET_STUDENT_INFO(
        USR_LOGIN IN UNI_USER.USER_LOGIN%TYPE
    )RETURN SYS_REFCURSOR
    IS
      cursorchik SYS_REFCURSOR;
    BEGIN
    OPEN cursorchik FOR
        SELECT DISTINCT UNI_USER.USER_LOGIN, UNI_USER.USER_PASSWORD, STUDENT.CARD_ID, STUDENT.STUDENT_NAME
        FROM STUDENT JOIN UNI_USER ON STUDENT.USER_LOGIN = UNI_USER.USER_LOGIN
        WHERE STUDENT.USER_LOGIN = USR_LOGIN;
    RETURN cursorchik;
    END GET_STUDENT_INFO;

    FUNCTION GET_STUDENT_MARKS(
        USR_LOGIN IN UNI_USER.USER_LOGIN%TYPE
    )RETURN SYS_REFCURSOR
    IS
      cursorchik SYS_REFCURSOR;
    BEGIN
    OPEN cursorchik FOR
        SELECT DISTINCT MARK.DISCIPLINE_NAME, MARK.MARK
        FROM STUDENT JOIN MARK ON
        STUDENT.CARD_ID = MARK.CARD_ID
        WHERE STUDENT.USER_LOGIN = USR_LOGIN and MARK.DELETED is NULL;
    RETURN cursorchik;
    END GET_STUDENT_MARKS;

    PROCEDURE ADD_STUDENT(
    USR_LOGIN IN UNI_USER.USER_LOGIN%TYPE,
    USR_PASSWORD IN UNI_USER.USER_PASSWORD%TYPE,
    STDNT_ID IN STUDENT.CARD_ID%TYPE, 
    STDNT_NAME IN STUDENT.STUDENT_NAME%TYPE, 
    STUDY_SEMESTER IN STUDENT.ST_SEMESTER%TYPE
    )
    IS
    BEGIN
    INSERT INTO UNI_USER (USER_LOGIN, USER_PASSWORD, ROLE_NAME)
    VALUES (USR_LOGIN, USR_PASSWORD, 'STUDENT');
    INSERT INTO STUDENT (USER_LOGIN, CARD_ID, STUDENT_NAME, ST_SEMESTER)
    VALUES (USR_LOGIN, STDNT_ID, STDNT_NAME, STUDY_SEMESTER);
    COMMIT;
    END ADD_STUDENT;

    PROCEDURE UPDATE_STUDENT_PASSWORD(
        USR_LOGIN IN UNI_USER.USER_LOGIN%TYPE,
        STDNT_PASSWORD IN UNI_USER.USER_PASSWORD%TYPE
    )
    IS
    BEGIN
    UPDATE UNI_USER 
    SET UNI_USER.USER_PASSWORD = STDNT_PASSWORD
    WHERE UNI_USER.USER_LOGIN = USR_LOGIN;
    COMMIT;
    END UPDATE_STUDENT_PASSWORD;

    PROCEDURE UPDATE_STUDENT_NAME(
        USR_LOGIN IN UNI_USER.USER_LOGIN%TYPE,
        STDNT_NAME IN STUDENT.STUDENT_NAME%TYPE
    )
    IS
    BEGIN
    UPDATE STUDENT 
    SET STUDENT.STUDENT_NAME = STDNT_NAME
    WHERE STUDENT.USER_LOGIN = USR_LOGIN;
    COMMIT;
    END UPDATE_STUDENT_NAME;

    PROCEDURE DELETE_STUDENT(
    USR_LOGIN IN UNI_USER.USER_LOGIN%TYPE
    )
    IS
    BEGIN
    DELETE FROM DELETED_MARK WHERE CARD_ID IN
                               (SELECT DELETED_MARK.CARD_ID
                               FROM DELETED_MARK JOIN STUDENT on DELETED_MARK.CARD_ID = STUDENT.CARD_ID
                               WHERE STUDENT.USER_LOGIN = USR_LOGIN);
    DELETE FROM STUDENT
    WHERE STUDENT.USER_LOGIN  = USR_LOGIN;
    DELETE FROM UNI_USER
    WHERE UNI_USER.USER_LOGIN  = USR_LOGIN;
    COMMIT;
    END DELETE_STUDENT;

    FUNCTION find_student (
        s_id           STUDENT.CARD_ID%TYPE
    ) RETURN NUMBER IS
        res   NUMBER(1);
    BEGIN
        SELECT
            COUNT(*)
        INTO res
        FROM
            STUDENT
        WHERE
            STUDENT.CARD_ID = s_id;
        return(res);
    END find_student;

END STUDENT_PACKAGE;
/

