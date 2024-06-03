-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Gép: 127.0.0.1
-- Létrehozás ideje: 2022. Nov 26. 02:33
-- Kiszolgáló verziója: 10.4.25-MariaDB
-- PHP verzió: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Adatbázis: `musorujsag`
--

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `jatszik`
--

CREATE TABLE `jatszik` (
  `musorid` int(4) NOT NULL,
  `szereploid` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- A tábla adatainak kiíratása `jatszik`
--

INSERT INTO `jatszik` (`musorid`, `szereploid`) VALUES
(1, 12),
(1, 30),
(2, 30),
(3, 30),
(4, 30),
(5, 30),
(6, 30),
(12, 1),
(13, 1),
(17, 2),
(17, 3),
(17, 4),
(17, 5),
(17, 6),
(17, 7),
(17, 8),
(17, 9),
(17, 10),
(18, 11),
(18, 12),
(18, 13),
(18, 14),
(18, 15),
(18, 16),
(18, 17),
(18, 18),
(18, 19),
(33, 20),
(33, 21),
(33, 22),
(33, 23),
(33, 24),
(33, 25),
(33, 26),
(33, 27),
(33, 28),
(34, 29),
(34, 30),
(35, 31),
(35, 32),
(35, 33),
(35, 34),
(35, 35),
(35, 36),
(35, 37),
(35, 38),
(35, 39),
(40, 40),
(40, 41),
(40, 42),
(40, 43),
(40, 44),
(40, 45),
(40, 46),
(40, 47),
(41, 48),
(41, 49),
(41, 50),
(41, 51),
(41, 52),
(41, 53),
(41, 54),
(41, 55),
(41, 56),
(42, 57),
(42, 58),
(42, 59),
(42, 60),
(42, 61),
(42, 62),
(42, 63),
(43, 64),
(43, 65),
(43, 66),
(43, 67),
(43, 68),
(43, 69),
(45, 30),
(57, 30),
(57, 70),
(57, 71),
(57, 72),
(57, 73),
(57, 74),
(57, 75),
(57, 76),
(57, 77),
(59, 78),
(60, 79),
(60, 80),
(60, 81),
(60, 82),
(60, 83),
(60, 84),
(60, 85),
(60, 86),
(61, 87),
(61, 88),
(61, 89),
(61, 90),
(61, 91),
(61, 92),
(61, 93),
(61, 94),
(61, 95),
(62, 40),
(62, 96),
(62, 97),
(62, 98),
(62, 99),
(62, 100),
(62, 101),
(62, 102),
(63, 103),
(63, 104),
(63, 105),
(63, 106),
(63, 107),
(63, 108),
(63, 109),
(63, 110),
(63, 111),
(64, 112),
(64, 113),
(64, 114),
(64, 115),
(64, 116),
(64, 117),
(64, 118),
(64, 119),
(64, 120),
(67, 30),
(69, 999),
(77, 121),
(77, 122),
(77, 123),
(77, 124),
(77, 125),
(77, 126),
(77, 127),
(77, 128),
(77, 129),
(79, 130),
(79, 131),
(79, 132),
(79, 133),
(79, 134),
(79, 135),
(79, 136),
(80, 137),
(80, 138),
(80, 139),
(83, 30),
(87, 140),
(87, 141),
(87, 142),
(88, 143),
(88, 144),
(88, 145),
(88, 146),
(88, 147),
(88, 148);

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `kozvetit`
--

CREATE TABLE `kozvetit` (
  `tv_csatornaid` int(4) NOT NULL,
  `m_musorid` int(4) NOT NULL,
  `idopont` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- A tábla adatainak kiíratása `kozvetit`
--

INSERT INTO `kozvetit` (`tv_csatornaid`, `m_musorid`, `idopont`) VALUES
(1, 1, '00:00:00'),
(1, 2, '00:20:00'),
(1, 2, '01:05:00'),
(1, 2, '02:00:00'),
(1, 2, '03:00:00'),
(1, 2, '04:00:00'),
(1, 2, '05:00:00'),
(1, 3, '06:00:00'),
(1, 3, '07:00:00'),
(1, 3, '08:00:00'),
(1, 3, '09:00:00'),
(1, 3, '10:00:00'),
(1, 3, '11:00:00'),
(1, 3, '12:01:00'),
(1, 3, '13:00:00'),
(1, 3, '14:00:00'),
(1, 3, '14:15:00'),
(1, 3, '15:00:00'),
(1, 3, '16:00:00'),
(1, 3, '17:00:00'),
(1, 3, '18:00:00'),
(1, 3, '19:30:00'),
(1, 3, '21:00:00'),
(1, 3, '22:00:00'),
(1, 3, '23:00:00'),
(3, 3, '06:35:00'),
(5, 3, '02:00:00'),
(7, 3, '07:00:00'),
(1, 4, '06:30:00'),
(1, 4, '18:25:00'),
(3, 4, '07:05:00'),
(4, 4, '07:05:00'),
(4, 4, '10:05:00'),
(4, 4, '13:05:00'),
(1, 5, '03:30:00'),
(1, 5, '07:30:00'),
(1, 5, '08:30:00'),
(1, 5, '09:30:00'),
(1, 5, '10:30:00'),
(1, 5, '11:30:00'),
(1, 5, '13:30:00'),
(1, 5, '14:30:00'),
(1, 5, '15:30:00'),
(1, 5, '16:30:00'),
(1, 5, '17:30:00'),
(1, 5, '19:00:00'),
(1, 6, '12:00:00'),
(1, 6, '14:16:00'),
(1, 7, '20:25:00'),
(1, 7, '22:30:00'),
(1, 8, '21:30:00'),
(1, 8, '23:30:00'),
(2, 9, '00:00:00'),
(2, 10, '02:35:00'),
(2, 11, '03:15:00'),
(1, 12, '00:45:00'),
(2, 12, '06:21:00'),
(2, 13, '05:10:00'),
(2, 14, '05:40:00'),
(2, 15, '06:05:00'),
(2, 16, '06:30:00'),
(3, 17, '00:00:00'),
(3, 18, '01:50:00'),
(3, 18, '02:35:00'),
(3, 19, '03:20:00'),
(3, 20, '03:45:00'),
(3, 21, '04:14:00'),
(3, 22, '05:05:00'),
(3, 23, '05:30:00'),
(3, 24, '07:25:00'),
(4, 25, '00:00:00'),
(4, 25, '05:10:00'),
(4, 25, '08:05:00'),
(4, 26, '02:00:00'),
(4, 27, '04:05:00'),
(4, 28, '04:35:00'),
(4, 29, '07:35:00'),
(4, 30, '10:20:00'),
(4, 31, '12:35:00'),
(4, 32, '13:35:00'),
(1, 33, '11:22:33'),
(5, 33, '00:00:00'),
(5, 34, '02:35:00'),
(5, 35, '04:35:00'),
(5, 36, '05:40:00'),
(5, 36, '12:20:00'),
(5, 37, '06:20:00'),
(5, 37, '10:20:00'),
(6, 37, '10:55:00'),
(5, 38, '06:45:00'),
(5, 38, '13:40:00'),
(5, 39, '07:20:00'),
(5, 40, '13:20:00'),
(6, 41, '00:00:00'),
(6, 42, '01:55:00'),
(6, 43, '04:05:00'),
(6, 44, '06:15:00'),
(6, 45, '07:30:00'),
(6, 46, '10:00:00'),
(6, 47, '12:00:00'),
(6, 48, '12:30:00'),
(7, 49, '00:00:00'),
(7, 50, '01:00:00'),
(7, 51, '02:00:00'),
(7, 52, '03:00:00'),
(7, 53, '04:00:00'),
(7, 54, '04:20:00'),
(7, 54, '05:00:00'),
(7, 54, '08:00:00'),
(7, 55, '05:30:00'),
(7, 55, '06:00:00'),
(7, 55, '06:30:00'),
(7, 56, '09:00:00'),
(8, 57, '00:00:00'),
(8, 58, '03:05:00'),
(8, 59, '03:30:00'),
(8, 59, '04:15:00'),
(8, 60, '05:00:00'),
(8, 60, '05:40:00'),
(8, 60, '06:20:00'),
(8, 61, '07:05:00'),
(8, 61, '07:35:00'),
(8, 61, '08:05:00'),
(8, 61, '08:40:00'),
(8, 62, '09:15:00'),
(8, 62, '10:05:00'),
(8, 63, '10:30:00'),
(8, 64, '11:25:00'),
(8, 64, '12:20:00'),
(9, 65, '00:00:00'),
(9, 65, '02:00:00'),
(9, 65, '11:15:00'),
(9, 65, '13:30:00'),
(9, 65, '19:00:00'),
(10, 65, '03:30:00'),
(10, 65, '08:00:00'),
(10, 65, '23:00:00'),
(9, 66, '04:00:00'),
(9, 67, '05:00:00'),
(9, 68, '06:00:00'),
(9, 69, '07:00:00'),
(9, 69, '11:00:00'),
(10, 69, '06:30:00'),
(10, 69, '10:15:00'),
(9, 70, '09:30:00'),
(9, 71, '15:45:00'),
(10, 71, '00:00:00'),
(10, 71, '20:00:00'),
(9, 72, '20:00:00'),
(10, 73, '03:00:00'),
(10, 73, '06:00:00'),
(10, 74, '11:30:00'),
(10, 75, '12:00:00'),
(10, 75, '14:00:00'),
(10, 75, '16:00:00'),
(10, 75, '18:00:00'),
(9, 76, '21:00:00'),
(11, 77, '00:00:00'),
(11, 78, '01:00:00'),
(11, 79, '01:30:00'),
(11, 80, '02:00:00'),
(11, 81, '02:30:00'),
(11, 82, '03:00:00'),
(11, 83, '03:30:00'),
(11, 84, '04:00:00'),
(11, 85, '04:30:00'),
(11, 86, '05:00:00'),
(11, 87, '05:30:00'),
(11, 88, '06:00:00'),
(13, 90, '22:00:00');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `musorok`
--

CREATE TABLE `musorok` (
  `musorid` int(4) NOT NULL,
  `cim` varchar(100) COLLATE utf8_hungarian_ci NOT NULL,
  `tipus` varchar(50) COLLATE utf8_hungarian_ci NOT NULL,
  `hossz` time NOT NULL,
  `korhatar` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- A tábla adatainak kiíratása `musorok`
--

INSERT INTO `musorok` (`musorid`, `cim`, `tipus`, `hossz`, `korhatar`) VALUES
(1, 'HIMNUSZ', 'SZÓRAKOZTATÓ', '00:02:00', 12),
(2, 'MA ÉJSZAKA', 'HÍR- ÉS POLITIKAI MŰSOROK', '00:45:00', 0),
(3, 'HÍRADÓ', 'HÍR- ÉS POLITIKAI MŰSOROK', '00:30:00', 0),
(4, 'NEMZETI SPORTHÍRADÓ', 'HÍR- ÉS POLITIKAI MŰSOROK', '00:05:00', 0),
(5, 'HÍREK', 'HÍR- ÉS POLITIKAI MŰSOROK', '00:03:00', 0),
(6, 'DÉLI HARANGSZÓ', 'HÍR- ÉS POLITIKAI MŰSOROK', '00:01:00', 12),
(7, 'IDŐJÁRÁS-JELENTÉS', 'HÍR- ÉS POLITIKAI MŰSOROK', '00:10:00', 0),
(8, 'VILÁGHÍRADÓ', 'HÍR- ÉS POLITIKAI MŰSOROK', '00:30:00', 0),
(9, 'ELEKTRIP', 'MAGAZIN MŰSOROK', '02:35:00', 0),
(10, 'EUROPE IN CONCERT', 'KULTÚRA, SZÍNHÁZ', '00:40:00', 12),
(11, 'MR2 AKUSZTIK', 'KULTÚRA, SZÍNHÁZ', '01:05:00', 12),
(12, 'STILÓ', 'MAGAZIN MŰSOROK', '00:30:00', 12),
(13, 'MIRR-MURR KALANDJAI', 'SOROZATOK', '00:05:00', 0),
(14, 'MILO', 'SOROZATOK', '00:10:00', 0),
(15, 'RUBI SZIVÁRVÁNYIÁBAN', 'SOROZATOK', '00:10:00', 0),
(16, 'CSŰRCSAVAROSDI', 'SOROZATOK', '00:25:00', 0),
(17, 'MINDENT VAGY SEMMIT?', 'VÍGJÁTÉK', '01:50:00', 16),
(18, 'A HEGYI DOKTOR', 'SOROZATOK', '00:45:00', 12),
(19, 'DIVAT ÉS DIZÁJN', 'MAGAZIN MŰSOROK', '00:25:00', 6),
(20, 'HAZAJÁRÓ', 'DOKUMENTUM', '00:29:00', 12),
(21, 'NOÉ BARÁTAI', 'MAGAZIN MŰSOROK', '00:26:00', 0),
(22, 'ITTHON VAGY!', 'MAGAZIN MŰSOROK', '00:20:00', 0),
(23, 'CSALÁD-BARÁT', 'MAGAZIN MŰSOROK', '01:00:00', 0),
(24, 'KÖZELEBB-ROMA MAGAZIN', 'MAGAZIN MŰSOROK', '00:25:00', 0),
(25, 'LABDARÚGÁS: OTP BANK LIGA', 'SPORT', '02:00:00', 0),
(26, 'SÁRKÖZY TAMÁS JÉGKORONG EMLÉKTORNA', 'SPORT', '02:05:00', 0),
(27, 'SKIPPER', 'MAGAZIN MŰSOROK', '00:30:00', 0),
(28, 'VÍZILABDA MAGAZIN', 'MAGAZIN MŰSOROK', '00:35:00', 0),
(29, 'ÉPÍTŐK MAGAZIN', 'MAGAZIN MŰSOROK', '00:30:00', 0),
(30, 'FORMA-1 BRAZIL NAGYDÍJ', 'SPORT', '02:15:00', 0),
(31, 'SZABADIDŐ', 'MAGAZIN MŰSOROK', '00:30:00', 0),
(32, 'NŐI KÉZILABDA EURÓPA-BAJNOKSÁG', 'SPORT', '01:45:00', 0),
(33, 'ROHANÁS', 'AKCIÓ', '02:35:00', 18),
(34, 'GRAVITÁCIÓ', 'SCI-FI', '02:00:00', 12),
(35, 'CSI: A HELYSZÍNELŐK', 'SOROZATOK', '01:05:00', 16),
(36, 'NEVESS CSAK!', 'SZÓRAKOZTATÓ', '00:40:00', 12),
(37, 'TELESHOP', 'REKLÁM ÉS VÁSÁRLÁS', '00:25:00', 12),
(38, 'FÓKUSZ', 'MAGAZIN MŰSOROK', '00:35:00', 12),
(39, 'REGGELI', 'MAGAZIN MŰSOROK', '03:00:00', 12),
(40, 'AGYMENŐ KÁVÉZÓ', 'SOROZATOK', '00:20:00', 12),
(41, 'LEJTMENET', 'VÍGJÁTÉK', '01:55:00', 16),
(42, 'A TERMÉSZET EREJE', 'AKCIÓ', '02:10:00', 16),
(43, 'ELMOSÓDOTT VALÓSÁG', 'HORROR', '02:10:00', 18),
(44, 'CSALÁDI TITKOK', 'VALÓSÁGSHOW', '01:05:00', 12),
(45, 'MOKKA', 'MAGAZIN MŰSOROK', '02:30:00', 12),
(46, 'MOKKACHINO', 'MAGAZIN MŰSOROK', '00:55:00', 12),
(47, 'CSAPDÁBA CSALVA', 'VALÓSÁGSHOW', '00:30:00', 12),
(48, 'TÉNYEK PLUSZ', 'HÍR- ÉS POLITIKAI MŰSOROK', '00:45:00', 12),
(49, 'BAYER SHOW', 'MAGAZIN MŰSOROK', '01:00:00', 12),
(50, 'HAZAHÚZÓ', 'MAGAZIN MŰSOROK', '01:00:00', 12),
(51, 'POLITIKAI HOBBISTA', 'TALK-SHOW', '01:00:00', 12),
(52, 'CÉLPONT', 'MAGAZIN MŰSOROK', '00:40:00', 12),
(53, 'RADAR', 'MAGAZIN MŰSOROK', '00:20:00', 12),
(54, 'HÁBORÚ UKRAJNÁBAN ', 'HÍR- ÉS POLITIKAI MŰSOROK', '00:40:00', 12),
(55, 'NAPI AKTUÁLIS', 'MAGAZIN MŰSOROK', '00:30:00', 12),
(56, 'MOZAIK', 'MAGAZIN MŰSOROK', '01:30:00', 12),
(57, 'OCEAN\'S TWELVE-EGGYEL NŐ A TÉT', 'THRILLER ', '02:40:00', 16),
(58, 'TRENDKÖZELBEN', 'MAGAZIN MŰSOROK', '00:25:00', 12),
(59, 'SÜTIMESTER-REPETA', 'DOKUMENTUM', '00:45:00', 12),
(60, 'ELFELEDVE', 'SOROZATOK', '00:40:00', 16),
(61, 'JÓBARÁTOK', 'SOROZATOK', '00:30:00', 12),
(62, 'AGYMENŐK', 'SOROZATOK', '00:25:00', 12),
(63, 'DAWSON ÉS A HAVEROK', 'SOROZATOK', '00:55:00', 12),
(64, 'SZÍVEK SZÁLLODÁJA', 'SOROZATOK ', '00:55:00', 12),
(65, 'LABDARÚGÁS-OLASZ BAJNOKSÁG', 'SPORT', '02:00:00', 12),
(66, 'UEFA BAJNOKOK LIGÁJA ÖSSZEFOGLALÓ', 'MAGAZIN MŰSOROK', '01:00:00', 12),
(67, 'TRASH TALK', 'MAGAZIN MŰSOROK', '01:00:00', 12),
(68, 'WORLD POKER TOUR', 'SPORT', '01:00:00', 12),
(69, 'TELEVÍZIÓS VÁSÁRLÁS', 'MAGAZIN MŰSOROK', '02:15:00', 12),
(70, 'HARMADIK FÉLIDŐ', 'MAGAZIN MŰSORO', '01:30:00', 12),
(71, 'KOSÁRLABDA-NBA', 'SPORT', '03:00:00', 12),
(72, 'NYERŐ SZÉRIA', 'MAGAZIN MŰSOROK', '01:00:00', 12),
(73, 'KOSÁRLABDA-NBA ACTION', 'MAGAZIN MŰSOROK', '00:30:00', 12),
(74, 'ÖRDÖGÖK. A FEHÉRVÁR AV19 KLUBTÉVÉJE', 'MAGAZIN MŰSOROK', '00:30:00', 12),
(75, 'LABDARÚGÁS-SPANYOL KUPA', 'SPORT', '02:15:00', 12),
(76, 'DARTS: GRAND SLAM OF DARTS', 'SPORT', '04:00:00', 12),
(77, 'VIOLETTA', 'SOROZATOK', '00:50:00', 12),
(78, 'PIZSIHŐSÖK', 'SOROZATOK', '00:25:00', 12),
(79, 'BINNY ÉS A SZELLEM', 'SOROZATOK', '00:20:00', 12),
(80, 'EVERMOOR TITKAI', 'SOROZATOK ', '00:25:00', 12),
(81, 'SADIE SPARKS', 'SOROZATOK', '00:20:00', 12),
(82, 'MIRACULOUS KATICABOGÁR', 'SOROZATOK', '00:30:00', 12),
(83, 'REJTÉLYEK VÁROSKÁJA', 'SOROZATOK', '00:30:00', 12),
(84, 'GREEN CSALÁD A NAGYVÁROSBAN', 'SOROZATOK', '00:30:00', 12),
(85, 'A MEGÁLLÍTHATATLAN SÁRGA JETI', 'SOROZATOK', '00:30:00', 12),
(86, 'A SZELLEM ÉS MOLLY MCGEE', 'SOROZATOK', '00:30:00', 12),
(87, 'GHOSTFORCE', 'SOROZATOK', '00:30:00', 12),
(88, 'RAVEN OTTHONA', 'SOROZATOK', '00:30:00', 12),
(89, 'Teszt', 'Sori', '00:12:00', 18),
(90, 'TeszMusor', 'Éjjeli kimaradás Az adatb miatt', '04:00:00', 18);

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `szereplok`
--

CREATE TABLE `szereplok` (
  `szereploid` int(4) NOT NULL,
  `nev` varchar(50) COLLATE utf8_hungarian_ci NOT NULL,
  `szuletesiido` date NOT NULL,
  `szarmazasihely` varchar(25) COLLATE utf8_hungarian_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- A tábla adatainak kiíratása `szereplok`
--

INSERT INTO `szereplok` (`szereploid`, `nev`, `szuletesiido`, `szarmazasihely`) VALUES
(1, 'Halász Judit\n', '1942-10-07', 'Magyarország\n'),
(2, 'Tatiana Pauhofová\n', '1983-08-13', 'Szlovákia\n'),
(3, 'Klára Issová\n', '1979-04-26', 'Prága\n'),
(4, 'Michał Żebrowski\n', '1972-06-17', 'Lengyelország\n'),
(5, 'Ľuboš Kostelný\n', '1981-07-05', 'Szlovákia\n'),
(6, 'Ondřej Sokol\n', '1971-10-16', 'Csehország\n'),
(7, 'Paweł Deląg\n', '1970-04-29', 'Lengyelország'),
(8, 'Petr Vaněk\n', '1979-05-08', 'Csehország'),
(9, 'Zuzana Kronerová', '1952-04-17', 'Szlovákia'),
(10, 'Luděk Sobota', '1943-05-27', 'Csehország'),
(11, 'Gerhart Lippert', '1937-03-14', 'Németország'),
(12, 'Anita Zagaria', '1954-06-27', 'Olaszország'),
(13, 'Enzi Fuchs', '1937-01-28', 'Németország'),
(14, 'Walther Reyer', '1922-09-04', 'Ausztria'),
(15, 'Manuel Guggenberger', '1980-10-22', 'Ausztria'),
(16, 'Michaela May', '1952-03-18', 'Németország'),
(17, 'Carin C. Tietze', '1964-10-03', 'USA'),
(18, 'Herbert Fux', '1927-03-25', 'Ausztria'),
(19, 'Thomas Fritsch', '1944-01-16', 'Németország'),
(20, 'Billy Bob Thornton', '1955-08-04', 'USA'),
(21, 'Dwayne Johnson', '1972-05-02', 'USA'),
(22, 'Oliver Jackson-Cohen', '1986-10-24', 'Anglia'),
(23, 'Carla Gugino', '1971-08-29', 'USA'),
(24, 'Maggie Grace', '1983-09-21', 'USA'),
(25, 'Moon Bloodgood', '1975-09-20', 'USA'),
(26, 'Adewale Akinnuoye-Agbaje', '1967-08-22', 'Anglia'),
(27, 'Tom Berenger', '1949-05-31', 'USA'),
(28, 'Courtney Gains', '1965-08-22', 'USA'),
(29, 'Sandra Bullock', '1964-07-26', 'USA'),
(30, 'George Clooney', '1961-05-06', 'USA'),
(31, 'Laurence Fishburne', '1961-07-30', 'USA'),
(32, 'Marg Helgenberger', '1958-11-16', 'USA'),
(33, 'George Eads', '1967-03-01', 'USA'),
(34, 'Jorja Fox', '1968-07-07', 'USA'),
(35, 'Eric Szmanda', '1975-07-24', 'USA'),
(36, 'Robert David Hall', '1947-11-09', 'USA'),
(37, 'Wallace Langham', '1965-03-11', 'USA'),
(38, 'David Berman', '1967-01-04', 'USA'),
(39, 'Paul Guilfoyle', '1949-04-28', 'USA'),
(40, 'Mayim Bialik', '1975-12-12', 'USA'),
(41, 'Swoosie Kurtz', '1944-09-06', 'USA'),
(42, 'Leslie Jordan', '1955-04-29', 'USA'),
(43, 'Kyla Pratt', '1986-09-16', 'USA'),
(44, 'Cheyenne Jackson', '1975-07-12', 'USA'),
(45, 'Lamorne Morris', '1983-08-14', 'USA'),
(46, 'Jim O\'Heir', '1962-02-04', 'USA'),
(47, 'Schuyler Helford', '1991-03-10', 'USA'),
(48, 'Julia Louis-Dreyfus', '1961-01-13', 'USA'),
(49, 'Will Ferrell', '1967-07-16', 'USA'),
(50, 'Miranda Otto', '1967-12-16', 'Ausztrália'),
(51, 'Zach Woods', '1984-09-25', 'USA'),
(52, 'Zoë Carroll Chao', '1985-09-19', 'USA'),
(53, 'Julian Grey', '2006-03-15', 'USA'),
(54, 'Giulio Berruti', '1984-09-27', 'Olaszország'),
(55, 'Kristofer Hivju', '1978-12-07', 'Norvégia'),
(56, 'Ammon Ford', '2006-11-08', 'USA'),
(57, 'Emile Hirsch', '1985-03-13', 'USA'),
(58, 'Kate Bosworth', '1983-01-02', 'USA'),
(59, 'Mel Gibson', '1956-01-03', 'USA'),
(60, 'David Zayas', '1962-08-15', 'Puerto Rico'),
(61, 'Stephanie Cayo', '1988-04-08', 'Peru'),
(62, 'Jorge Luis Ramos', '1961-03-24', 'Puerto Rico'),
(63, 'Blas Diaz', '1977-11-10', 'Puerto Rico'),
(64, 'Rebecca Da Costa', '1984-05-12', 'Brazília'),
(65, 'Milo Ventimiglia', '1977-07-08', 'USA'),
(66, 'Andie MacDowell', '1958-04-21', 'USA'),
(67, 'Johnathon Schaech', '1969-09-10', 'USA'),
(68, 'Logan Browning', '1989-06-09', 'USA'),
(69, 'Brianne Davis', '1982-04-21', 'USA'),
(70, 'Brad Pitt', '1963-12-18', 'USA'),
(71, 'Matt Damon', '1970-10-08', 'USA'),
(72, 'Julia Roberts', '1967-10-28', 'USA'),
(73, 'Catherine Zeta-Jones', '1969-09-25', 'Anglia'),
(74, 'Andy García', '1956-04-12', 'Kuba'),
(75, 'Don Cheadle', '1964-11-29', 'USA'),
(76, 'Vincent Cassel', '1966-11-23', 'Franciaország'),
(77, 'Elliott Gould', '1938-08-29', 'USA'),
(78, 'Jo Brand', '1957-07-23', 'Anglia'),
(79, 'Stana Katić', '1978-04-26', 'USA'),
(80, 'Patrick Heusinger', '1981-02-14', 'USA'),
(81, 'Cara Theobold', '1990-01-08', 'Anglia'),
(82, 'Neil Jackson', '1976-03-05', 'Anglia'),
(83, 'Matt Le Nevez', '1979-01-10', 'Ausztrália'),
(84, 'Natasha Little', '1969-10-02', 'Anglia'),
(85, 'Christopher Colquhoun', '1970-01-10', 'Anglia'),
(86, 'Hugh Quarshie', '1954-12-22', 'Ghána'),
(87, 'Jennifer Aniston', '1969-02-11', 'USA'),
(88, 'Courteney Cox', '1964-06-15', 'USA'),
(89, 'Lisa Kudrow', '1963-07-30', 'USA'),
(90, 'Matt LeBlanc', '1967-07-25', 'USA'),
(91, 'Matthew Perry', '1969-08-19', 'USA'),
(92, 'Annie Parisse', '1975-07-31', 'USA'),
(93, 'David Schwimmer', '1966-11-02', 'USA'),
(94, 'Anna Faris', '1976-11-29', 'USA'),
(95, 'Jim O\'Heir', '1962-02-04', 'USA'),
(96, 'Jim Parsons', '1973-03-24', 'USA'),
(97, 'Johnny Galecki', '1975-04-30', 'Belgium'),
(98, 'Kaley Cuoco', '1985-11-30', 'USA'),
(99, 'Simon Helberg', '1980-12-09', 'USA'),
(100, 'Kunal Nayyar', '1981-04-30', 'Anglia'),
(101, 'Melissa Rauch', '1980-06-23', 'USA'),
(102, 'Kate Micucci', '1980-03-31', 'USA'),
(103, 'James Van Der Beek', '1977-03-08', 'USA'),
(104, 'Katie Holmes', '1978-12-18', 'USA'),
(105, 'Joshua Jackson', '1978-06-11', 'USA'),
(106, 'Michelle Williams', '1980-09-09', 'USA'),
(107, 'Mary Beth Peil', '1940-06-25', 'USA'),
(108, 'Meredith Monroe', '1969-12-30', 'USA'),
(109, 'Mary-Margaret Humes', '1954-04-04', 'USA'),
(110, 'John Wesley Shipp', '1955-01-22', 'USA'),
(111, 'Kerr Smith', '1972-03-09', 'USA'),
(112, 'Lauren Graham', '1967-03-16', 'USA'),
(113, 'Alexis Bledel', '1981-09-16', 'USA'),
(114, 'Melissa McCarthy', '1970-08-26', 'USA'),
(115, 'Keiko Agena', '1973-10-03', 'USA'),
(116, 'Yanic Truesdale', '1970-03-17', 'USA'),
(117, 'Scott Patterson', '1958-09-11', 'USA'),
(118, 'Liza Weil', '1977-06-05', 'USA'),
(119, 'Kelly Bishop', '1944-02-28', 'USA'),
(120, 'Edward Herrmann', '1943-07-21', 'USA'),
(121, 'Diego Ramos', '1972-11-29', 'Argentína'),
(122, 'Martina Stoessel', '1997-03-21', 'Argentína'),
(123, 'Pablo Espinosa', '1992-03-10', 'Spanyolország'),
(124, 'Mercedes Lambre', '1992-10-05', 'Argentína'),
(125, 'Jorge Blanco', '1991-12-19', 'Mexikó'),
(126, 'Nicolás Garnier', '1987-04-23', 'Argentína'),
(127, 'Candelaria Molfese', '1991-01-03', 'Argentína'),
(128, 'Alba Rico Navarro', '1989-02-26', 'Spanyolország'),
(129, 'Lodovica Comello', '1990-04-13', 'Olaszország'),
(130, 'Steffen Groth', '1974-09-16', 'Németország'),
(131, 'Johannes Hallervorden', '1998-09-12', 'Franciaország'),
(132, 'Merle Juschka', '1999-03-19', 'Németország'),
(133, 'Katharina Kaali', '1977-07-18', 'Finnország'),
(134, 'Anna Julia Kapfelsperger', '1985-07-11', 'Portugália'),
(135, 'Simon Mantei', '1984-11-10', 'Németország'),
(136, 'Tilman Pörzgen', '1993-05-12', 'Németország'),
(137, 'Naomi Sequeira', '1994-12-29', 'Ausztrália'),
(138, 'India Ria Amarteifio', '2001-09-17', 'Anglia'),
(139, 'Finney Cassidy', '1998-06-05', 'Anglia'),
(140, 'Cassandra Morris', '1982-04-19', 'USA'),
(141, 'Tara Sands', '1975-09-20', 'USA'),
(142, 'Ogie Banks', '1973-06-13', 'USA'),
(143, 'Raven-Symoné', '1985-12-10', 'USA'),
(144, 'Issac Ryan Brown', '2005-07-12', 'USA'),
(145, 'Navia Robinson', '2005-05-04', 'USA'),
(146, 'Sky Katz', '2004-12-12', 'USA'),
(147, 'Anneliese van der Pol', '1984-09-23', 'Hollandia'),
(148, 'Alec Mapa', '1965-07-10', 'USA'),
(888, 'Mikorka Kálmán', '1901-11-02', 'Kuba'),
(999, 'Teszt Elek', '1901-11-02', 'Atlanta');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `tvcsatornak`
--

CREATE TABLE `tvcsatornak` (
  `csatornaid` int(4) NOT NULL,
  `nev` varchar(20) COLLATE utf8_hungarian_ci NOT NULL,
  `nezettseg` int(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- A tábla adatainak kiíratása `tvcsatornak`
--

INSERT INTO `tvcsatornak` (`csatornaid`, `nev`, `nezettseg`) VALUES
(1, 'M1 HD ', 162000),
(2, 'M2 HD', 102000),
(3, 'DUNA HD', 98000),
(4, 'M4 SPORT HD', 315000),
(5, 'RTL', 505000),
(6, 'TV2', 489000),
(7, 'HÍR TV', 220000),
(8, 'VIASAT3', 165000),
(9, 'SPORT1', 368000),
(10, 'SPORT2', 304000),
(11, 'DISNEY CHANNEL', 401000),
(12, 'NatGeo', 230000),
(13, 'Bence ötlete ', 2147483647);

--
-- Indexek a kiírt táblákhoz
--

--
-- A tábla indexei `jatszik`
--
ALTER TABLE `jatszik`
  ADD PRIMARY KEY (`musorid`,`szereploid`),
  ADD KEY `musorid` (`musorid`),
  ADD KEY `szereploid` (`szereploid`);

--
-- A tábla indexei `kozvetit`
--
ALTER TABLE `kozvetit`
  ADD PRIMARY KEY (`tv_csatornaid`,`idopont`),
  ADD KEY `musorid` (`m_musorid`),
  ADD KEY `csatornaid` (`tv_csatornaid`);

--
-- A tábla indexei `musorok`
--
ALTER TABLE `musorok`
  ADD PRIMARY KEY (`musorid`) USING BTREE;

--
-- A tábla indexei `szereplok`
--
ALTER TABLE `szereplok`
  ADD PRIMARY KEY (`szereploid`);

--
-- A tábla indexei `tvcsatornak`
--
ALTER TABLE `tvcsatornak`
  ADD PRIMARY KEY (`csatornaid`);

--
-- Megkötések a kiírt táblákhoz
--

--
-- Megkötések a táblához `jatszik`
--
ALTER TABLE `jatszik`
  ADD CONSTRAINT `jatszik_ibfk_1` FOREIGN KEY (`musorid`) REFERENCES `musorok` (`musorid`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `jatszik_ibfk_2` FOREIGN KEY (`szereploid`) REFERENCES `szereplok` (`szereploid`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Megkötések a táblához `kozvetit`
--
ALTER TABLE `kozvetit`
  ADD CONSTRAINT `kozvetit_ibfk_1` FOREIGN KEY (`tv_csatornaid`) REFERENCES `tvcsatornak` (`csatornaid`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `kozvetit_ibfk_2` FOREIGN KEY (`m_musorid`) REFERENCES `musorok` (`musorid`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
