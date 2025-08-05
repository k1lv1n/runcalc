echo Start working of solver. Numbers go brrr
echo $(ls)
SCRIPT_DIR="$(dirname "$(realpath "$0")")"

grep diam "$SCRIPT_DIR/input_text.txt" >> "$SCRIPT_DIR/outputs/output_text.txt"

zip -r "$SCRIPT_DIR/outputs/outputs.zip" "$SCRIPT_DIR/outputs"