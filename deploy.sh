function deploy
    rm -rf ./src/*.pdf
    pip list --format=freeze > requirements.txt
    git add .
    git commit -m "$argv"
    git push
    git pull
end