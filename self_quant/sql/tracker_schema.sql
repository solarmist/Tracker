SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

DROP SCHEMA IF EXISTS `tracker` ;
CREATE SCHEMA IF NOT EXISTS `tracker` DEFAULT CHARACTER SET utf8 ;
USE `tracker` ;

-- -----------------------------------------------------
-- Table `tracker`.`user`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `tracker`.`user` ;

CREATE  TABLE IF NOT EXISTS `tracker`.`user` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT ,
  `name` VARCHAR(90) NOT NULL ,
  `email` VARCHAR(90) NOT NULL ,
  `password` CHAR(60) NOT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tracker`.`user_group`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `tracker`.`user_group` ;

CREATE  TABLE IF NOT EXISTS `tracker`.`user_group` (
  `id` INT UNSIGNED NOT NULL ,
  `uid` INT UNSIGNED NOT NULL ,
  `name` VARCHAR(90) NOT NULL ,
  CONSTRAINT `uid`
    FOREIGN KEY (`uid` )
    REFERENCES `tracker`.`user` (`id` )
    ON DELETE NO ACTION
    ON UPDATE CASCADE)
ENGINE = InnoDB
COMMENT = 'This tables allows groups of users to be created, so they ca' /* comment truncated */;

CREATE INDEX `user ids` ON `tracker`.`user_group` (`uid` ASC) ;


-- -----------------------------------------------------
-- Table `tracker`.`measurement_type`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `tracker`.`measurement_type` ;

CREATE  TABLE IF NOT EXISTS `tracker`.`measurement_type` (
  `type` VARCHAR(90) NOT NULL ,
  `units` VARCHAR(90) NOT NULL ,
  PRIMARY KEY (`type`, `units`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tracker`.`measurement`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `tracker`.`measurement` ;

CREATE  TABLE IF NOT EXISTS `tracker`.`measurement` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT ,
  `uid` INT UNSIGNED NOT NULL ,
  `dt` DATETIME NOT NULL COMMENT 'Date and time a recording happened' ,
  `category` VARCHAR(90) NULL COMMENT 'Allows grouping of multiple types of measurements' ,
  `type` VARCHAR(90) NOT NULL COMMENT 'i.e. weight, height, body fat, sleep score, etc.' ,
  `value` DOUBLE NOT NULL ,
  PRIMARY KEY (`id`) ,
  CONSTRAINT `type`
    FOREIGN KEY (`type` )
    REFERENCES `tracker`.`measurement_type` (`type` )
    ON DELETE NO ACTION
    ON UPDATE CASCADE,
  CONSTRAINT `fk_data_user1`
    FOREIGN KEY (`uid` )
    REFERENCES `tracker`.`user` (`id` )
    ON DELETE NO ACTION
    ON UPDATE CASCADE)
ENGINE = InnoDB
COMMENT = 'Actual measurements are stored here and the ';

CREATE INDEX `measurement type` ON `tracker`.`measurement` (`type` ASC) ;

CREATE INDEX `fk_data_user2` ON `tracker`.`measurement` (`uid` ASC) ;


-- -----------------------------------------------------
-- Table `tracker`.`media`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `tracker`.`media` ;

CREATE  TABLE IF NOT EXISTS `tracker`.`media` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT ,
  `uid` INT UNSIGNED NOT NULL COMMENT 'The user_id.' ,
  `dt` DATETIME NOT NULL ,
  `type` VARCHAR(90) NOT NULL COMMENT 'The type of the file, txt, jpg, png, gif, mp4, etc.' ,
  `file` TEXT NOT NULL COMMENT 'The location of the file on the filesystem relative to the base file dir' ,
  `metadata` TEXT NOT NULL ,
  PRIMARY KEY (`id`) ,
  CONSTRAINT `id`
    FOREIGN KEY (`uid` )
    REFERENCES `tracker`.`user` (`id` )
    ON DELETE NO ACTION
    ON UPDATE CASCADE)
ENGINE = InnoDB
COMMENT = 'Keep extra data, like process pictures, audio files, video, ' /* comment truncated */;

CREATE INDEX `media id` ON `tracker`.`media` (`uid` ASC) ;


-- -----------------------------------------------------
-- Table `tracker`.`goal`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `tracker`.`goal` ;

CREATE  TABLE IF NOT EXISTS `tracker`.`goal` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT ,
  `uid` INT UNSIGNED NOT NULL ,
  `start` DATETIME NOT NULL ,
  `end` DATETIME NOT NULL ,
  `successful` TINYINT(1) NULL ,
  `type` VARCHAR(90) NOT NULL ,
  `group_success` TINYINT(1) NULL ,
  `initial` DOUBLE NULL COMMENT 'The beginning measurement\n' ,
  `final` DOUBLE NULL COMMENT 'The ending measurement' ,
  PRIMARY KEY (`id`) ,
  CONSTRAINT `fk_goal_user1`
    FOREIGN KEY (`uid` )
    REFERENCES `tracker`.`user` (`id` )
    ON DELETE NO ACTION
    ON UPDATE CASCADE,
  CONSTRAINT `fk_goal_measurement1`
    FOREIGN KEY (`type` )
    REFERENCES `tracker`.`measurement_type` (`type` )
    ON DELETE NO ACTION
    ON UPDATE CASCADE)
ENGINE = InnoDB;

CREATE INDEX `fk_goal_user3` ON `tracker`.`goal` (`uid` ASC) ;

CREATE INDEX `fk_goal_measurement2` ON `tracker`.`goal` (`type` ASC) ;


-- -----------------------------------------------------
-- Table `tracker`.`goal_group`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `tracker`.`goal_group` ;

CREATE  TABLE IF NOT EXISTS `tracker`.`goal_group` (
  `id` INT UNSIGNED NOT NULL ,
  `name` VARCHAR(90) NOT NULL ,
  `gid` INT UNSIGNED NOT NULL ,
  CONSTRAINT `fk_goal_group_goal1`
    FOREIGN KEY (`gid` )
    REFERENCES `tracker`.`goal` (`id` )
    ON DELETE NO ACTION
    ON UPDATE CASCADE)
ENGINE = InnoDB
COMMENT = 'Group together sets of goals to have an overall goal';

CREATE INDEX `fk_goal_group_goal3` ON `tracker`.`goal_group` (`gid` ASC) ;


CREATE USER `tracker` IDENTIFIED BY 'tracker_db';

grant ALL on TABLE `tracker`.`measurement` to tracker;
grant ALL on TABLE `tracker`.`user` to tracker;
grant ALL on TABLE `tracker`.`goal` to tracker;
grant ALL on TABLE `tracker`.`goal_group` to tracker;
grant ALL on TABLE `tracker`.`measurement_type` to tracker;
grant ALL on TABLE `tracker`.`user_group` to tracker;
grant ALL on TABLE `tracker`.`media` to tracker;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- Data for table `tracker`.`measurement_type`
-- -----------------------------------------------------
START TRANSACTION;
USE `tracker`;
INSERT INTO `tracker`.`measurement_type` (`type`, `units`) VALUES ('waist', 'in');
INSERT INTO `tracker`.`measurement_type` (`type`, `units`) VALUES ('waist', 'cm');
INSERT INTO `tracker`.`measurement_type` (`type`, `units`) VALUES ('weight', 'kg');
INSERT INTO `tracker`.`measurement_type` (`type`, `units`) VALUES ('weight', 'lbs');
INSERT INTO `tracker`.`measurement_type` (`type`, `units`) VALUES ('weight', 'stones');

COMMIT;
