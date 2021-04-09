IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Employee]') AND type in (N'U'))
DROP TABLE [dbo].[Employee]

CREATE TABLE [dbo].[Employee](
	[ID] [int] NULL,
    [Name] [varchar](50) NULL,
    [Age] [int] NULL,)

insert into Employee values (1,'Rajat',22)
insert into Employee values (2,'Raj',23)

select * from Employee
