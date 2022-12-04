{-# OPTIONS_GHC -Wno-incomplete-patterns #-}
import Framework
import Data.List

readRange :: String -> [Int]
readRange s = case splitStr s '-' of
  [a, b] -> [(read a) .. (read b)]

readLine :: String -> ([Int], [Int])
readLine s = case splitStr s ',' of
  [a, b] -> (readRange a, readRange b)

day1 = length . filter (\(a, b) -> a `isInfixOf` b || b `isInfixOf` a) . map readLine . lines

day2 = length . filter (not . null) . map (uncurry intersect . readLine) . lines