CREATE VIEW DELETED_MARK AS
  SELECT *
  FROM MARK;
  
create or replace trigger trg_delete_student_mark
  instead of delete on DELETED_MARK
  REFERENCING OLD AS deleted_row
  FOR EACH ROW
  begin
    UPDATE MARK
  SET DELETED = systimestamp
  WHERE CARD_ID = :deleted_row.CARD_ID and discipline_name = :deleted_row.discipline_name and st_year = :deleted_row.st_year;
END;
