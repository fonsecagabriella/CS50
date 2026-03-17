-- Create and use database
CREATE DATABASE IF NOT EXISTS `linkedin`;
USE `linkedin`;

-- Users table
CREATE TABLE IF NOT EXISTS `users`(
    `id` INT AUTO_INCREMENT,
    `first_name` VARCHAR(50) NOT NULL,
    `last_name` VARCHAR(255) NOT NULL,
    `username` VARCHAR(16) UNIQUE NOT NULL,
    `password` HASH(255) NOT NULL,
    `date_of_birth` DATETIME,
    `date_creation_profile` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (`id`)
);

-- Schools and Universities table
CREATE TABLE IF NOT EXISTS `schools` (
    `id` INT AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `type` ENUM('Primary', 'Secondary', 'Higher Education') NOT NULL,
    `location` VARCHAR(255) NOT NULL,
    `year_founded` YEAR NOT NULL,
    `date_creation_profile` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (`id`)


);

-- Companies table
CREATE TABLE IF NOT EXISTS `companies` (
    `id` INT AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `industry` ENUM('Technology', 'Education', 'Business') NOT NULL,
    `location` VARCHAR(255) NOT NULL,
    `date_creation_profile` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (`id`)
);

-- People connections table
CREATE TABLE IF NOT EXISTS `user_connections` (
    `id` INT AUTO_INCREMENT,
    `user_id` INT NOT NULL,
    `connection_id` INT NOT NULL,

    PRIMARY KEY (`id`),
    FOREIGN KEY (`user_id`) REFERENCES `users`(`id`),
    FOREIGN KEY (`connection_id`) REFERENCES `users`(`id`)
);

-- School connections table
CREATE TABLE IF NOT EXISTS `school_connections` (
    `id` INT AUTO_INCREMENT,
    `user_id` INT NOT NULL,
    `school_id` INT NOT NULL,
    `start_date_affiliation` DATE NOT NULL,
    `end_date_affiliation` DATE,
    `type_affiliation` VARCHAR(10) NOT NULL,

    PRIMARY KEY (`id`),
    FOREIGN KEY (`user_id`) REFERENCES `users`(`id`),
    FOREIGN KEY (`school_id`) REFERENCES `schools`(`id`)
);

-- Company connections table
CREATE TABLE IF NOT EXISTS `company_connections` (
    `id` INT AUTO_INCREMENT,
    `user_id` INT NOT NULL,
    `company_id` INT NOT NULL,
    `start_date_affiliation` DATE NOT NULL,
    `end_date_affiliation` DATE,
    `title` VARCHAR(10) NOT NULL,

    PRIMARY KEY (`id`),
    FOREIGN KEY (`user_id`) REFERENCES `users`(`id`),
    FOREIGN KEY (`company_id`) REFERENCES `companies`(`id`)
);