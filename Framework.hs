module Framework  where

import System.Environment
import Data.List
import Data.Maybe
import Debug.Trace

splitStr :: String -> Char -> [String]
splitStr s delimiter = case break (== delimiter) s of
  (s', c : rest) -> s' : splitStr rest delimiter
  (s', []) -> [s']