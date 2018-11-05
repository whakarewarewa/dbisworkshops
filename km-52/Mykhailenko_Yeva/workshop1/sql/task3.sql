CREATE OR REPLACE TRIGGER USER_DELETION 
before delete on USERS for each row
begin 
if  user <> 'ADMINISTRATOR' then 
  raise_application_error(-20003,'YOU ARE NOT GRANTED TO DELETE USER');
end if;
end USER_DELETION;

DELETE FROM USERS
WHERE USER_NAME = 'STUDENT1';
