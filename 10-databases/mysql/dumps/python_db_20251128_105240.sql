-- Valentina Studio --
-- MySQL dump --
-- ---------------------------------------------------------


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
-- ---------------------------------------------------------


-- CREATE DATABASE "python_db" -----------------------------
CREATE DATABASE IF NOT EXISTS `python_db` CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `python_db`;
-- ---------------------------------------------------------


-- CREATE TABLE "persone" --------------------------------------
CREATE TABLE `persone`( 
	`id` Int( 0 ) AUTO_INCREMENT NOT NULL,
	`nome` VarChar( 255 ) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
	`cognome` VarChar( 255 ) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
	`data_nascita` Date NULL DEFAULT NULL,
	PRIMARY KEY ( `id` ) )
CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci
ENGINE = InnoDB
AUTO_INCREMENT = 4;
-- -------------------------------------------------------------


-- Dump data of "persone" ----------------------------------
BEGIN;

INSERT INTO `persone`(`id`,`nome`,`cognome`,`data_nascita`) VALUES 
( '1', 'Giovanni', 'Rossi', '1995-07-23' ),
( '2', 'Mario', 'Bianchi', '1990-10-01' ),
( '3', 'Simona', 'Gialli', '2005-12-15' ),
( '4', 'Laura', 'Verdi', '2001-03-08' ),
( '5', 'Laura', 'Verdi', '2001-03-08' );
COMMIT;
-- ---------------------------------------------------------


/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
-- ---------------------------------------------------------


