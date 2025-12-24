-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 24-12-2025 a las 16:59:42
-- Versión del servidor: 8.4.7
-- Versión de PHP: 8.3.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `kit_shine`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `contactos`
--

DROP TABLE IF EXISTS `contactos`;
CREATE TABLE IF NOT EXISTS `contactos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `apellido` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `correo` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tema` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `mensaje` text COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `contactos`
--

INSERT INTO `contactos` (`id`, `nombre`, `apellido`, `correo`, `tema`, `mensaje`) VALUES
(1, 'Luc%C3%ADa', 'Torreblanca', 'ltorreblanca%40gmail.com', 'garantia', 'Quisiera+saber+la+garant%C3%ADa+de+cada+uno+de+los+productos+en+cat%C3%A1logo.'),
(2, 'Jakeline', 'Tupayachi', 'jtupayachi%40gmail.com', 'productos', 'Me+gustar%C3%ADa+saber+si+hay+ofertas+en+los+productos+de+cat%C3%A1logo.');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `opiniones`
--

DROP TABLE IF EXISTS `opiniones`;
CREATE TABLE IF NOT EXISTS `opiniones` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `apellido` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `correo` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `calificacion` int DEFAULT NULL,
  `comentario` text COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `opiniones`
--

INSERT INTO `opiniones` (`id`, `nombre`, `apellido`, `correo`, `calificacion`, `comentario`) VALUES
(1, 'Alexandra', 'Ch%C3%A1vez', 'dchavez%40gmail.com', 5, '%22El+pedido+me+llego+a+tiempo+y+me+encantaron+todos+los+implementos+%3A3%22'),
(2, 'Milagros', 'Florez', 'mflorez%40gmail.com', 4, 'Me+gustaron+muchos+los+accesorios.');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedidos`
--

DROP TABLE IF EXISTS `pedidos`;
CREATE TABLE IF NOT EXISTS `pedidos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `apellido` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `dni` varchar(15) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `direccion` varchar(150) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `correo` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `producto` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `pago` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `comentarios` text COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `pedidos`
--

INSERT INTO `pedidos` (`id`, `nombre`, `apellido`, `dni`, `direccion`, `correo`, `producto`, `pago`, `comentarios`) VALUES
(1, 'Aleyda', 'Quispe', '72970103', 'Peru+-+Arequipa+-+Cerro+Colorado+-+Calle+Villanueva', 'aquispehach%40unsa.edu.pe', 'kit2', 'tarjeta', 'Estoy+ansiosa+de+poder+obtener+el+kit+shine+que+eleg%C3%AD.'),
(2, 'Sof%C3%ADa', 'Espinoza', '12345678', 'Peru+-+Arequipa+-+Selva+Alegre', 'sespinoza%40gmail.com', 'kit2', 'yape', 'Ninguna.');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
