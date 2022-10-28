while true; do
	out=$(hyprctl activewindow -j | sed 's/\n//')
	echo $out
done
