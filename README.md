# HYROX Tracker

HYROX Tracker is a lightweight, mobile-first Progressive Web App (PWA) designed to help athletes practice the official HYROX fitness race format. It provides a structured, ordered checklist of the runs and functional workout stations, complete with integrated timers to track individual section splits and total elapsed time during training sessions.

Rather than just focusing on one category, the app is a comprehensive training companion supporting all official HYROX divisions (including Singles and Doubles) as well as custom-built workout plans.

## Features

- **Full HYROX Division Support**: Pre-configured trackers tailored for official divisions:
  - **Men's Open Singles & Doubles** (e.g., 152kg Sled Push, 103kg Sled Pull)
  - **Men's Pro Singles & Doubles** (e.g., 202kg Sled Push, 153kg Sled Pull)
- **Custom Workout Builder**: A flexible plan creator that lets users build, save, and edit custom workout sequences using official HYROX exercises, perfect for tailoring training runs or scaling workouts.
- **Race-Format Checklist**: Locks the runs and stations in the exact official sequence (from SkiErg to Wall Balls) so athletes can focus on pacing discipline.
- **Integrated Timers**: Tracks individual station/run times, automatically transitions when sections are checked off, and maintains a total session elapsed time.
- **Offline Support (PWA)**: Installable to the home screen and fully capable of running offline, ensuring reliability in gyms with poor cellular reception.
- **Performance Summary**: Generates a detailed breakdown at the end of the session, highlighting total run time, total station time, average pace, and identifying the fastest and slowest stations.
- **Export to Photo**: Allows users to save their session summary as a shareable image.

## Tech Stack

The application is intentionally built with zero heavy frameworks, prioritizing speed, offline reliability, and simplicity.

- **Frontend Core**: Vanilla HTML5, CSS3, and JavaScript (ES6+).
- **State Management**: Browser `localStorage` is used extensively to preserve timer states during accidental reloads and to store custom workout plans locally on the device.
- **PWA Capabilities**: Utilizes a Service Worker (`sw.js`) for aggressive offline caching and a Web App Manifest (`manifest.json`) for native-like installation.
- **DOM to Image**: Includes `html2canvas.min.js` to render the final HTML summary view into a downloadable PNG image.
- **Static Generation Tools**: Includes several Python utility scripts (`generate_pages.py`, `add_home.py`, `add_ms.py`, `add_photo.py`) used to programmatically generate and update the static HTML files across the different tracker variants.

## Application Structure

- **`index.html`**: The main landing page, containing race format info and navigation to the specific division trackers.
- **`hyrox-*-singles.html` / `hyrox-*-doubles.html`**: The core tracker applications pre-configured for different divisions.
- **`hyrox-custom.html`**: The UI for managing, editing, and creating new custom workout sequences.
- **`hyrox-custom-tracker.html`**: The tracking engine that dynamically loads custom sequences from `localStorage` and executes the standard timing logic.
- **`sw.js`**: Service worker script responsible for caching assets for offline use.
- **`manifest.json`**: Configuration for the PWA setup, defining icons, theme colors, and display modes.
- **`vendor/`**: Contains external dependencies (like `html2canvas.min.js`).
- **`assets/` & `icons/`**: Images, graphics, and app icons.

## Running Locally

Because the application uses vanilla web technologies, it can be run using any basic local HTTP server.

```bash
# Using Python
python3 -m http.server 8000

# Using Node.js (http-server)
npx http-server -p 8000
```

Then open `http://localhost:8000` in your web browser.

## Offline Functionality

The app is designed to be added to your mobile device's home screen. On the first visit, the Service Worker caches all necessary HTML, CSS, JavaScript, and image assets. Subsequent visits—even without an internet connection—will load the app instantly from the local cache. All workout progress and custom plans remain strictly local to the device.
