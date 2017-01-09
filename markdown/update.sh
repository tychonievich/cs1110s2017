#!/bin/bash

git pull
git commit -a -m 'autocommit caused by update'
git push

here="$(dirname "$(readlink -m "$0")")/"
target="$HOME/public_html/1110/S2017/"
remote=cs1110@stardock.cs.virginia.edu/home/cs1110/www/
if [ ! -d "$target" ]
then
	echo "Live destination unreachable"
	target="$here""../demo_site/"
	mkdir -p "$target"
fi
target="$(readlink -f "$target")"

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
            -o "$target${1%.md}.html"
		shift
	done
}

for f in *.yaml ../schedulify.py
do if [ "$f" -nt schedule.md ]
then
	python3 ../schedulify.py > schedule.md
fi done


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
		cp "$f" "$target";
	fi
done


for f in files/*
do
	if [ "$f" -nt "$target$f" ]
	then
		echo 'copying' "$f"
		cp "$f" "$target/files";
	fi
done


echo rsync "$target" "$remote" --recursive --times
