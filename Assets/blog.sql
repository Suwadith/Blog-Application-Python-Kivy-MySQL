-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 08, 2022 at 07:05 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `blog`
--

-- --------------------------------------------------------

--
-- Table structure for table `blog_posts`
--

CREATE TABLE `blog_posts` (
  `blog_id` int(10) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp(),
  `title` varchar(255) NOT NULL,
  `body` text NOT NULL,
  `file` longblob DEFAULT NULL,
  `visibility` varchar(10) NOT NULL,
  `username` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

set global max_allowed_packet=104857600

--
-- Dumping data for table `blog_posts`
--

INSERT INTO `blog_posts` (`blog_id`, `timestamp`, `title`, `body`, `file`, `visibility`, `username`) VALUES
(1, '2022-05-08 15:00:56', 'QoNdXFZV*PWDbFUWgPUXGLinlR1zPQw==*yykJkbE/Jgv/zK/2ph2kYA==*oyti13xd5oqHpwrdzf/Q3g==', 'dB44U9VUmTV9Vu/L9RcJRq3bukuAcUpc9sVrJQ0xRawCqYK5PvD2SB0IAkNT7eNXSTE4Qv5LHBcGUanYKB/EUgAKmkvpD/f9Q1OskdfFEpYritPQCgYwK1AThQmaSQVFEvSmSf9fkueYs1CpdymWPUNpzvN8cxxtT0nfTFA/lyC9mCgZcv1lhJXVbX3kTVNRkgMhuGQDyick2WgqoPuAOAoK5Gdeb8o1aMiyn1u3BTJM+KEN5oeKrnrNtHVzlxE7UWLGDqjXUqnHbdlcs28T25YRKMy/MTfjCUKX2bbEhub5d6oca8f4HH9nIL8Tm+aYnW8FKsxys4ZDmE/unMWrWp/1OVrCZcfxOzmD2HXK9DqhHvULJP3MgEIpnfS+xQZWriJr1gkON1EJjzS400nv9LVzDaBpkaaPWsUn2RWMGN0aPc8jXi6RZHzfAnTMuD0TXXalKkHe/j8TxnC3E+rCMCGGX77Ny6rjvlMJ8ZrYDey2XKO90mkSle81QpxGT3YCIzWIxXLRsCrconekEIq2Af2Q9hbfRgDXdPz4pVp/QjXAGeW98/3rWoiVN3bAA7WHeM8uKQ7D2xuLDE9+t53EmiCcdiTjqn8=*+U/P5NAe9ozEC2LXy6VgYA==*U9H63tV+SqQiVWqd2S1VMQ==*LUTNPqCWU9jfz4Toknr8yA==', NULL, 'member', 'charles'),
(2, '2022-05-08 15:02:30', '7oUDDMTGlA==*ktk5R+ygVyh/sEwCN6dN2g==*D28ePw1IzEBd/t1BkMPu1A==*pOXf1/R7koDIHtfsnu1RUw==', 'mk/Odx+cvr77d5IHIMUIqJC5ekIL5NQ7tzu9/MxaX1luxTNf3xDcNwjKNaVHihBNrnYszIg+Rh8EIzT9YVRo3tgu0/0hl+eMwRhvf1IlU/alrtPn0RP6epnCDov1iDj/DbqCDtSx3tNl3KnZZxqKli7fJivGfkPQlI5t8aT+0RhXz85H2mxmNOedEpJik86PlPQCL+BFW4ozUYGZQ4uPVhVC6iW0WSNCPkanwas7u3HZtRpVjgRAIGpfcSU3N1x7hVIg+NgOWXud7fhYYGXp03r1AchO3T1A1FrAznuBTUdFrER9s2McXzItKIACPDRvzekAok/XenK1oN7VvJ4YziQATd4naw6fk8C1upNpxaqn3YxezwA7BoKMIIbPFaU5wkwERK7RonBTs8NuFSt2gcmLvDdCaBgeuDoVJnhShu1kvD+uEEqQkZqzgiiM356Ou0LIWXk6rJ5bZa5+SnPj5DbAvp4ei02NIFF2W7s+tS3V/p6caRQg*yhB/9PIqzcD9Dm5ui+rqpg==*EpDFhVXLmzEOH+xyl8mK5A==*ccT9utlxGgNdgYWeIU0X8A==', NULL, 'public', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `logs`
--

CREATE TABLE `logs` (
  `log_id` int(100) NOT NULL,
  `activity` varchar(50) NOT NULL,
  `username` varchar(10) NOT NULL,
  `ip_address` varchar(50) NOT NULL,
  `location` varchar(100) NOT NULL,
  `device` varchar(100) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `logs`
--

INSERT INTO `logs` (`log_id`, `activity`, `username`, `ip_address`, `location`, `device`, `timestamp`) VALUES
(1, 'launched app', 'Guest', '86.106.157.199', 'London', '(\'Linux\', \'Chrome 5.0.307.11\')', '2022-05-08 15:53:23'),
(2, 'accessed public posts section', 'Guest', '86.106.157.199', 'London', '(\'Linux\', \'Chrome 5.0.307.11\')', '2022-05-08 15:53:31'),
(3, 'accessed public posts section', 'Guest', '86.106.157.199', 'London', '(\'Linux\', \'Chrome 5.0.307.11\')', '2022-05-08 15:53:49'),
(4, 'logged in', 'admin', '86.106.157.199', 'London', '(\'Linux\', \'Chrome 5.0.307.11\')', '2022-05-08 15:54:29'),
(5, 'accessed public posts section', 'admin', '86.106.157.199', 'London', '(\'Linux\', \'Chrome 5.0.307.11\')', '2022-05-08 15:54:31'),
(6, 'accessed member posts section', 'admin', '86.106.157.199', 'London', '(\'Linux\', \'Chrome 5.0.307.11\')', '2022-05-08 15:54:32'),
(7, 'accessed personal page section', 'admin', '86.106.157.199', 'London', '(\'Linux\', \'Chrome 5.0.307.11\')', '2022-05-08 15:54:34'),
(8, 'launched app', 'Guest', '86.106.157.199', 'London', '(\'Linux\', \'Chrome 5.0.307.11\')', '2022-05-08 15:56:09'),
(9, 'launched app', 'Guest', '86.106.157.199', 'London', '(\'Linux\', \'Chrome 5.0.307.11\')', '2022-05-08 15:56:46'),
(10, 'launched app', 'Guest', '86.106.157.199', 'London', '(\'Linux\', \'Chrome 5.0.307.11\')', '2022-05-08 15:57:00'),
(11, 'launched app', 'Guest', '86.106.157.199', 'London', '(\'Linux\', \'Chrome 5.0.307.11\')', '2022-05-08 15:57:56'),
(12, 'launched app', 'Guest', '86.106.157.199', 'London', '(\'Linux\', \'Chrome 5.0.307.11\')', '2022-05-08 15:58:22'),
(13, 'launched app', 'Guest', '86.106.157.199', 'London', '(\'Linux\', \'Chrome 5.0.307.11\')', '2022-05-08 15:59:15'),
(14, 'accessed public posts section', 'Guest', '86.106.157.199', 'London', '(\'Linux\', \'Chrome 5.0.307.11\')', '2022-05-08 15:59:22'),
(15, 'launched app', 'Guest', '86.106.157.199', 'London', '(\'Linux\', \'Chrome 5.0.307.11\')', '2022-05-08 16:45:52'),
(16, 'accessed public posts section', 'Guest', '86.106.157.199', 'London', '(\'Linux\', \'Chrome 5.0.307.11\')', '2022-05-08 16:45:57'),
(17, 'launched app', 'Guest', '86.106.157.199', 'London', '(\'Linux\', \'Chrome 5.0.307.11\')', '2022-05-08 16:58:08');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(10) NOT NULL,
  `username` varchar(10) NOT NULL,
  `password` varchar(255) NOT NULL,
  `user_type` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `username`, `password`, `user_type`) VALUES
(1, 'admin', 'n9NZxJETKP6i*OkiZ+Wt9hqJtmZnpn4j6Sg==*x1Ptnnt6Xvi8PRoH51tNLg==*mfeCP3MYH6peKO7XgwcJsQ==', 'admin'),
(2, 'charles', 'xvnU7kFS2RKQpbE=*bmCp/KVPLx+79jFZq9UgMQ==*rPR4muixgenlFuDOIzX4VQ==*83gDjSF5Cbf6lufd+V/q3A==', 'user');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `blog_posts`
--
ALTER TABLE `blog_posts`
  ADD PRIMARY KEY (`blog_id`);

--
-- Indexes for table `logs`
--
ALTER TABLE `logs`
  ADD PRIMARY KEY (`log_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `blog_posts`
--
ALTER TABLE `blog_posts`
  MODIFY `blog_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `logs`
--
ALTER TABLE `logs`
  MODIFY `log_id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
