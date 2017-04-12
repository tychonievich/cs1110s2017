#!/bin/bash

here="$(dirname "$(readlink -m "$0")")/"
cd "$here"

git commit -a -m 'autocommit caused by update'
git pull
git push

target="$(readlink -f "$here""../demo_site/")/"
remote=cs1110@stardock.cs.virginia.edu:/home/cs1110/www/
mkdir -p "$target"files/002
mkdir -p "$target"files/001
mkdir -p "$target"files/1111

function pd() {
    while [ $# -gt 0 ]
    do
        # --self-contained 
        #  --css=bootstrap.united.min.css
        pandoc --standalone --to=html5 \
            --smart --html-q-tags \
            --number-sections \
            --title-prefix="CS 1110/1111" \
            --table-of-contents --toc-depth=4 "$here$1" \
            --css=style.css \
            --template=template.html \
            --variable=year:$(date +%Y) \
            --variable="datetime:$(date "+%Y-%m-%d %H:%M")" \
            -o "$target${1%.md}.html"
        shift
    done
}

for f in *.yaml *.list ../schedulify.py
do if [ "$f" -nt schedule.md ]
then
    python3 ../schedulify.py > schedule.md
fi done

for f in cal-shared.yaml ../assignify.py
do if [ "$f" -nt assignments.md ]
then
    python3 ../assignify.py > assignments.md
fi done

head -1 ../assignments.csv > /tmp/assignments.csv
tail -n +2 ../assignments.csv | sort -k3 -t, >> /tmp/assignments.csv

scp "/tmp/assignments.csv" "archimedes.cs.virginia.edu:/var/www/html/cs1110/uploads/assignments.csv"



cd "$here"
for f in *.md
do
    name="${f%.md}"
    if [ "$f" -nt "$target$name.html" ] || [ -n "$1" ] || [ "$(ls -tr *.html | tail -1)" -nt "$target$name.html" ]
    then
        echo 'updating' "$target$name.html"
        pd "$f"
        sed -i 's/XXXX-XX-XX/'"$(stat -c '%y' "$f" | cut -d'.' -f1)"'/g' "$target$name.html"
        sed -i 's/<a href="'$name'.html">\([^<]*\)<\/a>/<span class="visited">\1<\/span>/g' "$target$name.html"
    fi
done


for f in *.{png,svg,jpg,tar,txt,pdf,css,zip,py}
do
    if [ "$f" -nt "$target$f" ]
    then
        echo 'copying' "$f"
        cp "$f" "$target"
    fi
done


for f in files/*
do
    if [ -d "$f" ]
    then
        for g in $f/*
        do
            if [ "$g" -nt "$target$g" ]
            then
                echo 'copying' "$g"
                cp "$g" "$target$g";
            fi
        done
    elif [ "$f" -nt "$target$f" ]
    then
        echo 'copying' "$f"
        cp "$f" "$target/files";
    fi
done


mkdir -p "$target"oh
cp oh/*.{cgi,py} "$target"oh

rsync --update --compress --recursive --times --verbose \
    -e ssh "$target" "$remote"

