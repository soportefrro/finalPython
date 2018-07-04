CREATE DATABASE  IF NOT EXISTS `mundial2018` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `mundial2018`;
-- MySQL dump 10.13  Distrib 5.7.12, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: mundial2018
-- ------------------------------------------------------
-- Server version	5.7.15-log

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
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cliente` (
  `dni` varchar(8) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `apellido` varchar(45) NOT NULL,
  `mail` varchar(45) NOT NULL,
  PRIMARY KEY (`dni`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
INSERT INTO `cliente` VALUES ('39270102','Augusto','Maneiro','maneiro.augusto@gmail.com'),('39710982','Micaela','Mastrovincenzo','mb.mastrovincenzo@gmail.com');
/*!40000 ALTER TABLE `cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `entrada`
--

DROP TABLE IF EXISTS `entrada`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `entrada` (
  `fechaVenta` date NOT NULL,
  `nroComprobante` int(11) NOT NULL AUTO_INCREMENT,
  `dni` varchar(45) NOT NULL,
  `idPartido` int(11) NOT NULL,
  `nroAsiento` int(11) NOT NULL,
  `precioUSD` float NOT NULL,
  `cotizacionDolar` float NOT NULL,
  `precioARS` float NOT NULL,
  PRIMARY KEY (`nroComprobante`),
  KEY `fk_entrada_cliente_idx` (`dni`),
  KEY `fk_entrada_vip_idx` (`idPartido`),
  KEY `fk_entrada_vip2_idx` (`nroAsiento`),
  CONSTRAINT `fk_entrada_cliente` FOREIGN KEY (`dni`) REFERENCES `cliente` (`dni`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_entrada_vip` FOREIGN KEY (`idPartido`) REFERENCES `vip` (`idPartido`) ON UPDATE CASCADE,
  CONSTRAINT `fk_entrada_vip2` FOREIGN KEY (`nroAsiento`) REFERENCES `vip` (`nroAsiento`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `entrada`
--

LOCK TABLES `entrada` WRITE;
/*!40000 ALTER TABLE `entrada` DISABLE KEYS */;
/*!40000 ALTER TABLE `entrada` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estadio`
--

DROP TABLE IF EXISTS `estadio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `estadio` (
  `nombre` varchar(45) NOT NULL,
  `capacidad` int(11) NOT NULL,
  `ciudad` varchar(45) NOT NULL,
  PRIMARY KEY (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estadio`
--

LOCK TABLES `estadio` WRITE;
/*!40000 ALTER TABLE `estadio` DISABLE KEYS */;
INSERT INTO `estadio` VALUES ('Ekaterimburgo Arena',30,'Ekaterimburgo'),('Fisht',30,'Sochi'),('Kaliningrado',30,'Kaliningrado'),('Kazan Arena',30,'Kazan'),('Luzhniki',30,'Moscú'),('Mordovia Arena',30,'Saransk'),('Nizhni',30,'Novgorod'),('Rostov Arena',30,'Rostov'),('Samara Arena',30,'Samara'),('San Petersburgo',30,'San Perersburgo'),('Spartak',30,'Moscú'),('Volvogrado Arena',30,'Volvogrado');
/*!40000 ALTER TABLE `estadio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `partido`
--

DROP TABLE IF EXISTS `partido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `partido` (
  `idPartido` int(11) NOT NULL AUTO_INCREMENT,
  `fechaPartido` date NOT NULL,
  `pais1` varchar(45) NOT NULL,
  `pais2` varchar(45) NOT NULL,
  `instancia` varchar(45) NOT NULL,
  `precioUSD` float NOT NULL,
  `nombreEstadio` varchar(45) NOT NULL,
  PRIMARY KEY (`idPartido`),
  KEY `fk_partido_estadio_idx` (`nombreEstadio`),
  CONSTRAINT `fk_partido_estadio` FOREIGN KEY (`nombreEstadio`) REFERENCES `estadio` (`nombre`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `partido`
--

LOCK TABLES `partido` WRITE;
/*!40000 ALTER TABLE `partido` DISABLE KEYS */;
INSERT INTO `partido` VALUES (1,'2018-06-16','Argentina','Islandia','Grupo D',95,'Spartak'),(2,'2018-06-16','Croacia','Nigeria','Grupo D',80,'Kaliningrado'),(3,'2018-06-21','Argentina','Croacia','Grupo D',110,'Nizhni'),(4,'2018-06-22','Nigeria','Islandia','Grupo D',70,'Volvogrado Arena'),(5,'2018-06-26','Nigeria','Argentina','Grupo D',95,'San Petersburgo'),(6,'2018-06-26','Islandia','Croacia','Grupo D',95,'Rostov Arena'),(7,'2018-06-14','Rusia','Arabia Saudita','Grupo A',150,'Luzhniki'),(8,'2018-06-15','Egipto','Uruguay','Grupo A',90,'Ekaterimburgo Arena'),(9,'2018-06-15','Portugal','España','Grupo B',95,'Fisht'),(10,'2018-06-15','Marruecos','Irán','Grupo B',70,'San Petersburgo'),(11,'2018-06-17','Brasil','Suiza','Grupo E',85,'Rostov Arena'),(12,'2018-06-17','Costa Rica','Serbia','Grupo E',80,'Samara Arena');
/*!40000 ALTER TABLE `partido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vip`
--

DROP TABLE IF EXISTS `vip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vip` (
  `nroAsiento` int(11) NOT NULL,
  `libre` tinyint(2) NOT NULL DEFAULT '1',
  `idPartido` int(11) NOT NULL,
  PRIMARY KEY (`nroAsiento`,`idPartido`),
  KEY `fk_vip_partido_idx` (`idPartido`),
  CONSTRAINT `fk_vip_partido` FOREIGN KEY (`idPartido`) REFERENCES `partido` (`idPartido`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vip`
--

LOCK TABLES `vip` WRITE;
/*!40000 ALTER TABLE `vip` DISABLE KEYS */;
INSERT INTO `vip` VALUES (1,1,1),(1,1,2),(1,1,3),(1,1,4),(1,1,5),(1,1,6),(1,1,7),(1,1,8),(1,1,9),(2,1,1),(2,1,2),(2,1,3),(2,1,4),(2,1,5),(3,1,1),(3,1,2),(3,1,3),(4,1,1),(4,1,3),(5,1,1);
/*!40000 ALTER TABLE `vip` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-07-03 15:07:14
