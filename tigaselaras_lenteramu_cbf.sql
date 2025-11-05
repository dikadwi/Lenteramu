-- phpMyAdmin SQL Dump
-- version 5.2.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Waktu pembuatan: 05 Nov 2025 pada 14.40
-- Versi server: 10.6.23-MariaDB-cll-lve
-- Versi PHP: 8.4.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tigaselaras_lenteramu_cbf`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `ai_recommendations`
--

CREATE TABLE `ai_recommendations` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `recommendation_type` enum('content','difficulty','timing','sequence') NOT NULL,
  `match_score` float NOT NULL,
  `reasoning` text DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `ai_recommendations`
--

INSERT INTO `ai_recommendations` (`id`, `user_id`, `course_id`, `recommendation_type`, `match_score`, `reasoning`, `created_at`, `is_active`) VALUES
(1, 5, 3, 'content', 87, 'Based on learning style and previous performance', '2025-09-04 08:38:30', 1),
(2, 5, 4, 'content', 87, 'Based on learning style and previous performance', '2025-09-04 08:38:30', 1),
(3, 5, 5, 'content', 87, 'Based on learning style and previous performance', '2025-09-04 08:38:30', 1),
(4, 6, 3, 'content', 89, 'Based on learning style and previous performance', '2025-09-04 08:38:30', 1),
(5, 6, 4, 'content', 89, 'Based on learning style and previous performance', '2025-09-04 08:38:30', 1),
(6, 6, 5, 'content', 89, 'Based on learning style and previous performance', '2025-09-04 08:38:30', 1),
(7, 7, 3, 'content', 91, 'Based on learning style and previous performance', '2025-09-04 08:38:30', 1),
(8, 7, 4, 'content', 91, 'Based on learning style and previous performance', '2025-09-04 08:38:30', 1),
(9, 7, 5, 'content', 91, 'Based on learning style and previous performance', '2025-09-04 08:38:30', 1),
(10, 8, 3, 'content', 93, 'Based on learning style and previous performance', '2025-09-04 08:38:30', 1),
(11, 8, 4, 'content', 93, 'Based on learning style and previous performance', '2025-09-04 08:38:30', 1),
(12, 8, 5, 'content', 93, 'Based on learning style and previous performance', '2025-09-04 08:38:30', 1),
(13, 9, 3, 'content', 95, 'Based on learning style and previous performance', '2025-09-04 08:38:30', 1),
(14, 9, 4, 'content', 95, 'Based on learning style and previous performance', '2025-09-04 08:38:30', 1),
(15, 9, 5, 'content', 95, 'Based on learning style and previous performance', '2025-09-04 08:38:30', 1),
(16, 5, 1, 'sequence', 0, '{\"state\": [\"kinesthetic\", \"medium\", \"intrinsic\", \"medium\"], \"action\": \"1\"}', '2025-09-18 06:57:00', 1),
(17, 5, 2, 'sequence', 0, '{\"state\": [\"kinesthetic\", \"medium\", \"intrinsic\", \"medium\"], \"action\": \"2\"}', '2025-09-18 06:57:00', 1),
(18, 5, 3, 'sequence', 0, '{\"state\": [\"kinesthetic\", \"medium\", \"intrinsic\", \"medium\"], \"action\": \"3\"}', '2025-09-18 06:57:00', 1),
(19, 5, 4, 'sequence', 0.999996, '{\"state\": [\"kinesthetic\", \"medium\", \"intrinsic\", \"medium\"], \"action\": \"4\"}', '2025-09-18 06:57:00', 1),
(20, 6, 1, 'sequence', 0, '{\"state\": [\"visual\", \"medium\", \"intrinsic\", \"medium\"], \"action\": \"1\"}', '2025-09-18 06:57:00', 1),
(21, 6, 2, 'sequence', 0, '{\"state\": [\"visual\", \"medium\", \"intrinsic\", \"medium\"], \"action\": \"2\"}', '2025-09-18 06:57:00', 1),
(22, 6, 3, 'sequence', 0, '{\"state\": [\"visual\", \"medium\", \"intrinsic\", \"medium\"], \"action\": \"3\"}', '2025-09-18 06:57:00', 1),
(23, 6, 4, 'sequence', 0.999996, '{\"state\": [\"visual\", \"medium\", \"intrinsic\", \"medium\"], \"action\": \"4\"}', '2025-09-18 06:57:00', 1),
(24, 7, 1, 'sequence', 0, '{\"state\": [\"auditory\", \"medium\", \"intrinsic\", \"medium\"], \"action\": \"1\"}', '2025-09-18 06:57:00', 1),
(25, 7, 2, 'sequence', 0, '{\"state\": [\"auditory\", \"medium\", \"intrinsic\", \"medium\"], \"action\": \"2\"}', '2025-09-18 06:57:00', 1),
(26, 7, 3, 'sequence', 0, '{\"state\": [\"auditory\", \"medium\", \"intrinsic\", \"medium\"], \"action\": \"3\"}', '2025-09-18 06:57:00', 1),
(27, 7, 4, 'sequence', 0.999996, '{\"state\": [\"auditory\", \"medium\", \"intrinsic\", \"medium\"], \"action\": \"4\"}', '2025-09-18 06:57:00', 1),
(28, 8, 1, 'sequence', 0, '{\"state\": [\"kinesthetic\", \"medium\", \"intrinsic\", \"medium\"], \"action\": \"1\"}', '2025-09-18 06:57:00', 1),
(29, 8, 2, 'sequence', 0, '{\"state\": [\"kinesthetic\", \"medium\", \"intrinsic\", \"medium\"], \"action\": \"2\"}', '2025-09-18 06:57:00', 1),
(30, 8, 3, 'sequence', 0, '{\"state\": [\"kinesthetic\", \"medium\", \"intrinsic\", \"medium\"], \"action\": \"3\"}', '2025-09-18 06:57:00', 1),
(31, 8, 4, 'sequence', 0.999996, '{\"state\": [\"kinesthetic\", \"medium\", \"intrinsic\", \"medium\"], \"action\": \"4\"}', '2025-09-18 06:57:00', 1),
(32, 9, 1, 'sequence', 8.50956, '{\"state\": [\"visual\", \"medium\", \"intrinsic\", \"medium\"], \"action\": \"1\"}', '2025-09-18 06:57:00', 1),
(33, 9, 2, 'sequence', 8.50956, '{\"state\": [\"visual\", \"medium\", \"intrinsic\", \"medium\"], \"action\": \"2\"}', '2025-09-18 06:57:00', 1),
(34, 9, 3, 'sequence', 9.50956, '{\"state\": [\"visual\", \"medium\", \"intrinsic\", \"medium\"], \"action\": \"3\"}', '2025-09-18 06:57:00', 1),
(35, 9, 4, 'sequence', 9.51446, '{\"state\": [\"visual\", \"medium\", \"intrinsic\", \"medium\"], \"action\": \"4\"}', '2025-09-18 06:57:00', 1),
(36, 10, 7, 'sequence', 9.61478, '{\"state\": [\"visual\", \"medium\", \"intrinsic\", \"medium\"], \"action\": \"7\"}', '2025-09-18 06:57:00', 1),
(37, 10, 8, 'sequence', 9.61548, '{\"state\": [\"visual\", \"medium\", \"intrinsic\", \"medium\"], \"action\": \"8\"}', '2025-09-18 06:57:00', 1),
(38, 10, 9, 'sequence', 9.61548, '{\"state\": [\"visual\", \"medium\", \"intrinsic\", \"medium\"], \"action\": \"9\"}', '2025-09-18 06:57:00', 1),
(39, 10, 10, 'sequence', 9.61619, '{\"state\": [\"visual\", \"medium\", \"intrinsic\", \"medium\"], \"action\": \"10\"}', '2025-09-18 06:57:00', 1),
(40, 10, 11, 'sequence', 9.61689, '{\"state\": [\"visual\", \"medium\", \"intrinsic\", \"medium\"], \"action\": \"11\"}', '2025-09-18 06:57:00', 1),
(41, 10, 12, 'sequence', 9.61757, '{\"state\": [\"visual\", \"medium\", \"intrinsic\", \"medium\"], \"action\": \"12\"}', '2025-09-18 06:57:00', 1),
(42, 10, 13, 'sequence', 9.61825, '{\"state\": [\"visual\", \"medium\", \"intrinsic\", \"medium\"], \"action\": \"13\"}', '2025-09-18 06:57:00', 1);

-- --------------------------------------------------------

--
-- Struktur dari tabel `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('add_reset_password_fields');

