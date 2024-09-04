MSSQL Guides
============

# Grant User Access to Database

Entire database, for granual access to tables you will need to do a different method.

This assumes the user already exists as a login for the server.

## GUI Method

Open MSSQL Managment Studio

Connect to target db

Expand: Database, Security, Logins

Right click on target user and select properties

Select **User Mapping**

Check **Map** for the database you want to grant access to.

Under **Database role membership for: DB Name** check the desired roles

For read access check **db_datareader**

For write access check **db_datawriter**

Click **OK**

## Command Method

```
USE [DatabaseName]
GO
CREATE USER [Username] FOR LOGIN [Username]
GO
USE [DatabaseName]
GO
ALTER ROLE [db_datareader] ADD MEMBER [Username]
GO
USE [DatabaseName]
GO
ALTER ROLE [db_datawriter] ADD MEMBER [Username]
GO
```
