create PACKAGE USER_PACKAGE AS

FUNCTION login_user (
        loginuser      UNI_USER.USER_LOGIN%TYPE,
        passworduser   UNI_USER.USER_PASSWORD%TYPE
    ) RETURN NUMBER;

FUNCTION check_user (
        loginuser      UNI_USER.USER_LOGIN%TYPE
    ) RETURN NUMBER;

FUNCTION get_role(
      username  UNI_USER.USER_LOGIN%TYPE
) RETURN VARCHAR2;

  FUNCTION register_student (
        loginuser      UNI_USER.USER_LOGIN%TYPE,
        s_id           STUDENT.CARD_ID%TYPE
    ) RETURN NUMBER;

FUNCTION register_teacher (
        loginuser      UNI_USER.USER_LOGIN%TYPE,
        t_id           TEACHER.CONTRACT_ID%TYPE
    ) RETURN NUMBER;


END USER_PACKAGE;
/

create PACKAGE BODY USER_PACKAGE IS
    
FUNCTION login_user (
        loginuser      UNI_USER.USER_LOGIN%TYPE,
        passworduser   UNI_USER.USER_PASSWORD%TYPE
    ) RETURN NUMBER IS
        res   NUMBER(1);
    BEGIN
        SELECT
            COUNT(*)
        INTO res
        FROM
            UNI_USER
        WHERE
            (UNI_USER.USER_LOGIN = loginuser)
            AND (UNI_USER.USER_PASSWORD = passworduser);

        return(res);
    END login_user;

FUNCTION check_user (
        loginuser      UNI_USER.USER_LOGIN%TYPE
    ) RETURN NUMBER IS
        res   NUMBER(1);
    BEGIN
        SELECT
            COUNT(*)
        INTO res
        FROM
            UNI_USER
        WHERE
            UNI_USER.USER_LOGIN = loginuser;
        return(res);
    END check_user;

FUNCTION get_role(
      username  UNI_USER.USER_LOGIN%TYPE
) RETURN VARCHAR2 IS
  name VARCHAR2(8);
  BEGIN
    SELECT
    ROLE_NAME
    INTO name
    FROM UNI_USER
        WHERE UNI_USER.USER_LOGIN = username;
    return(name);
  END get_role;

FUNCTION register_student (
        loginuser      UNI_USER.USER_LOGIN%TYPE,
        s_id           STUDENT.CARD_ID%TYPE
    ) RETURN NUMBER IS
        res   NUMBER(1);
    BEGIN
        SELECT
            COUNT(*)
        INTO res
        FROM
            UNI_USER JOIN STUDENT ON UNI_USER.USER_LOGIN = STUDENT.USER_LOGIN
        WHERE
            (UNI_USER.USER_LOGIN = loginuser)
            OR (STUDENT.CARD_ID = s_id);

        return(res);
    END register_student;

FUNCTION register_teacher(
        loginuser      UNI_USER.USER_LOGIN%TYPE,
        t_id           TEACHER.CONTRACT_ID%TYPE
    ) RETURN NUMBER IS
        res   NUMBER(1);
    BEGIN
        SELECT
            COUNT(*)
        INTO res
        FROM
            UNI_USER JOIN TEACHER ON UNI_USER.USER_LOGIN = TEACHER.USER_LOGIN
        WHERE
            (UNI_USER.USER_LOGIN = loginuser)
            OR (TEACHER.CONTRACT_ID = t_id);

        return(res);
    END register_teacher;

END USER_PACKAGE;
/