-- --------------------------------------------------------

--
-- Struktur dari tabel `badges`
--

CREATE TABLE `badges` (
  `id_badges` int(100) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `point` int(11) NOT NULL,
  `detail` text NOT NULL,
  `keterangan` varchar(150) NOT NULL,
  `badges` varchar(255) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `badges`
--

INSERT INTO `badges` (`id_badges`, `nama`, `point`, `detail`, `keterangan`, `badges`, `created_at`, `updated_at`) VALUES
(1, 'Negative', -1000, 'Negative Badges', 'Badges diberikan ketika poin negatif', '1740973961_f3e4f3e97c34d4e638b7.png', '2025-03-03 03:52:41', '2025-03-02 20:52:41'),
(2, 'Master', 30, 'Badges Pemula', 'Badges diberikan saat pertama kali', '1740973968_f3c8e53db523ccae6a48.png', '2025-03-25 12:33:20', '2025-03-25 05:33:20'),
(3, 'Silver', 50, 'Badges Pemain', 'Badges diberikan saat memperoleh point 50', '1740973975_58a8422172e0cef26758.png', '2025-03-03 03:52:55', '2025-03-02 20:52:55'),
(4, 'Gold', 100, 'Badges Pemain', 'Badges diberikan saat memperoleh point 100', '1740973984_2557996eac0391b35944.png', '2025-03-03 03:53:04', '2025-03-02 20:53:04'),
(5, 'Platinum', 150, 'Badges Pemain', 'Badges diberikan saat memperoleh point 150', '1740973998_263dd9caed3d9e182fae.png', '2025-03-03 03:53:18', '2025-03-02 20:53:18'),
(6, 'Diamond', 200, 'Badges Super', 'Badges diberikan saat memperoleh point 200', '1740974009_cb633a5b0226f8415959.png', '2025-03-03 03:53:29', '2025-03-02 20:53:29'),
(7, 'King', 250, 'Badges Superior', 'Badges diberikan saat memperoleh point 250', '1740974021_3f504f437a03db99d11c.png', '2025-03-03 03:53:41', '2025-03-02 20:53:41');

-- --------------------------------------------------------

--
-- Struktur dari tabel `courses`
--

CREATE TABLE `courses` (
  `id` int(11) NOT NULL,
  `title` varchar(200) NOT NULL,
  `description` text DEFAULT NULL,
  `subject_id` int(11) NOT NULL,
  `difficulty_level` enum('beginner','intermediate','advanced') DEFAULT NULL,
  `content_type` enum('video','article','quiz','practice') NOT NULL,
  `content_url` varchar(255) DEFAULT NULL,
  `duration_minutes` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `courses`
--

INSERT INTO `courses` (`id`, `title`, `description`, `subject_id`, `difficulty_level`, `content_type`, `content_url`, `duration_minutes`, `created_at`, `is_active`) VALUES
(1, 'Aljabar Linear', 'Materi pembelajaran Aljabar Linear', 1, 'intermediate', 'video', '/content/aljabar_linear', 45, '2025-09-04 08:38:30', 1),
(2, 'Kalkulus Diferensial', 'Materi pembelajaran Kalkulus Diferensial', 1, 'advanced', 'article', '/content/kalkulus_diferensial', 60, '2025-09-04 08:38:30', 1),
(3, 'Geometri Ruang', 'Materi pembelajaran Geometri Ruang', 1, 'beginner', 'practice', '/content/geometri_ruang', 30, '2025-09-04 08:38:30', 1),
(4, 'Mekanika Newton', 'Materi pembelajaran Mekanika Newton', 2, 'intermediate', 'video', '/content/mekanika_newton', 50, '2025-09-04 08:38:30', 1),
(5, 'Gelombang dan Optik', 'Materi pembelajaran Gelombang dan Optik', 2, 'advanced', 'quiz', '/content/gelombang_dan_optik', 25, '2025-09-04 08:38:30', 1),
(6, 'Ikatan Kimia', 'Materi pembelajaran Ikatan Kimia', 3, 'beginner', 'video', '/content/ikatan_kimia', 40, '2025-09-04 08:38:30', 1),
(7, 'Persamaan Linear', 'Materi tentang Persamaan Linear', 6, 'beginner', 'article', NULL, 0, '2025-09-18 06:48:46', 1),
(8, 'Hukum Newton', 'Materi tentang Hukum Newton', 6, 'beginner', 'video', NULL, 0, '2025-09-18 06:48:46', 1),
(9, 'Reaksi Kimia', 'Materi tentang Reaksi Kimia', 6, 'beginner', 'article', NULL, 0, '2025-09-18 06:48:46', 1),
(10, 'Tugas Matematika 1', 'Tugas latihan matematika', 6, 'beginner', 'practice', NULL, 0, '2025-09-18 06:48:46', 1),
(11, 'Tugas Fisika 1', 'Tugas latihan fisika', 6, 'beginner', 'practice', NULL, 0, '2025-09-18 06:48:46', 1),
(12, 'Kuis Matematika', 'Kuis matematika dasar', 6, 'beginner', 'quiz', NULL, 0, '2025-09-18 06:48:46', 1),
(13, 'Kuis Fisika', 'Kuis fisika dasar', 6, 'beginner', 'quiz', NULL, 0, '2025-09-18 06:48:46', 1);

-- --------------------------------------------------------

--
-- Struktur dari tabel `learning_activities`
--

CREATE TABLE `learning_activities` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `activity_type` enum('view','complete','quiz_attempt','practice') NOT NULL,
  `start_time` datetime DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `score` float DEFAULT NULL,
  `completed` tinyint(1) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `learning_activities`
--

INSERT INTO `learning_activities` (`id`, `user_id`, `course_id`, `activity_type`, `start_time`, `end_time`, `score`, `completed`, `created_at`) VALUES
(1, 10, 7, 'complete', '2025-09-08 06:48:46', '2025-09-09 06:48:46', 85, 1, '2025-09-18 06:48:46'),
(2, 10, 8, 'complete', '2025-09-09 06:48:46', '2025-09-10 06:48:46', 85, 1, '2025-09-18 06:48:46'),
(3, 10, 9, 'complete', '2025-09-10 06:48:46', '2025-09-11 06:48:46', 85, 1, '2025-09-18 06:48:46'),
(4, 10, 10, 'complete', '2025-09-11 06:48:46', '2025-09-12 06:48:46', 85, 1, '2025-09-18 06:48:46'),
(5, 10, 11, 'complete', '2025-09-12 06:48:46', '2025-09-13 06:48:46', 85, 1, '2025-09-18 06:48:46'),
(6, 10, 12, 'complete', '2025-09-13 06:48:46', '2025-09-14 06:48:46', 85, 1, '2025-09-18 06:48:46'),
(7, 10, 13, 'complete', '2025-09-14 06:48:46', '2025-09-15 06:48:46', 85, 1, '2025-09-18 06:48:46');

-- --------------------------------------------------------

--
-- Struktur dari tabel `student_profiles`
--

CREATE TABLE `student_profiles` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `student_id` varchar(20) DEFAULT NULL,
  `school_name` varchar(100) DEFAULT NULL,
  `learning_style` enum('visual','auditory','kinesthetic','reading') DEFAULT NULL,
  `learning_pace` enum('slow','normal','fast') DEFAULT NULL,
  `preferred_subjects` text DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `mslq_level` enum('high','medium','low') DEFAULT NULL,
  `ams_type` enum('intrinsic','extrinsic','achievement','amotivation') DEFAULT NULL,
  `engagement_level` enum('high','medium','low') DEFAULT NULL,
  `verification_token` varchar(100) DEFAULT NULL,
  `verification_sent_at` datetime DEFAULT NULL,
  `verified_at` datetime DEFAULT NULL,
  `kelas` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `student_profiles`
--

INSERT INTO `student_profiles` (`id`, `user_id`, `student_id`, `school_name`, `learning_style`, `learning_pace`, `preferred_subjects`, `created_at`, `mslq_level`, `ams_type`, `engagement_level`, `verification_token`, `verification_sent_at`, `verified_at`, `kelas`) VALUES
(1, 5, 'STD0005', 'SMA Negeri 1 Jakarta', 'kinesthetic', 'slow', '[\"MTK\", \"FIS\"]', '2025-09-04 08:38:30', NULL, NULL, NULL, NULL, NULL, NULL, ''),
(2, 6, 'STD0006', 'SMA Negeri 1 Jakarta', 'visual', 'normal', '[\"MTK\", \"FIS\"]', '2025-09-04 08:38:30', NULL, NULL, NULL, NULL, NULL, NULL, ''),
(3, 7, 'STD0007', 'SMA Negeri 1 Jakarta', 'auditory', 'fast', '[\"MTK\", \"FIS\"]', '2025-09-04 08:38:30', NULL, NULL, NULL, NULL, NULL, NULL, ''),
(4, 8, 'STD0008', 'SMA Negeri 1 Jakarta', 'kinesthetic', 'slow', '[\"MTK\", \"FIS\"]', '2025-09-04 08:38:30', NULL, NULL, NULL, NULL, NULL, NULL, ''),
(5, 9, 'STD0009', 'SMA Negeri 1 Jakarta', 'visual', 'normal', '[\"MTK\", \"FIS\"]', '2025-09-04 08:38:30', NULL, NULL, NULL, NULL, NULL, NULL, ''),
(6, 1, 'DEMO1', 'SMA Demo', 'visual', 'normal', '[\"Matematika\", \"Fisika\"]', '2025-09-18 06:20:30', 'medium', 'intrinsic', 'medium', NULL, NULL, NULL, ''),
(7, 10, 'DEMO10', 'SMA Demo', 'visual', 'normal', '[\"Matematika\", \"Fisika\"]', '2025-08-19 06:46:51', 'medium', 'intrinsic', 'medium', NULL, NULL, NULL, '');

-- --------------------------------------------------------

--
-- Struktur dari tabel `student_progress`
--

CREATE TABLE `student_progress` (
  `id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `progress_percentage` float DEFAULT NULL,
  `last_accessed` datetime DEFAULT NULL,
  `completion_date` datetime DEFAULT NULL,
  `grade` varchar(5) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `student_progress`
--

INSERT INTO `student_progress` (`id`, `student_id`, `course_id`, `progress_percentage`, `last_accessed`, `completion_date`, `grade`, `created_at`, `updated_at`) VALUES
(1, 1, 1, 30, '2025-09-04 08:38:30', NULL, 'A', '2025-09-04 08:38:30', '2025-09-04 08:38:30'),
(2, 1, 2, 55, '2025-09-04 08:38:30', NULL, 'B', '2025-09-04 08:38:30', '2025-09-04 08:38:30'),
(3, 1, 3, 80, '2025-09-04 08:38:30', NULL, 'A', '2025-09-04 08:38:30', '2025-09-04 08:38:30'),
(4, 1, 4, 100, '2025-09-04 08:38:30', NULL, NULL, '2025-09-04 08:38:30', '2025-09-04 08:38:30'),
(5, 2, 1, 35, '2025-09-04 08:38:30', NULL, 'A', '2025-09-04 08:38:30', '2025-09-04 08:38:30'),
(6, 2, 2, 60, '2025-09-04 08:38:30', NULL, 'B', '2025-09-04 08:38:30', '2025-09-04 08:38:30'),
(7, 2, 3, 85, '2025-09-04 08:38:30', NULL, 'A', '2025-09-04 08:38:30', '2025-09-04 08:38:30'),
(8, 2, 4, 100, '2025-09-04 08:38:30', NULL, NULL, '2025-09-04 08:38:30', '2025-09-04 08:38:30'),
(9, 3, 1, 40, '2025-09-04 08:38:30', NULL, 'A', '2025-09-04 08:38:30', '2025-09-04 08:38:30'),
(10, 3, 2, 65, '2025-09-04 08:38:30', NULL, 'B', '2025-09-04 08:38:30', '2025-09-04 08:38:30'),
(11, 3, 3, 90, '2025-09-04 08:38:30', NULL, 'A', '2025-09-04 08:38:30', '2025-09-04 08:38:30'),
(12, 3, 4, 100, '2025-09-04 08:38:30', NULL, NULL, '2025-09-04 08:38:30', '2025-09-04 08:38:30'),
(13, 4, 1, 45, '2025-09-04 08:38:30', NULL, 'A', '2025-09-04 08:38:30', '2025-09-04 08:38:30'),
(14, 4, 2, 70, '2025-09-04 08:38:30', NULL, 'B', '2025-09-04 08:38:30', '2025-09-04 08:38:30'),
(15, 4, 3, 95, '2025-09-04 08:38:30', NULL, 'A', '2025-09-04 08:38:30', '2025-09-04 08:38:30'),
(16, 4, 4, 100, '2025-09-04 08:38:30', NULL, NULL, '2025-09-04 08:38:30', '2025-09-04 08:38:30'),
(17, 5, 1, 50, '2025-09-04 08:38:30', NULL, 'A', '2025-09-04 08:38:30', '2025-09-04 08:38:30'),
(18, 5, 2, 75, '2025-09-04 08:38:30', NULL, 'B', '2025-09-04 08:38:30', '2025-09-04 08:38:30'),
(19, 5, 3, 100, '2025-09-04 08:38:30', NULL, 'A', '2025-09-04 08:38:30', '2025-09-04 08:38:30'),
(20, 5, 4, 100, '2025-09-04 08:38:30', NULL, NULL, '2025-09-04 08:38:30', '2025-09-04 08:38:30'),
(21, 7, 7, 100, '2025-09-18 06:48:46', NULL, '85', '2025-09-08 06:48:46', '2025-09-18 06:48:46'),
(22, 7, 8, 100, '2025-09-18 06:48:46', NULL, '85', '2025-09-08 06:48:46', '2025-09-18 06:48:46'),
(23, 7, 9, 100, '2025-09-18 06:48:46', NULL, '85', '2025-09-08 06:48:46', '2025-09-18 06:48:46'),
(24, 7, 10, 100, '2025-09-18 06:48:46', NULL, '85', '2025-09-08 06:48:46', '2025-09-18 06:48:46'),
(25, 7, 11, 100, '2025-09-18 06:48:46', NULL, '85', '2025-09-08 06:48:46', '2025-09-18 06:48:46'),
(26, 7, 12, 100, '2025-09-18 06:48:46', NULL, '85', '2025-09-08 06:48:46', '2025-09-18 06:48:46'),
(27, 7, 13, 100, '2025-09-18 06:48:46', NULL, '85', '2025-09-08 06:48:46', '2025-09-18 06:48:46');

-- --------------------------------------------------------

--
-- Struktur dari tabel `subjects`
--

CREATE TABLE `subjects` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `code` varchar(10) NOT NULL,
  `description` text DEFAULT NULL,
  `grade_level` varchar(10) NOT NULL,
  `created_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `subjects`
--

INSERT INTO `subjects` (`id`, `name`, `code`, `description`, `grade_level`, `created_at`) VALUES
(1, 'Matematika', 'MTK', 'Mata pelajaran matematika', 'SMA', '2025-09-04 08:38:29'),
(2, 'Fisika', 'FIS', 'Mata pelajaran fisika', 'SMA', '2025-09-04 08:38:29'),
(3, 'Kimia', 'KIM', 'Mata pelajaran kimia', 'SMA', '2025-09-04 08:38:29'),
(4, 'Biologi', 'BIO', 'Mata pelajaran biologi', 'SMA', '2025-09-04 08:38:29'),
(5, 'Bahasa Indonesia', 'BIN', 'Mata pelajaran bahasa Indonesia', 'SMA', '2025-09-04 08:38:29'),
(6, 'Matematika', 'MAT', 'Matematika Dasar', 'XII', '2025-09-18 06:48:46');

-- --------------------------------------------------------

--
-- Struktur dari tabel `system_metrics`
--

CREATE TABLE `system_metrics` (
  `id` int(11) NOT NULL,
  `metric_name` varchar(100) NOT NULL,
  `metric_value` float NOT NULL,
  `metric_unit` varchar(20) DEFAULT NULL,
  `recorded_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `system_metrics`
--

INSERT INTO `system_metrics` (`id`, `metric_name`, `metric_value`, `metric_unit`, `recorded_at`) VALUES
(1, 'active_users', 234, 'count', '2025-09-04 08:38:30'),
(2, 'cpu_usage', 45.2, 'percentage', '2025-09-04 08:38:30'),
(3, 'memory_usage', 68.5, 'percentage', '2025-09-04 08:38:30'),
(4, 'response_time', 120, 'ms', '2025-09-04 08:38:30'),
(5, 'model_accuracy', 94.2, 'percentage', '2025-09-04 08:38:30');

-- --------------------------------------------------------

--
-- Struktur dari tabel `teacher_profiles`
--

CREATE TABLE `teacher_profiles` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `school_name` varchar(100) DEFAULT NULL,
  `subjects` text DEFAULT NULL,
  `experience_years` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `verification_token` varchar(100) DEFAULT NULL,
  `verification_sent_at` datetime DEFAULT NULL,
  `verified_at` datetime DEFAULT NULL,
  `nip` varchar(18) NOT NULL,
  `mata_pelajaran` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `teacher_profiles`
--

INSERT INTO `teacher_profiles` (`id`, `user_id`, `school_name`, `subjects`, `experience_years`, `created_at`, `verification_token`, `verification_sent_at`, `verified_at`, `nip`, `mata_pelajaran`) VALUES
(1, 2, 'SMA Negeri 1 Jakarta', '[\"MTK\"]', 5, '2025-09-04 08:38:29', NULL, NULL, NULL, '', ''),
(2, 3, 'SMA Negeri 1 Jakarta', '[\"FIS\"]', 5, '2025-09-04 08:38:29', NULL, NULL, NULL, '', ''),
(3, 4, 'SMA Negeri 1 Jakarta', '[\"KIM\"]', 5, '2025-09-04 08:38:29', NULL, NULL, NULL, '', '');

-- --------------------------------------------------------

--
-- Struktur dari tabel `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(80) NOT NULL,
  `email` varchar(120) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `full_name` varchar(100) NOT NULL,
  `role` enum('siswa','guru','admin') NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT NULL,
  `reset_token` varchar(100) DEFAULT NULL,
  `reset_token_sent_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `users`
--

INSERT INTO `users` (`id`, `username`, `email`, `password_hash`, `full_name`, `role`, `created_at`, `is_active`, `reset_token`, `reset_token_sent_at`) VALUES
(1, 'admin', 'admin@lenteramu.id', '$2b$12$I.GQBaFVqPAIampawaGMEOKLKfo7Yf9k22XqMtpxtk5LBOQ7ySupO', 'Administrator', 'admin', '2025-09-04 08:38:29', 1, NULL, NULL),
(2, 'guru_matematika', 'guru.mtk@lenteramu.id', '$2b$12$41DWJsZazr3vInm.n.7ZsekcTZWY4I6AvIZ0qGFi3Fl5hnEVHgI4W', 'Dr. Siti Nurhaliza', 'guru', '2025-09-04 08:38:29', 1, NULL, NULL),
(3, 'guru_fisika', 'guru.fis@lenteramu.id', '$2b$12$s17qTqkHVsQ3s6oZjvB0VeHxTd0MWqzCRlr3ATomMjgNqzfag.vJ.', 'Prof. Ahmad Dahlan', 'guru', '2025-09-04 08:38:29', 1, NULL, NULL),
(4, 'guru_kimia', 'guru.kim@lenteramu.id', '$2b$12$e3zFwyzLg0uW164242UeeeAQ7CUky95cEBtcWK7M/ZZ9uL1q49BCG', 'Dra. Maya Sari', 'guru', '2025-09-04 08:38:29', 1, NULL, NULL),
(5, 'ahmad_rizki', 'ahmad.rizki@student.id', '$2b$12$l2zm/V/lpBBMN6XDEOgxpOM1.5rlidOzSHckz0GA2yuoqLBruaIgi', 'Ahmad Rizki Pratama', 'siswa', '2025-09-04 08:38:29', 1, NULL, NULL),
(6, 'siti_aisyah', 'siti.aisyah@student.id', '$2b$12$zRRQwPdCDhTXS/hBhMH6u.DgUx5F/OS/6VEzcd0hZSBOI6xPc0xvq', 'Siti Aisyah Putri', 'siswa', '2025-09-04 08:38:30', 1, NULL, NULL),
(7, 'budi_santoso', 'budi.santoso@student.id', '$2b$12$11uqDnNMr0VwwrvKQnoVn./WeNMVwbvgNi1vkzgIa7bQqk7qnwxlW', 'Budi Santoso', 'siswa', '2025-09-04 08:38:30', 1, NULL, NULL),
(8, 'maya_indira', 'maya.indira@student.id', '$2b$12$c7M6QPbScgL6aDmOFyht..v4Jwyq3B64PUfA09gGBMMEJfD4XwwJ.', 'Maya Indira Sari', 'siswa', '2025-09-04 08:38:30', 1, NULL, NULL),
(9, 'rizki_fadillah', 'rizki.fadillah@student.id', '$2b$12$T6jUvmm/etJvfvbDzbAygedLfw1RMRfQq0C7VFybCkRbSdKUUp0gW', 'Rizki Fadillah', 'siswa', '2025-09-04 08:38:30', 1, NULL, NULL),
(10, 'demo_student', 'demo_student@lenteramu.id', '$2b$12$7NK3kd7y98aLICEfP9TfOeZrulI/aMBQ5rztTUUGHPJ9GNpUEZyoG', 'Demo Siswa', 'siswa', '2025-09-18 06:46:51', 1, NULL, NULL);

-- --------------------------------------------------------

--
-- Struktur dari tabel `user_feedback`
--

CREATE TABLE `user_feedback` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `feedback_type` enum('system','content','feature','bug') NOT NULL,
  `rating` int(11) DEFAULT NULL,
  `comments` text DEFAULT NULL,
  `created_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `user_feedback`
--

INSERT INTO `user_feedback` (`id`, `user_id`, `feedback_type`, `rating`, `comments`, `created_at`) VALUES
(1, 5, 'system', 5, 'Sistem sangat membantu dalam pembelajaran', '2025-09-04 08:38:30'),
(2, 6, 'system', 5, 'Sistem sangat membantu dalam pembelajaran', '2025-09-04 08:38:30'),
(3, 7, 'system', 5, 'Sistem sangat membantu dalam pembelajaran', '2025-09-04 08:38:30');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `ai_recommendations`
--
ALTER TABLE `ai_recommendations`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `course_id` (`course_id`);

--
-- Indeks untuk tabel `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indeks untuk tabel `badges`
--
ALTER TABLE `badges`
  ADD PRIMARY KEY (`id_badges`);

--
-- Indeks untuk tabel `courses`
--
ALTER TABLE `courses`
  ADD PRIMARY KEY (`id`),
  ADD KEY `subject_id` (`subject_id`);

--
-- Indeks untuk tabel `learning_activities`
--
ALTER TABLE `learning_activities`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `course_id` (`course_id`);

--
-- Indeks untuk tabel `student_profiles`
--
ALTER TABLE `student_profiles`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `student_id` (`student_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indeks untuk tabel `student_progress`
--
ALTER TABLE `student_progress`
  ADD PRIMARY KEY (`id`),
  ADD KEY `student_id` (`student_id`),
  ADD KEY `course_id` (`course_id`);

--
-- Indeks untuk tabel `subjects`
--
ALTER TABLE `subjects`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `code` (`code`);

--
-- Indeks untuk tabel `system_metrics`
--
ALTER TABLE `system_metrics`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `teacher_profiles`
--
ALTER TABLE `teacher_profiles`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indeks untuk tabel `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `uq_users_reset_token` (`reset_token`);

--
-- Indeks untuk tabel `user_feedback`
--
ALTER TABLE `user_feedback`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `ai_recommendations`
--
ALTER TABLE `ai_recommendations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT untuk tabel `badges`
--
ALTER TABLE `badges`
  MODIFY `id_badges` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT untuk tabel `courses`
--
ALTER TABLE `courses`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT untuk tabel `learning_activities`
--
ALTER TABLE `learning_activities`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT untuk tabel `student_profiles`
--
ALTER TABLE `student_profiles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT untuk tabel `student_progress`
--
ALTER TABLE `student_progress`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT untuk tabel `subjects`
--
ALTER TABLE `subjects`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT untuk tabel `system_metrics`
--
ALTER TABLE `system_metrics`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT untuk tabel `teacher_profiles`
--
ALTER TABLE `teacher_profiles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT untuk tabel `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT untuk tabel `user_feedback`
--
ALTER TABLE `user_feedback`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `ai_recommendations`
--
ALTER TABLE `ai_recommendations`
  ADD CONSTRAINT `ai_recommendations_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `ai_recommendations_ibfk_2` FOREIGN KEY (`course_id`) REFERENCES `courses` (`id`);

--
-- Ketidakleluasaan untuk tabel `courses`
--
ALTER TABLE `courses`
  ADD CONSTRAINT `courses_ibfk_1` FOREIGN KEY (`subject_id`) REFERENCES `subjects` (`id`);

--
-- Ketidakleluasaan untuk tabel `learning_activities`
--
ALTER TABLE `learning_activities`
  ADD CONSTRAINT `learning_activities_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `learning_activities_ibfk_2` FOREIGN KEY (`course_id`) REFERENCES `courses` (`id`);

--
-- Ketidakleluasaan untuk tabel `student_profiles`
--
ALTER TABLE `student_profiles`
  ADD CONSTRAINT `student_profiles_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Ketidakleluasaan untuk tabel `student_progress`
--
ALTER TABLE `student_progress`
  ADD CONSTRAINT `student_progress_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `student_profiles` (`id`),
  ADD CONSTRAINT `student_progress_ibfk_2` FOREIGN KEY (`course_id`) REFERENCES `courses` (`id`);

--
-- Ketidakleluasaan untuk tabel `teacher_profiles`
--
ALTER TABLE `teacher_profiles`
  ADD CONSTRAINT `teacher_profiles_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Ketidakleluasaan untuk tabel `user_feedback`
--
ALTER TABLE `user_feedback`
  ADD CONSTRAINT `user_feedback_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
