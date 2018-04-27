CREATE DATABASE IF NOT EXISTS project;

USE project;

CREATE TABLE IF NOT EXISTS twitter_users (
    user_id INT unique AUTO_INCREMENT,
    account_id BIGINT,
    account_name VARCHAR(16),
    bot_score float(3,2),
    is_bot BOOL,
    PRIMARY KEY (user_id)
);