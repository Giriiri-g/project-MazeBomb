-- MySQL dump 10.10
--
-- Host: localhost    Database: rogue
-- ------------------------------------------------------
-- Server version	5.0.22-community-nt

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `maps`
--

DROP TABLE IF EXISTS `maps`;
CREATE TABLE `maps` (
  `Map_name` varchar(15) default NULL,
  `rows` int(11) default NULL,
  `col` int(11) default NULL,
  `length` int(11) default NULL,
  `data` varchar(2048) default NULL,
  `rooms` int(11) default NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `maps`
--


/*!40000 ALTER TABLE `maps` DISABLE KEYS */;
LOCK TABLES `maps` WRITE;
INSERT INTO `maps` VALUES ('Test1',70,22,1561,'oooooooaddddddddddiooooooooooooooooooooooooooooooooooooooooooooooooooonooooooobffffffffffboooooooooooooooooooooooooooooooaddddddddddddddddddinooooooobffffffffffbooooooooooooooooooooooooooooooobffffffff!fffffffffbnoooooooeddddddkdddjooooooooooooooooooooooooooootttgfffffffffffff!ffffbnooooooooooooootooooooooooooooooooooooooottttttttooekdddddddddddddddddjnooooooooooooootoooooooooooooooooooooooootooooooooootoooooooooooooooooonooooooootttttttoooooooooooooooooooottttttoooooooooottttttooooooooooooonadddddddcddddddddddioooooooooooooootooooooooooooooadddddcddddddddddddinbffffffffffffffffffhtttooooooooooootoooooooooooooobffffffffffffffffffbnbffffffffffffffffffbootooadddddddddcdioooooooooooobffffffffffffffffffbnbffffffffffffffffffbootttgfffffffff!fboooooooooooobffffffffffffffffffbnbffffffffffffffffffbooooobfffffffffffhttttttttttttgffffffffffff!fffffbnbffffffffffffffffffbooooobffff!ffffffboooooooooooobffffffffffffffffffbnedddddddkddddddddddjoooooedddddddddkdjooooooooooooeddddddddddddddddddjnooooooootooooooooooooooooooottttttttoooooooooooooooooooooooooooooooooonooooooootttttttttttoooooooadcdiooooooooooooooooooooooooooooooooooooooonoooooooaddddddddddcdiooootgfffbooooooooooooooooooooooooooaddddiooooooonooooooobffffffffffffhtttttbfffboooooooooooooooooooooooooobffffbooooooonooooooobffffffffffffbooooobfffboooooooooooooooooooooooooobf!ffbooooooonooooooobffffffffffffbooooobfffboottttttttttttttttttttttttgffffbooooooonooooooobfffff!ffffffbooooobfffhtttooooooooooooooooooooooobffffbooooooonoooooooeddddddddddddjoooooedddjooooooooooooooooooooooooooeddddjooooooo',8);
UNLOCK TABLES;
/*!40000 ALTER TABLE `maps` ENABLE KEYS */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `Id` int(11) default NULL,
  `Username` varchar(10) default NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--


/*!40000 ALTER TABLE `users` DISABLE KEYS */;
LOCK TABLES `users` WRITE;
INSERT INTO `users` VALUES (221,'Giriirig'),(119,'PsylectrA');
UNLOCK TABLES;
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

