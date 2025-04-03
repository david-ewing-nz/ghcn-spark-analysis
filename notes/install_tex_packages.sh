#!/bin/bash

# Update tlmgr (TeX Live Manager) to ensure you have the latest package info
echo "Updating tlmgr..."
tlmgr update --self --all

# Define an array of package names to install.
# Note: "graphicx" is provided by the "graphics" package.
packages=(
    "graphics"    # Provides graphicx.sty
    "float"
    "booktabs"
    "fontspec"
    "longtable"
    "array"
    "caption"
    "listings"
    "fancyhdr"
    "hyperref"
    "datetime2"
    "placeins"
    "appendix"
    "biblatex"
)

# Loop through each package and install it.
for pkg in "${packages[@]}"; do
    echo "Installing $pkg..."
    tlmgr install "$pkg"
done

echo "All packages installed."