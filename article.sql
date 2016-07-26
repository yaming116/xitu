/*
Date: 2016-07-26 20:50:11
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for article
-- ----------------------------
DROP TABLE IF EXISTS `article`;
CREATE TABLE `article` (
  `objectId` varchar(32) NOT NULL,
  `title` varchar(256) DEFAULT NULL,
  `author` varchar(64) DEFAULT NULL,
  `content` varchar(512) DEFAULT NULL,
  `tagsTitleArray` varchar(256) DEFAULT NULL,
  `category` varchar(128) DEFAULT NULL,
  `hotIndex` int(11) DEFAULT NULL,
  `updatedAt` varchar(32) DEFAULT NULL,
  `viewsCount` int(11) DEFAULT NULL,
  `collectionCount` int(11) DEFAULT NULL,
  `hot` char(2) DEFAULT NULL,
  `original` char(2) DEFAULT NULL,
  `createdAt` varchar(32) DEFAULT NULL,
  `type` varchar(32) DEFAULT NULL,
  `english` char(2) DEFAULT NULL,
  `rankIndex` float(11,11) DEFAULT NULL,
  `url` varchar(128) DEFAULT NULL,
  `gfw` char(2) DEFAULT NULL,
  `commentsCount` int(11) DEFAULT NULL,
  `subscribersCount` int(11) DEFAULT NULL,
  `userId` varchar(32) DEFAULT NULL,
  `originalUrl` varchar(128) DEFAULT NULL,
  `photoUrl` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`objectId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
