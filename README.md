<p align="center">
  <img src="media/logo.png" alt="MiyaDesktop Logo" width="200">
</p>

MiyaDesktop helps you regain control of a cluttered desktop by organizing shortcuts and folders without touching important files.
With a single action, it reduces visual noise while keeping everything accessible.

<p align="center">
  <img src="media/BeforeAfter.png" alt="Before and After — MiyaDesktop cleans your messy desktop" />
</p>

The result of MiyaDesktop’s automatic organization — the same desktop, cleaned and structured without deleting user data.

---

## Main UI

<p align="center">
  <img src="media/main_ui.png" alt="MiyaDesktop Main Interface" />
</p>

MiyaDesktop’s main interface acts as a central control hub for all features of the application. From here, users can access the Add Application manager, Music player, Neon customization, theme switching, and startup behavior in a single window.

The interface also includes controls for toggling Miya’s animated display, adjusting font and GIF size, and configuring API access for the online version. A clearly marked red Override Mode button provides advanced control over restricted system paths for experienced users.

The Custom button allows users to upload and use their own GIF instead of the four built-in options, which is then displayed in the live preview window outside the main MiyaDesktop panel.

---

## Neon customization

<p align="center">
  <img src="media/neon.png" alt="MiyaDesktop Neon Customization" />
</p>

MiyaDesktop’s Neon mode lets users customize the visual style of interface elements, including button highlights, toggles, and window borders.

The neon system is fully optional — its colors and effects can be adjusted to suit different moods, or disabled completely for a neutral, distraction-free interface.

---

## Add Application

<p align="center">
  <img src="media/add.png" alt="MiyaDesktop Add Application Interface" />
</p>

The Add Application interface provides both manual and automated ways to register applications and folders within MiyaDesktop. The Add button allows users to manually select any file or folder, while the Auto button scans the Desktop and automatically collects shortcuts and folders, excluding individual files and images. A dedicated Folder Toggle determines whether folders detected by Auto are copied into MiyaDesktop/Desktop/ or only registered within the app.

Below the controls, a centralized management window displays all added items, where users can rename, edit, or remove entries at any time. Each entry can be assigned a custom name, which Miya can later recognize — when the user presses Ctrl + M and says “open {name},” Miya searches this list and opens the matching application or folder if it exists.

---

## Music

<p align="center">
  <img src="media/music.png" alt="MiyaDesktop Music Player Interface" />
</p>

The Music interface functions as an integrated media player within MiyaDesktop, displaying all tracks detected from the system’s registered Music folder. Users can control playback, volume, and track navigation directly from this panel, with repeat enabled by default.

Multiple playback modes are available, including Repeat (default), Juggle (shuffle), and Straight (sequential play), allowing for different listening preferences. A built-in Add Music option enables users to download tracks through yt-dlp and immediately make them available within the player.

---

## Shortcuts

### General

| Key           | Action                                                                                |
| ------------- | ------------------------------------------------------------------------------------- |
| **ESC**       | Close current page (Music, Neon Picker, or Add Application) and return to main window |
| **Backspace** | Minimize the window                                                                   |

### Navigation

| Key   | Opens                |
| ----- | -------------------- |
| **1** | Add Application Page |
| **2** | Music Page           |
| **3** | Choose Neon Colour   |
| **4** | Custom GIF           |
| **5** | GIF Size Settings    |
| **6** | API Settings         |

### Add Application

| Action         | Behavior                      |
| -------------- | ----------------------------- |
| Double-tap row | Open edit window              |
| Tap Delete     | Remove entry from MiyaDesktop |
| **1**          | Open Add Application window   |
| **2**          | Toggle Auto Add Applications  |

### Music controls

| Key       | Action        |
| --------- | ------------- |
| **← / →** | Change track  |
| **↑ / ↓** | Adjust volume |
| **Enter** | Play / Pause  |

### Playtback modes

| Key   | Mode                  |
| ----- | --------------------- |
| **1** | Repeat                |
| **2** | Juggle (Shuffle)      |
| **3** | Straight (Sequential) |
| **4** | Open music list       |
| **5** | Open add music window |

---

## Limitations & Notes

Voice Recognition

Offline version has limited accuracy.

Online version depends on your network speed.

Speech recognition may be reduced when no internet connection is available.

Add Application Behavior

Does not touch individual files or photos on the Desktop — only folders and shortcuts.

Folders are copied, not moved; deleting from Desktop is always the user’s choice.

Users can safely delete Desktop shortcuts after they are registered in MiyaDesktop.

Memory Usage

MiyaDesktop typically uses ~30 MB of RAM while idle.

While playing music, RAM usage may increase to ~150–180 MB.

Startup & Background

Enabling startup does not slow system boot; Miya launches quietly in the background.

Music Playback & Download

Music may stop if the window goes to sleep.

Temporary freezing during music download via yt-dlp is normal.

Removal

Uninstalling MiyaDesktop does not delete any user files or folders.

---
