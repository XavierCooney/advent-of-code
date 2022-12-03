{-# OPTIONS_GHC -Wno-incomplete-patterns #-}
import Framework
import Data.List
import Data.Maybe

splitElves l = case break null l of
    (s, []) -> [s]
    (s, "" : rest) -> s : splitElves rest

sumCalories = map (sum . map read)

day1 = maximum . sumCalories . splitElves . lines
day2 = sum . take 3 . reverse . sort . sumCalories . splitElves . lines
