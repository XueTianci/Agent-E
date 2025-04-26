import argparse
import asyncio
from test.tests_processor import run_single_task_tests

if __name__ == "__main__":
    # Create the parser
    parser = argparse.ArgumentParser(description='Run test suite for specified range of test tasks.')

    # Add arguments
    parser.add_argument('-s', '--take_screenshots', type=bool, default=True,
                        help='Take screenshots after every operation performed (default: False)')
    parser.add_argument('-wait', '--wait_time_non_headless', type=int, default=5,
                        help='Time to wait between test tasks when running in non-headless mode (default: 10 seconds)')
    parser.add_argument('-id', '--test_results_id', type=str, default="",
                        help='A unique identifier for the test results. If not provided, a timestamp is used.')
    parser.add_argument('-config', '--test_config_file', type=str,
                        help='Path to the test configuration file. Default is "test/tasks/test.json" in the project root.')

    # Parse the command line arguments
    args = parser.parse_args()

    task_config = {
        "task_id": "4091bdd3fa64a5b0d912bc08eaf9c824",
        "confirmed_task": "Find the list of neighborhood maps for Brooklyn on new.mta.info.",
        "website": "https://new.mta.info/",
        "reference_length": 5,
        "level": "easy"
    }
    # Run the main function with the provided or default arguments, not passing browser_manager or AutoGenWrapper will cause the test processor to create new instances of them
    asyncio.run(run_single_task_tests(None, None, test_results_id=args.test_results_id, task_config=task_config,
                          take_screenshots=args.take_screenshots, wait_time_non_headless=args.wait_time_non_headless))
