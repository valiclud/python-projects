use addressary;

Drop table if exists Addressary;

Create table Addressary (
      Id_addressary Integer Not Null auto_increment,
      Forname VarChar(20) Null,
      Surname VarChar(30) Null,
      Address VarChar(50) Null,
      Constraint PK_Addresary Primary Key (Id_addressary)
);