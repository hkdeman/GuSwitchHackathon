module Paths_GuSwitchHackathon (
    version,
    getBinDir, getLibDir, getDataDir, getLibexecDir,
    getDataFileName, getSysconfDir
  ) where

import qualified Control.Exception as Exception
import Data.Version (Version(..))
import System.Environment (getEnv)
import Prelude

catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
catchIO = Exception.catch

version :: Version
version = Version [0,1,0,0] []
bindir, libdir, datadir, libexecdir, sysconfdir :: FilePath

bindir     = "/home/leodalinci/.cabal/bin"
libdir     = "/home/leodalinci/.cabal/lib/x86_64-linux-ghc-7.10.3/GuSwitchHackathon-0.1.0.0-8Q2nAwydWgL6uXNTBxk1kO"
datadir    = "/home/leodalinci/.cabal/share/x86_64-linux-ghc-7.10.3/GuSwitchHackathon-0.1.0.0"
libexecdir = "/home/leodalinci/.cabal/libexec"
sysconfdir = "/home/leodalinci/.cabal/etc"

getBinDir, getLibDir, getDataDir, getLibexecDir, getSysconfDir :: IO FilePath
getBinDir = catchIO (getEnv "GuSwitchHackathon_bindir") (\_ -> return bindir)
getLibDir = catchIO (getEnv "GuSwitchHackathon_libdir") (\_ -> return libdir)
getDataDir = catchIO (getEnv "GuSwitchHackathon_datadir") (\_ -> return datadir)
getLibexecDir = catchIO (getEnv "GuSwitchHackathon_libexecdir") (\_ -> return libexecdir)
getSysconfDir = catchIO (getEnv "GuSwitchHackathon_sysconfdir") (\_ -> return sysconfdir)

getDataFileName :: FilePath -> IO FilePath
getDataFileName name = do
  dir <- getDataDir
  return (dir ++ "/" ++ name)
