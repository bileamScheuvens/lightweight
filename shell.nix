let
  pkgs = import <nixpkgs> { };
in
  pkgs.mkShell {
    LD_LIBRARY_PATH = "$LD_LIBRARY_PATH:${pkgs.stdenv.cc.cc.lib}/lib";
  }