{ pkgs ? import <nixpkgs> {} }:

pkgs.python3Packages.buildPythonApplication {
  pname = "csv_xlsx_converter";
  src = ./.;
  version = "0.1";
  propagatedBuildInputs = [
   pkgs.python3Packages.pandas
   pkgs.python3Packages.openpyxl
  ];
}