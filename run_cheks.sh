# !usr/bin/env bash
echo "Running flake8..."
#find ./server -name "*.py" -print0 | xargs -0 -n 1 flake8 --ignore=E501,E402,E731
find ./MinhaSaude -name "*.py" -print0 | xargs -0 -n 1 flake8 --ignore=E501,E402,E731,E722,E117,F632,E741,W605,W504,F901
find ./msapp -name "*.py" -print0 | xargs -0 -n 1 flake8 --ignore=E501,E402,E731,E722,E117,F632,E741,W605,W504,F901
echo "Done!"
