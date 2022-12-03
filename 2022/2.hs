{-# OPTIONS_GHC -Wno-incomplete-patterns #-}
import Framework
import Data.List
import Data.Maybe

data Move = Rock | Paper | Scissors

winsAgainst :: Move -> Move -> Bool
Rock `winsAgainst` Scissors = True
Scissors `winsAgainst` Paper = True
Paper `winsAgainst` Rock = True
_ `winsAgainst` _ = False

allMoves = [Rock, Paper, Scissors]

bonusScore Rock = 1
bonusScore Paper = 2
bonusScore Scissors = 3

scoreFromOutcome :: Move -> Move -> Int
scoreFromOutcome opponent me
  | me `winsAgainst` opponent = 6
  | opponent `winsAgainst` me = 0
  | otherwise = 3

readMove :: Char -> Move
readMove 'A' = Rock
readMove 'B' = Paper
readMove 'C' = Scissors
readMove 'X' = Rock
readMove 'Y' = Paper
readMove 'Z' = Scissors

totalScore :: Move -> Move -> Int
totalScore opponent me = scoreFromOutcome opponent me + bonusScore me

matchMove :: Move -> Char -> Move
matchMove m 'X' = fromJust $ find (m `winsAgainst`) allMoves
matchMove m 'Y' = m
matchMove m 'Z' = fromJust $ find (`winsAgainst` m) allMoves

day1 s = sum [
    totalScore (readMove c1) (readMove c2) | [c1, ' ', c2] <- lines s
  ]
day2 s = sum [
    let opponentMove = readMove c1 in
        totalScore opponentMove (matchMove opponentMove c2)
    | [c1, ' ', c2] <- lines s
  ]
