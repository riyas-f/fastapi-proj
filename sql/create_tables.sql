-- create table TBL_Users(

-- 	UserID INT NOT NULL GENERATED ALWAYS AS IDENTITY,
-- 	UserFullName varchar(40) NOT NULL,
-- 	UserEmail varchar(40) NOT NULL,
-- 	UserPassword varchar(150) NOT NULL,
	
-- 	CONSTRAINT tbl_users_pkey PRIMARY KEY (UserID)

-- );



-- create table TBL_Posts(

-- 	PostID INT NOT NULL GENERATED ALWAYS AS IDENTITY,
-- 	UserID INT NOT null,
-- 	PostTitle varchar(40) NOT NULL,
-- 	PostCreateDate varchar(40) NOT NULL,
-- 	PostContent varchar(40) NOT NULL

-- );

-- ALTER TABLE public.TBL_Posts ADD CONSTRAINT tbl_posts_user_id_fkey FOREIGN KEY (UserID) REFERENCES public.TBL_Users(UserID);

-- -- create_table.sql
-- CREATE TABLE TBL_Users (
--     UserID SERIAL PRIMARY KEY,
--     UserFullName VARCHAR(40) NOT NULL,
--     UserEmail VARCHAR(40) NOT NULL,
--     UserPassword VARCHAR(150) NOT NULL
-- );

-- CREATE TABLE TBL_Posts (
--     PostID SERIAL PRIMARY KEY,
--     UserID INT NOT NULL,
--     PostTitle VARCHAR(40) NOT NULL,
--     PostCreateDate TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
--     PostContent TEXT NOT NULL,
--     CONSTRAINT tbl_posts_user_id_fkey FOREIGN KEY (UserID) REFERENCES TBL_Users(UserID)
-- );

CREATE TABLE TBL_Users (
    UserID SERIAL PRIMARY KEY,
    UserFullName VARCHAR(40) NOT NULL,
    UserEmail VARCHAR(40) NOT NULL,
    UserPassword VARCHAR(150) NOT NULL
);


CREATE TABLE TBL_Teachers (
    TeacherId SERIAL PRIMARY KEY,
    FullName VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE TBL_Students (
    StudentId SERIAL PRIMARY KEY,
    FullName VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE TBL_TeacherStudentAssignments (
    Id SERIAL PRIMARY KEY,
    TeacherId INT NOT NULL,
    StudentId INT NOT NULL,
    FOREIGN KEY (TeacherId) REFERENCES TBL_Teachers(TeacherId) ON DELETE CASCADE,
    FOREIGN KEY (StudentId) REFERENCES TBL_Students(StudentId) ON DELETE CASCADE
);
