-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               5.7.18-log - MySQL Community Server (GPL)
-- Server OS:                    Win64
-- HeidiSQL Version:             9.4.0.5125
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for imdb
CREATE DATABASE IF NOT EXISTS `imdb` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `imdb`;

-- Dumping structure for table imdb.genre
CREATE TABLE IF NOT EXISTS `genre` (
  `genre_id` int(11) NOT NULL,
  `genre_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`genre_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table imdb.genre: ~6 rows (approximately)
/*!40000 ALTER TABLE `genre` DISABLE KEYS */;
INSERT INTO `genre` (`genre_id`, `genre_name`) VALUES
	(1, 'Adventure'),
	(2, 'Family'),
	(3, 'Fantasy'),
	(4, 'Musical'),
	(5, 'Action'),
	(6, 'Sci-Fi');
/*!40000 ALTER TABLE `genre` ENABLE KEYS */;

-- Dumping structure for table imdb.movie
CREATE TABLE IF NOT EXISTS `movie` (
  `movie_id` int(11) NOT NULL AUTO_INCREMENT,
  `popularity` float DEFAULT '0',
  `director` varchar(50) NOT NULL DEFAULT '0',
  `imdb_score` float DEFAULT '0',
  `movie_name` varchar(50) NOT NULL DEFAULT '0',
  PRIMARY KEY (`movie_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- Dumping data for table imdb.movie: ~2 rows (approximately)
/*!40000 ALTER TABLE `movie` DISABLE KEYS */;
INSERT INTO `movie` (`movie_id`, `popularity`, `director`, `imdb_score`, `movie_name`) VALUES
	(1, 83, 'Victor Fleming', 8.3, 'The Wizard of Oz'),
	(2, 88, 'George Lucas', 8.8, 'Star Wars');
/*!40000 ALTER TABLE `movie` ENABLE KEYS */;

-- Dumping structure for table imdb.movie_genre_map
CREATE TABLE IF NOT EXISTS `movie_genre_map` (
  `movie_genre_map_id` int(11) NOT NULL,
  `movie_id` int(11) NOT NULL,
  `genre_id` int(11) NOT NULL,
  PRIMARY KEY (`movie_genre_map_id`),
  KEY `FK_movie_map` (`movie_id`),
  KEY `FK_genre_map` (`genre_id`),
  CONSTRAINT `FK_genre_map` FOREIGN KEY (`genre_id`) REFERENCES `genre` (`genre_id`),
  CONSTRAINT `FK_movie_map` FOREIGN KEY (`movie_id`) REFERENCES `movie` (`movie_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table imdb.movie_genre_map: ~8 rows (approximately)
/*!40000 ALTER TABLE `movie_genre_map` DISABLE KEYS */;
INSERT INTO `movie_genre_map` (`movie_genre_map_id`, `movie_id`, `genre_id`) VALUES
	(1, 1, 1),
	(2, 1, 2),
	(3, 1, 3),
	(4, 1, 4),
	(5, 2, 5),
	(6, 2, 1),
	(7, 2, 3),
	(8, 2, 6);
/*!40000 ALTER TABLE `movie_genre_map` ENABLE KEYS */;

-- Dumping structure for table imdb.role
CREATE TABLE IF NOT EXISTS `role` (
  `role_id` int(11) NOT NULL,
  `role_type` varchar(50) NOT NULL,
  PRIMARY KEY (`role_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table imdb.role: ~2 rows (approximately)
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
INSERT INTO `role` (`role_id`, `role_type`) VALUES
	(1, 'admin'),
	(2, 'enduser');
/*!40000 ALTER TABLE `role` ENABLE KEYS */;

-- Dumping structure for table imdb.user
CREATE TABLE IF NOT EXISTS `user` (
  `user_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  `user_name` varchar(50) NOT NULL,
  PRIMARY KEY (`user_id`),
  KEY `FK_role` (`role_id`),
  CONSTRAINT `FK_role` FOREIGN KEY (`role_id`) REFERENCES `role` (`role_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table imdb.user: ~2 rows (approximately)
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` (`user_id`, `role_id`, `user_name`) VALUES
	(1, 1, 'dev'),
	(2, 2, 'test');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
