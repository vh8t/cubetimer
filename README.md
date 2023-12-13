## Overwiew

Cubetimer is a lightweight and command-line-based speedcubing timer designed for simplicity and ease of use. It was developed as a school project to provide speedcubers with a straightforward tool to time their solves, generate scrambles, and track their progress.

## Features

- **Simple Interface:** Cubetimer features a minimalist command-line interface, providing a distraction-free environment for speedcubing practice.
- **High Precision Timing:** The timer records solve times with precision up to 3 decimal places of a second, ensuring accurate measurement for competitive speedcubers.
- **Scramble Generator:** The application generates 20-25 move scrambles, offering a diverse set of challenges for every solve.
- **Data Storage:** Cubetimer stores all your solve data in a `times.json` file. This file includes timestamps for each solve, corresponding scramble sequences, and solve times.

## Installation

1. Clone the Cubetimer repository:

    ```bash
    git clone https://github.com/vh8t/cubetimer.git
    ```

2. Navigate to the Cubetimer directory:

    ```bash
    cd cubetimer
    ```

3. Run Cubetimer:

    ```bash
    python3 cubetimer.py
    ```

## Usage

- **Starting and Stopping a Solve:**
    - Run the Cubetimer application.
    - Press `Enter` to start the timer.
    - Press `Enter` again to stop the timer and view your solve time.
    - You can then press `Enter` to generate a new scramble for the next solve.
- **Viewing your top 5 solves:**
    - After completing a solve, instead of pressing `Enter` to generate a new scramble, type `lb` and press `Enter` to view your top 5 runs from the `times.json` file.
- **Exiting the application:**
    - Press a designated key `Ctrl+C` to exit the application.

## Contributing

Contributions to Cubetimer are welcome! If you find any issues or have suggestions for improvements, feel free to create a pull request or open an issue on the GitHub repository.

## License

Cubetimer is open-source software released under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0.html). Feel free to use, modify, and distribute it in accordance with the terms of the license.

Happy Cubing! 🧡🕒🔧