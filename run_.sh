#!/bin/bash

while true; do
    python -m test.run_tests --min_task_index 0 --max_task_index 300 --test_results_id first_300_tests 
    echo "wait 5 seconds"
    sleep 5
done
