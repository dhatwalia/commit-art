#!/bin/sh

# Delete old dates
rm dates.txt

# Run the date writer
python date_writer.py 2018 Prajwal
python date_writer.py 2019 fabulous

# Read line by line
while IFS= read -r line; do
    # Read the count from file
    count=$(head -n 1 'counter.txt')

    # Prepare the commit message
    message='Update #'$count

    # Update the count in file
    count=$(($count + 1))
    echo $count > 'counter.txt'
    
    git add .
    git commit --date="$line 11:23:00" -m "$message"
done <dates.txt

git push
