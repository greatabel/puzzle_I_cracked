for f in *; do mv "$f" "i0${f:1}"; done

# http://stackoverflow.com/questions/17386836/bash-rename-files-with-prefix-serial-number
# http://stackoverflow.com/questions/208181/how-to-rename-with-prefix-suffix