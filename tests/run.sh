# Check if received an argument
if (( "$#" != 1 )) ; then
    echo "usage: $0 test.txt"
    exit 1
fi

sed '/^[[:blank:]]*#/d;s/#.*//' $1 | sed '/^\s*$/d' | ace -g ../engvec.dat -f 1> tests.out 2>info.out
egrep "parsed \\d+ / \\d+" info.out