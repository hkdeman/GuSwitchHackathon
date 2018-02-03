import System.Random       (randomRIO)
import Control.Applicative ((<$>))
import Control.Monad       (when)
import Text.Printf         (printf)  

playGame :: Int -> Int -> IO ()
playGame answer curGuesses = do
    putStrLn "What is your guess?"
    putStr   ">"
    guess <- getGuessFromUser
    when (guess /= answer) $ do
        giveHints answer guess
        playGame answer (curGuesses + 1)
    when (guess == answer) $ do
        putStrLn "You guessed it!"
        printf   "You guessed %d times!\n" (curGuesses + 1)

giveHints :: Int -> Int -> IO ()
giveHints answer guess 
    | answer > guess = putStrLn "It's higher!"
    | otherwise      = putStrLn "It's lower!"

getGuessFromUser :: IO Int
getGuessFromUser = do
    read <$> getLine

main :: IO ()
main = do
    answer <- randomRIO (1, 100)
    putStrLn "I'm thinking of a number between 1 and 100."
    playGame answer 0
