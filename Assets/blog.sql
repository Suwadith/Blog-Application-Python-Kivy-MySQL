-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 09, 2022 at 01:12 AM
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
  `file_path` text DEFAULT NULL,
  `visibility` varchar(10) NOT NULL,
  `username` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `blog_posts`
--

INSERT INTO `blog_posts` (`blog_id`, `timestamp`, `title`, `body`, `file_path`, `visibility`, `username`) VALUES
(1, '2022-05-08 23:05:03', 'RJBbMKzZmzxGVXLZd9CSSiLg7mc=*Xska0iyT3+sRQ9VANl2tOw==*Je4ACC/d4SnTw6vdr83fXQ==*9ZIkeM/V5PXjjZ2cQIwt8w==', 'v3BBhDALgYYztEhOeDB63mPpOFhY3Uasm4YPW3fOmfsAUiXSCgFQmBnV1nTIX6Myhsg8AlT4Wq8xN/D64OO8SnekQJ00aWVhWsWd3+SGh4BPU7Axy9nmLJbzbxQSrn3YFaNULNb/V2+KrAwwIdMbKskEMt6iDSwrHMZ37vAxXYw/jV+zfodNxBjoDu+TmQ3g/GXyQIzPVjqmXzJzXYs4GGbGS+RQig10MO57HZED4F9Ms3Du0tHDsF7hd4CUggAczi6QmUUpB+QyLJZUEq1qkUqtQXfxL7R3KpQk6f504QO0SeknNB7B7JiMXB8VZ+zYD+cgX3ozjOMYH36zEohAYmLmJtLdJuJNYxJ257UWThoihFZxuwRcnyErloKjRu6rwQOhK+P/2JlQhHOwoh8XKzlqZzUGWdYbHdrKeO9sMaKAPoqVOpyHDOLlBpW1whkX/KSDJEBlR2i9p6bMtAbVTXJZBb+ZmZqLUiiVG+nBlgaojzR4QhdBuX9W+dxtaCohgz7dc/gzwlCg/tw6Th7ZQTnCWI4MxkdqTOQzGcwt3Zctqabl4JBT1yO72Kn1KdOVIti+GRTv9J1zIVlf5mOugnuDKrVZpIGv72ZhPLgTVVDhO1PijSP/elAA+0InBxy/o733NpHQ5oHDORb8vqj201jJ41PgqPBZoQBGV0he0NjKQovdXYop4iIcdwR9vA58LzaUOWw6qrc7z0d8EIaoydwLniotn/m7XtUuymqUQu97NoJq60jwER9tQAJD/d/j1cRKCdVDtd270JP4Iz5pxzaIVHjX9V7L7qQQ5lFyblf1sp0EiN80lXgFi+ofNmEutalOS97eV/Kdovt1lbvWNrRFpB2pOrz1IP1Nrr0OtV44bGPBNLzvusKjKXFpywoGdDl+hN2k6rjrIlq3MA+HQtuMdcVfUyfWfJGP4XfdWjPbXO35qXo5pwkL9gJ1TDRdH4Fx0D4vLuNmM8QYcir4dDCUBuih/GnIvvc6gln79aFdXByOIMrMeSOmKRTp0XXe5uPMJLgWvaDOghBTyffjs0FXqBxPrYXP2FV0ZUuHsEaRH7wNaTkEp2CZ1DmVlJVt0YzRWIsN3Y1rU8L8w63X*I1V7eBpf8KMFqQGv1XGwiw==*Xql18bsiIx5TOfQ/YnQanA==*qVnlw4CFNBrbAVEM52FNNg==', NULL, 'member', 'charles'),
(2, '2022-05-08 23:06:05', 'Vhuq6EGFgbt20lq27zBzBU2xbbXGFrieyL9VDV/Mvg3QU7W82jasgCNxDw==*16Q4xS4o0gmuP5BsgFN7Mw==*z4I0YyfDXkxZbVj1hLX6ww==*MgZ24mYppR77yuSkzzejaQ==', 'kT0D0IfYnXw59aKQgVJDepSltc8weVkR+Y9wDkkiHV7tmxNKURMdxhiUFCAv10x/ySADLIZi/F8JKOSvU/ktntQWdiSvGEzPqTjOtpTXQk+DO+Do7h/BKHqmC/JBL0fJ+TQhz+Kh6rXWNnN6t/Ay/05rfDTK1+xwk6DQb9Tf8gKKd523ZGqMzw8HJ1ohEqveC1OHUVxJ3riqG8Au52SRSkPAqtYBgRHaC9tsyV8ctw63zzRnbEGZN5sMnPd2slZcryqVj2Nt6pvueEJKAWvZWg1fORsbXyBj+zkyQ6DN/IWV3OJFWynQoLNdVmBfM/WVsjSQazwxu0GMQyrl9zpBgdpTaEH+OrASaMcXBO9eMBd7iI7EbpUVD5mMD7NuRVi7xrfZa4AH+jWBZFFIR1wmHXILujLZKydQPvDfhrHN4FXsa/l48SZWP7S5efbJmZlCx7FMdSE7MRz8vbIT9zsQsPWY+rqiC8ea0q/RXpRrbZEMTgcBfTa2ChZ4uWgNejabkuK6Ql2WgXeoyXJqbtlH1ppXcpQl3HeW9rzxWcrfW1xR090Epj/uUYPLmGZ0HR6V796kMPHADf4J8fQGftkwlhkRhlUOHyyGh5ZwpjpmRQZmS71UJ+rEmd98IFJKFCvBosQ0vyjoEoYzLB0x/aRdrxlHV1C77E6NVSkO0WUdtPdnFlKyvvYTioYy7/4uaF0FWz08VzHSvvSqVaBRVJU4nlb/9T2JHc0PO0v7PibJbSXs9Zq5whmHSXGfDJMHxsfUImJlQiwAxIa5SsXwn5wxlone7pB3muftaqOj1Kf7IZZM/3Fb0gH8Edo2JMDmBFYAA20dx+Z90gH8adLJo9ZGVO7jR20gflN7618TlRb5ctLVfxnzA3oB+q2W7aw3ZfPoazWYCqospEd/v8/YvNK60YwjLTD4S1cXAyMc72t4SGMZsVGcvXOleFzu7JgjpCh8uQOfbkEzKcVJnhZTDyGpv2TWWX0=*KMiFU9fNhSR3uM15FNQj+w==*0RbtnckpcgvOvBapAZcLhA==*lllW5qGJm8WTQGL91LtenA==', NULL, 'public', 'admin');

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
  MODIFY `log_id` int(100) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

set global max_allowed_packet=104857600