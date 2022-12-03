{-# OPTIONS_GHC -Wno-incomplete-patterns #-}
import Framework
import Data.List
import Data.Maybe ( fromJust )

only [x] = x

priority :: String -> Int
priority = fromJust . flip elemIndex (['a' .. 'z'] ++ ['A' .. 'Z']) . only . nub

splitIntoHalf :: [a] -> ([a], [a])
splitIntoHalf line = splitAt (length line `div` 2) line

day1 :: String -> Int
day1 = sum . map (priority . uncurry intersect . splitIntoHalf) . lines

findBadges :: [String] -> [Int]
findBadges [] = []
findBadges linesLeft =
  let (group, rest) = splitAt 3 linesLeft
      badge = foldr1 intersect group in
  priority badge : findBadges rest

day2 = sum . findBadges . lines
