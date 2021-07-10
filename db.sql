CREATE DATABASE IF NOT EXISTS `TakeNote` DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
USE `TakeNote`;
CREATE TABLE IF NOT EXISTS `NOTES` (
    `id_note` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `athour` VARCHAR(50) COLLATE utf8_general_ci NOT NULL,
    `description` TEXT(100) COLLATE utf8_general_ci NOT NULL,
    `content` TEXT COLLATE utf8_general_ci NOT NULL,
    `status` VARCHAR(10) NOT NULL,
    `created_at` DATE NOT NULL,
    `updated_at` DATE NOT NULL,
    PRIMARY KEY (`id_note`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8 COLLATE = utf8_general_ci AUTO_INCREMENT = 1;
USE `TakeNote`;
CREATE TABLE IF NOT EXISTS `USERS` (
    `id_user` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `username` VARCHAR(50) COLLATE utf8_general_ci NOT NULL,
    `password` VARCHAR(50) COLLATE utf8_general_ci NOT NULL,
    `created_at` DATE NOT NULL,
    `updated_at` DATE NOT NULL,
    `isLoggedIn` VARCHAR(10) NOT NULL,
    PRIMARY KEY (`id_user`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8 COLLATE = utf8_general_ci AUTO_INCREMENT = 1;