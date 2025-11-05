-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Waktu pembuatan: 05 Nov 2025 pada 08.02
-- Versi server: 10.4.28-MariaDB
-- Versi PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `poin_market`
--

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

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `badges`
--
ALTER TABLE `badges`
  ADD PRIMARY KEY (`id_badges`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `badges`
--
ALTER TABLE `badges`
  MODIFY `id_badges` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
